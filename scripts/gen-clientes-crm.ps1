# Gera a casa completa de um cliente (estrutura de pastas + institucional.md + jornada.md +
# pessoas.md) a partir do CRM "Mapa de Clientes" e da base "Reunioes Compartilhadas com Clientes".
#
# Segue protocolo-criacao-cliente.md (passos 1, 2 e 4) e replica exatamente a estrutura de
# uMode/_Clientes/_template_cliente. Campo sem dado na fonte fica sempre [a preencher].
# Nao gera contexto-area.md: os 4 clientes-piloto tambem nao tem (pendencia 9), e criar 14
# arquivos vazios por cliente divergiria do padrao real aplicado.
#
# Uso:
#   .\gen-clientes-crm.ps1 -CsvCrm '...\crm-mapa-clientes.csv' -CsvReunioes '...\reunioes-clientes.csv'
#   .\gen-clientes-crm.ps1 ... -Only 'Osklen','NK STORE'      (subconjunto)
#   .\gen-clientes-crm.ps1 ... -WhatIfList                    (so lista o que faria)

param(
  [Parameter(Mandatory=$true)][string]$CsvCrm,
  [Parameter(Mandatory=$true)][string]$CsvReunioes,
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode",
  [string[]]$Only,
  [switch]$WhatIfList,
  # fontes extra para montar 'Aliases do cliente' (ver _auditoria-indexacao.md):
  # nomes de pasta da pasta Drive "Clientes" e o CSV de RFIs (cujos titulos usam apelidos)
  [string[]]$PastasDrive = @(),
  [string]$CsvRfis
)

$ErrorActionPreference = 'Stop'

# --- linhas do CRM que NAO sao cliente (ver _lista-clientes-reais.md) ---
$naoClientes = @('uMode', '. Página Cliente [Template]', 'Fornecedores')

# --- clientes que ja tem casa formalizada: nunca sobrescrever ---
$jaExistem = @('Lofty Style', 'Cambos', 'Luiza Barcelos', 'Moda Objetiva')

# --- as 14 areas canonicas (CONTEXT.md) na convencao de pasta ja aplicada ---
$areas = @(
  '01_Planejamento','02_Estilo-Criacao','03_Desenvolvimento-de-Colecao','04_Qualidade','05_PCP',
  '06_Compras-Supply-Sourcing','07_Logistica-CD','08_Ecommerce-Cadastro','09_Comercial-Vendas',
  '10_Marketing','11_Financeiro','12_Design','13_Modelagem','14_Engenharia'
)

$ID_CRM = '1_Bt8qKNeTVnlDAaeM1oOdoWgBmb6ek8k'
$ID_REU = '1mxs-UE3a_fF0MZMDlfh_zG9RldkbDmpa'
$SNAP   = 'snapshot de 05 mar 2026'
$HOJE   = '03 ago 2026'

function Clean-Value([string]$v) {
  if ($null -eq $v) { return '' }
  $v = $v -replace '\s*\(https?://www\.notion\.so/[^)]*\)', ''   # relacao do Notion -> so o nome
  $v = $v -replace '\\([^a-zA-Z0-9\s])', '$1'                     # desescapa markdown do Notion (inclui \_)
  $v = $v -replace "`r", ''
  return $v.Trim()
}

function Has([string]$v) { return ($v -and $v.Trim() -ne '') }

function OrPlaceholder([string]$v) { if (Has $v) { return (Clean-Value $v) } else { return '[a preencher]' } }

function Flat([string]$v) {
  $c = Clean-Value $v
  return ($c -replace "`n", ' · ')
}

# ---------------------------------------------------------------- fontes
$crm = Import-Csv $CsvCrm
$reu = Import-Csv $CsvReunioes
$colNome = ($crm[0].PSObject.Properties.Name | Where-Object { $_ -like '*Nome Fantasia*' })
$colKA   = ($crm[0].PSObject.Properties.Name | Where-Object { $_ -like '*Key Account*' })
$colCN   = ($crm[0].PSObject.Properties.Name | Where-Object { $_ -like '*Consultor de Neg*' })
$colCham = ($crm[0].PSObject.Properties.Name | Where-Object { $_ -like 'Chamado*Atendimento*' })

# rede de seguranca: nome de coluna que nao existe na fonte descartaria dado em silencio
$colunasEsperadas = @(
  'Status','Razão Social','CNPJ','Endereço','Cidade','Estado','Quantidade de Lojas',
  'Área de Atuação','Setor da Empresa','Receita Anual','Segmentação Grupos',
  'Data Ativação Cliente','ERP/Integração','Módulos contratados','Módulos','Produto',
  'Acessos contratados','Relatórios','Usuários totais mês atual (exceto inativos e cancelados)',
  'Time de Atendimento','Drive Operação','Portal do Cliente','Documentação Clientes','OKRs',
  'Material/Apresentação','Onde Estamos','Sucesso do Cliente','O que falta','Tamanho atendimento',
  'Departamento','Email Principal Financeiro','Flag','Última edição','Última edição por',
  'Fashion AI - Escopo Geral','Fashion AI - Integração','uRocket - Módulos Contratados',
  'uRocket - Integração','uRocket - Contatos Contratados','uRocket - Instâncias contratas',
  'uRocket - Mensagens Contradas','3A - Controle de Troca de Emails','Grupo do Whatsapp Oficial'
)
$reais = $crm[0].PSObject.Properties.Name
$faltando = @($colunasEsperadas | Where-Object { $reais -notcontains $_ })
if ($faltando.Count -gt 0) { throw "Colunas ausentes no CSV do CRM: $($faltando -join ' | ')" }
if (-not $colCham) { throw "Coluna de Chamado/Atendimento nao encontrada no CSV do CRM" }

# ---------------------------------------------------------------- ID e aliases
# ID do cliente: slug estavel derivado do nome do CRM. Nao muda se o nome comercial mudar —
# a partir daqui e ele, nao o nome da pasta, a chave logica do cliente.
function Slugify($nome) {
  $s = $nome.Normalize([Text.NormalizationForm]::FormD)
  $sb = New-Object Text.StringBuilder
  foreach ($ch in $s.ToCharArray()) {
    if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($ch) -ne [Globalization.UnicodeCategory]::NonSpacingMark) { [void]$sb.Append($ch) }
  }
  return (($sb.ToString().ToLower() -replace '[^a-z0-9]+','-').Trim('-'))
}

# apelidos usados nos titulos de RFI (ex.: "NK", "NK Store" para NK STORE; "Lofty" para Lofty Style)
$aliasRfi = @{}
if ($CsvRfis -and (Test-Path $CsvRfis)) {
  $rf = Import-Csv $CsvRfis
  $cCli = @($rf[0].PSObject.Properties.Name | Where-Object { $_ -like '*Clientes*' -and $_ -notlike '*Demandas*' })[0]
  $cNom = @($rf[0].PSObject.Properties.Name | Where-Object { $_ -eq 'Nome' })[0]
  foreach ($row in $rf) {
    $clientes = @($row.$cCli -split '\),' | ForEach-Object { Clean-Value (($_ -split ' \(http')[0]) } | Where-Object { $_ -ne '' })
    $titulo = Clean-Value $row.$cNom
    if ($titulo -eq '' -or $clientes.Count -ne 1) { continue }   # multi-cliente: prefixo e ambiguo
    $prefixo = (($titulo -split '\|')[0]).Trim()
    $prefixo = ($prefixo -replace '\s*RFI.*$','').Trim()
    if ($prefixo -eq '' -or $prefixo.Length -gt 30) { continue }
    $k = $clientes[0]
    if (-not $aliasRfi.ContainsKey($k)) { $aliasRfi[$k] = New-Object System.Collections.Generic.List[string] }
    if (-not $aliasRfi[$k].Contains($prefixo)) { $aliasRfi[$k].Add($prefixo) }
  }
}

$alvos = foreach ($r in $crm) {
  $n = (Clean-Value $r.$colNome)
  if ($naoClientes -contains $n) { continue }
  if ($jaExistem -contains $n)   { continue }
  if ($Only -and ($Only -notcontains $n)) { continue }
  [pscustomobject]@{ Nome = $n; Row = $r }
}

Write-Output "Clientes a gerar: $($alvos.Count)"
if ($WhatIfList) { $alvos | ForEach-Object { Write-Output " - $($_.Nome)" }; return }

$resumo = New-Object System.Collections.Generic.List[string]

foreach ($alvo in $alvos) {
  $nome = $alvo.Nome
  $r = $alvo.Row
  $dir = Join-Path $Root "uMode\_Clientes\$nome"

  # ---------------- passo 1 · estrutura de pastas
  foreach ($sub in @('_contexto','_protocolos','_demandas','_rfis')) {
    New-Item -ItemType Directory -Force -Path (Join-Path $dir "00_Institucional\$sub") | Out-Null
  }
  foreach ($a in $areas) {
    foreach ($sub in @('_contexto','_protocolos')) {
      New-Item -ItemType Directory -Force -Path (Join-Path $dir "$a\$sub") | Out-Null
    }
  }

  # ---------------- dados do CRM
  $status      = OrPlaceholder $r.'Status'
  $razao       = Clean-Value  $r.'Razão Social'
  $cnpj        = Clean-Value  $r.'CNPJ'
  $endereco    = Clean-Value  $r.'Endereço'
  $cidade      = Clean-Value  $r.'Cidade'
  $estado      = Clean-Value  $r.'Estado'
  $lojas       = Clean-Value  $r.'Quantidade de Lojas'
  $atuacao     = Clean-Value  $r.'Área de Atuação'
  $setor       = Clean-Value  $r.'Setor da Empresa'
  $receita     = OrPlaceholder $r.'Receita Anual'
  $grupoSeg    = OrPlaceholder $r.'Segmentação Grupos'
  $dataAtiv    = Clean-Value  $r.'Data Ativação Cliente'
  $erp         = OrPlaceholder $r.'ERP/Integração'
  $modContrat  = Clean-Value  $r.'Módulos contratados'
  $modulos     = Clean-Value  $r.'Módulos'
  $produto     = Clean-Value  $r.'Produto'
  $acessos     = Clean-Value  $r.'Acessos contratados'
  $relatorios  = Clean-Value  $r.'Relatórios'
  $usuarios    = Clean-Value  $r.'Usuários totais mês atual (exceto inativos e cancelados)'
  $ka          = Clean-Value  $r.$colKA
  $cn          = Clean-Value  $r.$colCN
  $time        = Clean-Value  $r.'Time de Atendimento'
  $driveOp     = Clean-Value  $r.'Drive Operação'
  $portal      = Clean-Value  $r.'Portal do Cliente'
  $docs        = Clean-Value  $r.'Documentação Clientes'
  $okrs        = Clean-Value  $r.'OKRs'
  $material    = Clean-Value  $r.'Material/Apresentação'
  $chamados    = Clean-Value  $r.$colCham
  $ondeEstamos = Clean-Value  $r.'Onde Estamos'
  $sucesso     = Clean-Value  $r.'Sucesso do Cliente'
  $oQueFalta   = Clean-Value  $r.'O que falta'
  $tamanho     = Clean-Value  $r.'Tamanho atendimento'
  $depto       = Clean-Value  $r.'Departamento'
  $emailFin    = Clean-Value  $r.'Email Principal Financeiro'
  $flag        = Clean-Value  $r.'Flag'
  $ultEdicao   = Clean-Value  $r.'Última edição'
  $ultEdPor    = Clean-Value  $r.'Última edição por'
  $faiEscopo   = Clean-Value  $r.'Fashion AI - Escopo Geral'
  $faiInteg    = Clean-Value  $r.'Fashion AI - Integração'
  $uRocketMod  = Clean-Value  $r.'uRocket - Módulos Contratados'
  $uRocketInt  = Clean-Value  $r.'uRocket - Integração'
  $uRocketCont = Clean-Value  $r.'uRocket - Contatos Contratados'
  $uRocketInst = Clean-Value  $r.'uRocket - Instâncias contratas'
  $uRocketMsg  = Clean-Value  $r.'uRocket - Mensagens Contradas'
  $emails3A    = Clean-Value  $r.'3A - Controle de Troca de Emails'
  $whats       = Clean-Value  $r.'Grupo do Whatsapp Oficial'

  # responsavel de atendimento (uMode)
  $respPartes = New-Object System.Collections.Generic.List[string]
  if (Has $ka)   { $respPartes.Add("$ka (Key Account)") }
  if (Has $cn)   { $respPartes.Add("$cn (Consultor de Negócios)") }
  $resp = if ($respPartes.Count -gt 0) { $respPartes -join ' · ' } else { '[a preencher]' }

  # ---------------- reunioes deste cliente
  $minhas = @($reu | Where-Object { (Clean-Value $_.Cliente) -eq $nome })
  $comData = @($minhas | Where-Object { $_.Data -match '^\s*(\d{1,2})/(\d{1,2})/(\d{4})' })
  $semData = @($minhas | Where-Object { $_.Data -notmatch '^\s*(\d{1,2})/(\d{1,2})/(\d{4})' })
  $ordenadas = $comData | Sort-Object {
    $null = $_.Data -match '(\d{1,2})/(\d{1,2})/(\d{4})'
    [datetime]::new([int]$Matches[3], [int]$Matches[2], [int]$Matches[1])
  }

  # participantes observados (NAO classificados uMode x cliente)
  $participantes = @()
  if ($minhas.Count -gt 0) {
    $participantes = $minhas | ForEach-Object { (Clean-Value $_.Participantes) -split ',' } |
      ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' } |
      Group-Object | Sort-Object Count -Descending
  }

  # ================================================================ institucional.md
  $L = New-Object System.Collections.Generic.List[string]
  $L.Add("# $nome · Institucional")
  $L.Add("")
  $L.Add("> Gerado em $HOJE a partir do CRM ""Mapa de Clientes"" (Drive ``$ID_CRM``, $SNAP).")
  $L.Add("> Todo campo sem dado na fonte está como ``[a preencher]`` — nada foi inferido.")
  $L.Add("")
  $L.Add("## Identidade")
  $L.Add("### ID do cliente")
  $L.Add((Slugify $nome))
  $L.Add("> Slug estável derivado do nome no CRM. **Não muda** se o nome comercial mudar — é a chave")
  $L.Add("> lógica deste cliente (o nome da pasta é só apresentação). Ver ``_auditoria-indexacao.md``.")
  $L.Add("### Aliases do cliente")
  $als = New-Object System.Collections.Generic.List[string]
  $als.Add("$nome (CRM ""Mapa de Clientes"" — nome canônico)")
  foreach ($pd in $PastasDrive) {
    if ($pd -ne $nome -and $pd.ToLower() -eq $nome.ToLower()) { $als.Add("$pd (pasta Drive ""Clientes"" — mesma grafia, caixa diferente)") }
  }
  if ($aliasRfi.ContainsKey($nome)) {
    foreach ($a in $aliasRfi[$nome]) {
      if ($a -ne $nome) { $als.Add("$a (prefixo usado nos títulos de RFI no Notion)") }
    }
  }
  foreach ($a in $als) { $L.Add("- $a") }
  $L.Add("### Quem são")
  $idPartes = New-Object System.Collections.Generic.List[string]
  if (Has $razao)    { $idPartes.Add("Razão Social: $razao") }
  if (Has $cnpj)     { $idPartes.Add("CNPJ: $cnpj") }
  if (Has $lojas)    { $idPartes.Add("Quantidade de lojas: $lojas") }
  if (Has $endereco) { $idPartes.Add("Endereço: $endereco") }
  if ($idPartes.Count -gt 0) { $L.Add(($idPartes -join ' · ')) } else { $L.Add('[a preencher]') }
  $L.Add("### O que fazem")
  $L.Add("[a preencher]")
  $L.Add("### Para quem fazem")
  $L.Add("[a preencher]")
  $L.Add("")
  $L.Add("## Posicionamento")
  $L.Add("### Segmento")
  $segPartes = New-Object System.Collections.Generic.List[string]
  if (Has $atuacao) { $segPartes.Add($atuacao) }
  if (Has $setor)   { $segPartes.Add($setor) }
  $local = @($cidade, $estado | Where-Object { Has $_ }) -join ' / '
  if (Has $local)   { $segPartes.Add($local) }
  if ($segPartes.Count -gt 0) { $L.Add(($segPartes -join ' — ')) } else { $L.Add('[a preencher]') }
  $L.Add("### Receita anual")
  $L.Add($receita)
  $L.Add("### Grupo de segmentação uMode")
  $L.Add($grupoSeg)
  $L.Add("")
  $L.Add("## Operação uMode")
  $L.Add("### Status atual")
  $L.Add($status)
  if ($status -in @('Regime CS','Negociação')) {
    $L.Add("> ⚠ ``$status`` é valor do enum do CRM e **não existe** no enum do template")
    $L.Add("> (Inativo / Pré Onboarding / Operação Assistida / Onboarding / Sem CS / Ongoing / Churn).")
    $L.Add("> Registrado literalmente como está na fonte — nenhuma equivalência foi presumida")
    $L.Add("> (pendência aberta em ``_pendencias-gerais.md``).")
  }
  $L.Add("### Data de ativação")
  if (Has $dataAtiv) { $L.Add($dataAtiv) } else { $L.Add('[não informada]') }
  $L.Add("### Módulos contratados")
  $modLinhas = New-Object System.Collections.Generic.List[string]
  if (Has $modContrat) { $modLinhas.Add("- Módulos contratados (CRM): $(Flat $modContrat)") }
  if (Has $modulos)    { $modLinhas.Add("- Módulos (CRM): $(Flat $modulos)") }
  if (Has $produto)    { $modLinhas.Add("- Produto (CRM): $(Flat $produto)") }
  if (Has $acessos)    { $modLinhas.Add("- Acessos contratados (CRM): $(Flat $acessos)") }
  if (Has $usuarios)   { $modLinhas.Add("- Usuários ativos no mês da fonte (CRM): $(Flat $usuarios)") }
  if (Has $relatorios) { $modLinhas.Add("- Relatórios (CRM): $(Flat $relatorios)") }
  if (Has $uRocketMod) { $modLinhas.Add("- uRocket — módulos contratados (CRM): $(Flat $uRocketMod) · ferramenta legada, descontinuada segundo o Vinicius (13 jul 2026) — contratação histórica") }
  if (Has $uRocketCont){ $modLinhas.Add("- uRocket — contatos contratados (CRM): $(Flat $uRocketCont)") }
  if (Has $uRocketInst){ $modLinhas.Add("- uRocket — instâncias contratadas (CRM): $(Flat $uRocketInst)") }
  if (Has $uRocketMsg) { $modLinhas.Add("- uRocket — mensagens contratadas (CRM): $(Flat $uRocketMsg)") }
  if (Has $faiEscopo)  { $modLinhas.Add("- Fashion AI — escopo geral (CRM): $(Flat $faiEscopo)") }
  if ($modLinhas.Count -gt 0) { foreach ($m in $modLinhas) { $L.Add($m) } } else { $L.Add('[a preencher]') }
  $L.Add("### ERP / Integração")
  $L.Add((Flat $erp))
  if (Has $uRocketInt) { $L.Add("> uRocket — integração (CRM): $(Flat $uRocketInt)") }
  if (Has $faiInteg)   { $L.Add("> Fashion AI — integração (CRM): $(Flat $faiInteg)") }
  $L.Add("### Responsável de atendimento (uMode)")
  $L.Add($resp)
  if (Has $time) { $L.Add("> Campo ``Time de Atendimento`` no CRM: $(Flat $time)") }
  $L.Add("")
  $L.Add("## Aliases de áreas")
  $L.Add("### Mapeamento alias → canônico")
  $L.Add("| Alias no cliente | Área canônica |")
  $L.Add("|---|---|")
  $L.Add("")
  $L.Add("[a preencher — o CRM não tem campo de alias de área. Preencher a partir de reunião,")
  $L.Add("kick-off ou levantamento direto com o cliente, conforme ``protocolo-criacao-cliente.md``.]")
  $L.Add("")
  $L.Add("## Sistemas e fontes de verdade")
  $L.Add("### Drive de operação")
  if (Has $driveOp) { $L.Add($driveOp) } else { $L.Add('[a preencher]') }
  $L.Add("### Outras fontes")
  $fontes = New-Object System.Collections.Generic.List[string]
  if (Has $portal)   { $fontes.Add("- Portal do Cliente (CRM): $(Flat $portal)") }
  if (Has $docs)     { $fontes.Add("- Documentação Clientes (CRM): $(Flat $docs)") }
  if (Has $okrs)     { $fontes.Add("- OKRs (CRM): $(Flat $okrs)") }
  if (Has $material) { $fontes.Add("- Material/Apresentação (CRM): $(Flat $material)") }
  if (Has $whats)    { $fontes.Add("- Grupo de WhatsApp oficial (CRM): $(Flat $whats)") }
  if (Has $emails3A) { $fontes.Add("- 3A · controle de troca de e-mails (CRM): $(Flat $emails3A)") }
  if (Has $chamados) { $fontes.Add("- Chamados/Atendimento vinculados no CRM: $(Flat $chamados)") }
  if ($fontes.Count -gt 0) { foreach ($x in $fontes) { $L.Add($x) } } else { $L.Add('[a preencher]') }
  $L.Add("")
  $L.Add("## Contexto crítico")
  $ctx = New-Object System.Collections.Generic.List[string]
  if (Has $ondeEstamos) { $ctx.Add("- Onde Estamos (CRM): $(Flat $ondeEstamos)") }
  if (Has $sucesso)     { $ctx.Add("- Sucesso do Cliente (CRM): $(Flat $sucesso)") }
  if (Has $oQueFalta)   { $ctx.Add("- O que falta (CRM): $(Flat $oQueFalta)") }
  if (Has $tamanho)     { $ctx.Add("- Tamanho atendimento (CRM): $(Flat $tamanho)") }
  if (Has $depto)       { $ctx.Add("- Departamento (CRM): $(Flat $depto)") }
  if (Has $flag)        { $ctx.Add("- Flag (CRM): $(Flat $flag)") }
  if (Has $emailFin)    { $ctx.Add("- Email principal financeiro (CRM): $(Flat $emailFin)") }
  if (Has $ultEdicao)   { $ctx.Add("- Última edição do registro no CRM: $(Flat $ultEdicao)$(if (Has $ultEdPor) { " por $(Flat $ultEdPor)" })") }
  # Portal do Cliente, Documentação, OKRs, Material, WhatsApp, 3A e Chamados saíram daqui em
  # 03 ago 2026: são fontes de verdade, e passaram a viver em "Sistemas e fontes de verdade →
  # Outras fontes" (seção nova do template). Ver _auditoria-indexacao.md.
  if ($ctx.Count -gt 0) { foreach ($c in $ctx) { $L.Add($c) } } else { $L.Add('[a preencher]') }
  $L.Add("")
  $L.Add("## Governança")
  $L.Add("### Responsável de atendimento (uMode)")
  $L.Add($resp)
  $L.Add("### Quem pode alterar este documento")
  $L.Add("Responsável de atendimento + liderança de Atendimento uMode")

  [System.IO.File]::WriteAllLines((Join-Path $dir "00_Institucional\_contexto\institucional.md"), $L, (New-Object System.Text.UTF8Encoding($false)))

  # ================================================================ jornada.md
  $J = New-Object System.Collections.Generic.List[string]
  $J.Add("# $nome · Jornada")
  $J.Add("")
  $J.Add("> Atualizar a cada marco relevante — fase, entrega, decisão, incidente.")
  $J.Add("")
  $J.Add("## Status atual")
  $J.Add($status)
  $J.Add("")
  $J.Add("## Fase atual")
  if (Has $ondeEstamos) { $J.Add("$(Flat $ondeEstamos)"); $J.Add("> Campo ``Onde Estamos`` do CRM.") } else { $J.Add('[a preencher]') }
  $J.Add("")
  $J.Add("## Marcos da jornada")
  $J.Add("| Data | Fase | Marco |")
  $J.Add("|---|---|---|")
  if (Has $dataAtiv) { $J.Add("| $dataAtiv | Onboarding | Data oficial de ativação do cliente (CRM) |") }
  foreach ($m in $ordenadas) {
    $d = (Clean-Value $m.Data)
    $fase = if (Has $m.'Tipo Reunião') { Clean-Value $m.'Tipo Reunião' } else { '[a preencher]' }
    $t = (Flat $m.'﻿Nome') -replace '\|', '/'
    if (-not (Has $t)) { $t = '[reunião sem título na fonte]' }
    $J.Add("| $d | $fase | $t |")
  }
  foreach ($m in $semData) {
    $fase = if (Has $m.'Tipo Reunião') { Clean-Value $m.'Tipo Reunião' } else { '[a preencher]' }
    $t = (Flat $m.'﻿Nome') -replace '\|', '/'
    if (-not (Has $t)) { $t = '[reunião sem título na fonte]' }
    $J.Add("| [não informada] | $fase | $t |")
  }
  $J.Add("")
  if ($minhas.Count -gt 0) {
    $J.Add("> Marcos reconstruídos da base ""Reuniões Compartilhadas com Clientes"" (Drive")
    $J.Add("> ``$ID_REU``, $SNAP) — $($minhas.Count) reuniões registradas para este cliente")
    $J.Add("> ($($comData.Count) com data, $($semData.Count) sem data na fonte). A coluna Fase usa o campo ``Tipo Reunião``")
    $J.Add("> da própria base quando ele existe; onde a fonte não traz, fica ``[a preencher]`` —")
    $J.Add("> nenhuma fase foi inferida do título da reunião.")
  } else {
    $J.Add("> Nenhuma reunião registrada para este cliente na base ""Reuniões Compartilhadas com")
    $J.Add("> Clientes"" (Drive ``$ID_REU``, $SNAP).")
  }
  $J.Add("")
  $J.Add("## Entregas comprometidas")
  $J.Add("[a preencher]")
  $J.Add("")
  $J.Add("## Módulos em uso")
  $emUso = @($modContrat, $modulos | Where-Object { Has $_ }) | ForEach-Object { Flat $_ }
  if ($emUso.Count -gt 0) { $J.Add(($emUso -join ' · ')) } else { $J.Add('[a preencher]') }
  $J.Add("")
  $J.Add("## Decisões e restrições registradas")
  $J.Add("[a preencher]")
  $J.Add("")
  $J.Add("## Métricas de sucesso definidas")
  if (Has $sucesso) { $J.Add("$(Flat $sucesso)"); $J.Add("> Campo ``Sucesso do Cliente`` do CRM — objetivo declarado, não métrica aferida.") } else { $J.Add('[a preencher]') }
  $J.Add("")
  $J.Add("## Próximos passos")
  if (Has $oQueFalta) { $J.Add("$(Flat $oQueFalta)"); $J.Add("> Campo ``O que falta`` do CRM.") } else { $J.Add('[a preencher]') }
  $J.Add("")
  $J.Add("## Histórico de incidentes / alertas")
  $J.Add("[a preencher]")
  $J.Add("")
  $J.Add("## Observações")
  $J.Add("- Casa criada em $HOJE pela replicação total (⭐ ORDEM DE PRIORIDADE, ``STATE.md``).")
  $J.Add("- Fonte de cadastro: CRM ""Mapa de Clientes"" (Drive ``$ID_CRM``, $SNAP).")
  $J.Add("- Fonte de marcos: base ""Reuniões Compartilhadas com Clientes"" (Drive ``$ID_REU``, $SNAP).")
  if ($minhas.Count -eq 0) { $J.Add("- Sem reuniões na base compartilhada — jornada ainda sem marcos reais registrados.") }

  [System.IO.File]::WriteAllLines((Join-Path $dir "00_Institucional\_contexto\jornada.md"), $J, (New-Object System.Text.UTF8Encoding($false)))

  # ================================================================ pessoas.md
  $P = New-Object System.Collections.Generic.List[string]
  $P.Add("# $nome · Pessoas")
  $P.Add("")
  $P.Add("## Responsável de atendimento (uMode)")
  $P.Add($resp)
  $P.Add("")
  if (Has $time) { $P.Add("> Campo ``Time de Atendimento`` no CRM: $(Flat $time)"); $P.Add("") }
  $P.Add("> Pessoas da uMode vivem apenas em ``uMode/00_Institucional/_pessoas/`` (regra travada em")
  $P.Add("> ``CONTEXT.md``) — aqui só o vínculo de atendimento, nunca uma segunda identidade.")
  $P.Add("")
  $P.Add("---")
  $P.Add("")
  $P.Add("## Diretoria e decisores")
  $P.Add("[a preencher]")
  $P.Add("")
  $P.Add("## Liderança do projeto (cliente)")
  $P.Add("[a preencher]")
  $P.Add("")
  $P.Add("---")
  $P.Add("")
  $P.Add("## Time do projeto por área")
  $P.Add("[a preencher]")
  $P.Add("")
  if ($participantes.Count -gt 0) {
    $P.Add("> ⚠ **Não confirmado — não usar como dado de pessoa.** A base ""Reuniões Compartilhadas")
    $P.Add("> com Clientes"" (Drive ``$ID_REU``, $SNAP) registra os nomes abaixo")
    $P.Add("> como participantes de reuniões deste cliente, com a frequência indicada. A base")
    $P.Add("> **mistura pessoas da uMode e do cliente no mesmo campo**, sem marcar de que lado cada")
    $P.Add("> uma está — classificar por conta própria repetiria exatamente o risco já registrado no")
    $P.Add("> caso Taís Moser (``_pendencias-gerais.md``). Fica como pista de levantamento:")
    foreach ($g in $participantes) { $P.Add("> - $($g.Name) — $($g.Count) reunião(ões)") }
    $P.Add("")
  }
  $P.Add("---")
  $P.Add("")
  $P.Add("## Financeiro")
  if (Has $emailFin) { $P.Add("E-mail principal financeiro (CRM): $(Flat $emailFin)") } else { $P.Add('[a preencher]') }
  $P.Add("")
  $P.Add("## Tecnologia")
  $P.Add("[a preencher]")

  [System.IO.File]::WriteAllLines((Join-Path $dir "00_Institucional\_contexto\pessoas.md"), $P, (New-Object System.Text.UTF8Encoding($false)))

  $resumo.Add(("{0,-24} status={1,-14} reunioes={2,3} participantes={3,3}" -f $nome, $status, $minhas.Count, $participantes.Count))
}

Write-Output ""
Write-Output "===== RESUMO ====="
$resumo | ForEach-Object { Write-Output $_ }
Write-Output "Total de casas geradas: $($resumo.Count)"



