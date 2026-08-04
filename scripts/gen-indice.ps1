# Gera o indice derivado em _indice/ a partir dos MDs reais.
#
# REGRA: o MD e a fonte de verdade. Este indice e 100% DERIVADO — nunca editar a mao, sempre
# regenerar. Se um numero aqui divergir do MD, o MD esta certo e o indice esta velho.
#
# Por que existe: a auditoria de 03 ago 2026 mostrou que a indexacao ja funciona por convencao
# (posicao de heading, 100% cumprida), mas exige varrer 1.292 arquivos pra qualquer pergunta
# relacional. O indice materializa isso em tabelas consultaveis, sem tocar em nenhum MD e sem
# introduzir frontmatter (que criaria duas fontes de verdade pro mesmo campo).
#
# Uso: .\gen-indice.ps1
#
# NOTA: a funcao de leitura NAO pode se chamar 'Ls' — no PowerShell, alias (ls = Get-ChildItem)
# tem precedencia sobre funcao, e a chamada devolveria FileInfo em vez das linhas do arquivo.

param(
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode",
  [string]$DataGeracao = "03 ago 2026"
)

$ErrorActionPreference = 'Stop'
$cli = Join-Path $Root "uMode\_Clientes"
$out = Join-Path $Root "_indice"
New-Item -ItemType Directory -Force -Path $out | Out-Null

function Linhas($p) { return @(Get-Content -Path $p -Encoding UTF8) }
function Val($ls, $h) {
  $i = [array]::IndexOf($ls, $h)
  if ($i -lt 0) { return '' }
  $j = $i + 1
  while ($j -lt $ls.Count -and ($ls[$j].Trim() -eq '' -or $ls[$j].StartsWith('>'))) { $j++ }
  if ($j -lt $ls.Count -and $ls[$j] -notmatch '^#{1,6}\s') { return $ls[$j].Trim() }
  return ''
}
function Corpo($ls, $h) {
  $i = [array]::IndexOf($ls, $h)
  if ($i -lt 0) { return @() }
  $j = $i + 1; $acc = @()
  while ($j -lt $ls.Count -and $ls[$j] -notmatch '^#{1,6}\s') { if ($ls[$j].Trim() -ne '') { $acc += $ls[$j].Trim() }; $j++ }
  return $acc
}
function Ph($v) { if ($v -like '`[a preencher*' -or $v -like '`[não informada*' -or $v -like '`[nao informada*' -or $v -eq '') { return '' } return $v }
function Rel($p) { return $p.Replace($Root + '\', '').Replace('\', '/') }

# ============================================================ clientes
$pastas = @(Get-ChildItem $cli -Directory | Where-Object { $_.Name -ne '_template_cliente' })
$clientes = New-Object System.Collections.Generic.List[object]
$mapaPastaId = @{}
foreach ($p in $pastas) {
  $arq = Join-Path $p.FullName '00_Institucional\_contexto\institucional.md'
  if (-not (Test-Path $arq)) { continue }
  $ls = Linhas $arq
  $id = Ph (Val $ls '### ID do cliente')
  if ($id -eq '') { $id = $p.Name.ToLower() }
  $mapaPastaId[$p.Name] = $id
  $aliases = @(Corpo $ls '### Aliases do cliente' | ForEach-Object { (($_ -replace '^-\s*','') -split ' \(')[0].Trim() })
  $jorn = Join-Path $p.FullName '00_Institucional\_contexto\jornada.md'
  $marcos = 0
  if (Test-Path $jorn) { $marcos = @(Linhas $jorn | Where-Object { $_ -match '^\|\s*(\d{2}/\d{2}/\d{4}|\[não informada\])' }).Count }
  $clientes.Add([pscustomobject]@{
    client_id       = $id
    pasta           = $p.Name
    aliases         = ($aliases -join ' ; ')
    status          = Ph (Val $ls '### Status atual')
    segmento        = Ph (Val $ls '### Segmento')
    grupo_segmentacao = Ph (Val $ls '### Grupo de segmentação uMode')
    data_ativacao   = Ph (Val $ls '### Data de ativação')
    erp_integracao  = Ph (Val $ls '### ERP / Integração')
    drive_operacao  = Ph (Val $ls '### Drive de operação')
    atendimento     = Ph (Val $ls '### Responsável de atendimento (uMode)')
    qtd_demandas    = @(Get-ChildItem $p.FullName -Recurse -Filter 'D-*.md' -File).Count
    qtd_rfis        = @(Get-ChildItem $p.FullName -Recurse -Filter 'RFI-*.md' -File).Count
    qtd_marcos      = $marcos
    arquivo         = Rel $arq
  })
}
$clientes | Sort-Object client_id | Export-Csv (Join-Path $out 'clientes.csv') -NoTypeInformation -Encoding UTF8

# ============================================================ demandas (clientes + Casa)
$demandas = New-Object System.Collections.Generic.List[object]
$fontes = @()
foreach ($p in $pastas) { $fontes += [pscustomobject]@{ Casa = $mapaPastaId[$p.Name]; Dir = (Join-Path $p.FullName '00_Institucional\_demandas') } }
$fontes += [pscustomobject]@{ Casa = 'umode-casa'; Dir = (Join-Path $Root 'uMode\00_Institucional\_demandas') }
foreach ($f in $fontes) {
  if (-not (Test-Path $f.Dir)) { continue }
  foreach ($arq in (Get-ChildItem $f.Dir -Filter 'D-*.md' -File)) {
    $ls = Linhas $arq.FullName
    $rfi = Ph (Val $ls '### RFI vinculada')
    $demandas.Add([pscustomobject]@{
      demanda_id     = Ph (Val $ls '### ID')
      client_id      = $f.Casa
      id_legado      = Ph (Val $ls '### ID legado (Notion/CX Hub)')
      titulo         = ($ls[0] -replace '^#\s*','' -replace '\s*·\s*Demanda$','')
      natureza       = Ph (Val $ls '### Natureza')
      data_abertura  = Ph (Val $ls '### Data de abertura')
      status_interno = ((Ph (Val $ls '### Status (interno)')) -replace ' —.*$','')
      vinculada      = Ph (Val $ls '### Vinculada?')
      vinculo        = Ph (Val $ls '### Vínculo')
      quadro         = Ph (Val $ls '### Quadro')
      area_cxhub     = Ph (Val $ls '### Área (CX Hub)')
      status_cxhub   = Ph (Val $ls '### Status')
      prioridade     = Ph (Val $ls '### Prioridade')
      tipo           = Ph (Val $ls '### Tipo')
      criador        = Ph (Val $ls '### Criador')
      responsavel    = Ph (Val $ls '### Responsável')
      motivo_bloqueio = Ph (Val $ls '### Motivo de bloqueio')
      rfi_id         = $(if ($rfi -match '^(RFI-\d{4}-\d{3})') { $Matches[1] } else { '' })
      destino_area   = Ph (Val $ls '### Destino (organizacional)')
      arquivo        = Rel $arq.FullName
    })
  }
}
$demandas | Sort-Object client_id, demanda_id | Export-Csv (Join-Path $out 'demandas.csv') -NoTypeInformation -Encoding UTF8

# ============================================================ rfis
$rfis = New-Object System.Collections.Generic.List[object]
foreach ($p in $pastas) {
  $dir = Join-Path $p.FullName '00_Institucional\_rfis'
  if (-not (Test-Path $dir)) { continue }
  foreach ($arq in (Get-ChildItem $dir -Filter 'RFI-*.md' -File)) {
    $ls = Linhas $arq.FullName
    # @(...) obrigatorio: se a secao tiver 1 linha so, o retorno vira string escalar e $nar[0]
    # devolveria o primeiro CARACTERE em vez da linha (bug real, corrigido em 03 ago 2026)
    $nar = @(Corpo $ls '## Conteúdo / narrativa')
    $temNar = ($nar.Count -gt 0 -and -not ($nar[0] -like '`[a preencher*'))
    $rfis.Add([pscustomobject]@{
      rfi_id        = Ph (Val $ls '### ID')
      client_id     = $mapaPastaId[$p.Name]
      id_legado     = Ph (Val $ls '### ID legado (Notion/CX Hub)')
      nome          = Ph (Val $ls '### Nome / Descrição')
      resumo        = Ph (Val $ls '### Resumo do assunto')
      grupo         = Ph (Val $ls '### Grupo')
      status        = Ph (Val $ls '### Status')
      horas_estimadas = Ph (Val $ls '### Horas estimadas')
      valor_negociado = Ph (Val $ls '### Valor negociado com o cliente')
      valor_calculado = Ph (Val $ls '### Valor calculado')
      criado_por    = Ph (Val $ls '### Criado por')
      key_account   = Ph (Val $ls '### Key Account no momento da criação')
      data_criacao  = Ph (Val $ls '### Data de criação')
      tem_narrativa = $temNar
      arquivo       = Rel $arq.FullName
    })
  }
}
$rfis | Sort-Object client_id, rfi_id | Export-Csv (Join-Path $out 'rfis.csv') -NoTypeInformation -Encoding UTF8

# ============================================================ produtos (Portfolio)
$produtos = New-Object System.Collections.Generic.List[object]
$dirProd = Join-Path $Root 'uMode\03_Produto-e-Solucoes'
foreach ($arq in (Get-ChildItem $dirProd -Recurse -Filter 'produto.md' -File | Where-Object { $_.FullName -notlike '*_template_produto*' })) {
  $ls = Linhas $arq.FullName
  $produtos.Add([pscustomobject]@{
    produto_id   = $arq.Directory.Parent.Name   # o arquivo vive em <pasta_do_produto>/_contexto/
    nome         = Ph (Val $ls '### Nome atual')
    nome_legado  = Ph (Val $ls '### Nome legado')
    destino      = Ph (Val $ls '### Destino')
    area_cliente = Ph (Val $ls '### Área canônica do cliente conectada')
    geracao      = Ph (Val $ls '### Geração')
    maturidade   = Ph (Val $ls '### Score de maturidade')
    upstream     = Ph (Val $ls '### Consome de (upstream)')
    downstream   = Ph (Val $ls '### Produz para (downstream)')
    clientes     = Ph (Val $ls '### Clientes que contrataram')
    arquivo      = Rel $arq.FullName
  })
}
$produtos | Sort-Object produto_id | Export-Csv (Join-Path $out 'produtos.csv') -NoTypeInformation -Encoding UTF8

# ============================================================ pessoas da Casa
$pessoas = New-Object System.Collections.Generic.List[object]
$dirP = Join-Path $Root 'uMode\00_Institucional\_pessoas'
foreach ($arq in (Get-ChildItem $dirP -Filter '*.md' -File | Where-Object { $_.Name -ne '_template_pessoa.md' })) {
  $ls = Linhas $arq.FullName
  $ids = New-Object System.Collections.Generic.List[string]
  foreach ($h in @('### Clientes atuais atendidos','### Clientes atendidos historicamente')) {
    foreach ($linha in (Corpo $ls $h)) {
      if ($linha -match '^Como .+?\(\d+\):\s*(.+)$') {
        foreach ($n in ($Matches[1] -split '·')) {
          $n = $n.Trim()
          if ($mapaPastaId.ContainsKey($n) -and -not $ids.Contains($mapaPastaId[$n])) { $ids.Add($mapaPastaId[$n]) }
        }
      }
    }
  }
  $pessoas.Add([pscustomobject]@{
    pessoa_id   = $arq.BaseName
    nome        = Ph (Val $ls '### Nome completo')
    cadeira     = ((Ph (Val $ls '### Cadeira / cargo atual')) -replace '\s*\(papel conforme.*$','')
    status_umode = Ph (Val $ls '### Status na uMode')
    area        = Ph (Val $ls '### Área (organizacional)')
    qtd_clientes = $ids.Count
    clientes    = ($ids -join ' ; ')
    arquivo     = Rel $arq.FullName
  })
}
$pessoas | Sort-Object pessoa_id | Export-Csv (Join-Path $out 'pessoas.csv') -NoTypeInformation -Encoding UTF8

# ============================================================ integracoes
# Eixo aberto em 03 ago 2026: o integracao.md e o 5o tipo de MD de cliente e nao estava no indice.
# 'rfis_citadas' materializa o vinculo que a leitura dos repositorios revelou: o documento tecnico
# cita a RFI pelo numero do CX Hub (ex.: "RFI #83") e o campo 'ID legado (Notion/CX Hub)' das nossas
# RFIs resolve esse numero pro nosso ID. Sem isso, o vinculo existe mas ninguem acha.
$mapaRfiLegado = @{}   # 'RFI-83' -> 'VIX/RFI-2026-005'
foreach ($p in $pastas) {
  foreach ($f in @(Get-ChildItem $p.FullName -Recurse -Filter 'RFI-*.md' -File)) {
    $leg = Ph (Val (Linhas $f.FullName) '### ID legado (Notion/CX Hub)')
    if ($leg -ne '') { $mapaRfiLegado[$leg.ToUpper()] = "$($p.Name)/$($f.BaseName)" }
  }
}
$integracoes = New-Object System.Collections.Generic.List[object]
foreach ($p in $pastas) {
  $arq = Join-Path $p.FullName '00_Institucional\_contexto\integracao.md'
  if (-not (Test-Path $arq)) { continue }
  $ls = Linhas $arq
  # RFI citada no corpo, em qualquer forma ('RFI #83', 'RFI 83', 'RFI-83')
  $cit = New-Object System.Collections.Generic.List[string]
  foreach ($lin in $ls) {
    foreach ($m in [regex]::Matches($lin, 'RFI\s*#?\s*(\d{1,4})')) {
      $k = "RFI-$($m.Groups[1].Value)"
      $alvo = if ($mapaRfiLegado.ContainsKey($k)) { $mapaRfiLegado[$k] } else { "$k (não resolvida)" }
      if (-not $cit.Contains($alvo)) { $cit.Add($alvo) }
    }
  }
  $inc = @($ls | Where-Object { $_ -match '^\|' -and $_ -notmatch '^\|\s*(Data|-{3})' -and $_ -notmatch '^\|---' }).Count
  $integracoes.Add([pscustomobject]@{
    client_id      = if ($mapaPastaId.ContainsKey($p.Name)) { $mapaPastaId[$p.Name] } else { $p.Name.ToLower() }
    pasta          = $p.Name
    erp            = Ph (Val $ls '### ERP / sistema integrado')
    status         = Ph (Val $ls '### Status da integração')
    direcoes       = Ph (Val $ls '### Direções de integração')
    repositorio    = Ph (Val $ls '### Repositório de código')
    tem_documento  = if ((Val $ls '### Tabelas do ERP mapeadas') -like '*a preencher*') { $false } else { $true }
    qtd_incidentes = $inc
    rfis_citadas   = ($cit -join ' ; ')
    responsavel    = Ph (Val $ls '### Responsável técnico')
    arquivo        = Rel $arq
  })
}
$integracoes | Sort-Object client_id | Export-Csv (Join-Path $out 'integracoes.csv') -NoTypeInformation -Encoding UTF8

# ============================================================ README do indice
$comRfi = @($demandas | Where-Object { $_.rfi_id -ne '' }).Count
$comNar = @($rfis | Where-Object { $_.tem_narrativa }).Count
$semDestino = @($demandas | Where-Object { $_.destino_area -eq '' }).Count
$R = New-Object System.Collections.Generic.List[string]
$R.Add('# _indice/ — índice derivado do cérebro')
$R.Add('')
$R.Add('> **Gerado por `scripts/gen-indice.ps1` em ' + $DataGeracao + '. Não editar a mão.**')
$R.Add('> O MD é a fonte de verdade; este índice é derivado dele. Se um número aqui divergir do MD,')
$R.Add('> o MD está certo e o índice está velho — basta regerar.')
$R.Add('')
$R.Add('## Por que existe')
$R.Add('A auditoria de 03 ago 2026 (`uMode/00_Institucional/_contexto/_auditoria-indexacao.md`)')
$R.Add('mostrou que a indexação já funciona por convenção — a posição de heading é um contrato')
$R.Add('cumprido em 100% dos arquivos. O que faltava era **materializar** isso: sem o índice,')
$R.Add('qualquer pergunta relacional exige varrer 1.292 arquivos.')
$R.Add('')
$R.Add('Decisão explícita: **índice derivado, não frontmatter.** Frontmatter nos MDs criaria duas')
$R.Add('fontes de verdade para o mesmo campo (o heading e o metadado), com risco real de divergirem.')
$R.Add('Aqui a duplicação é assumida e descartável — regenerar reconcilia sempre.')
$R.Add('')
$R.Add('## Tabelas')
$R.Add('')
$R.Add('| Arquivo | Linhas | Chave | Liga com |')
$R.Add('|---|---|---|---|')
$R.Add("| ``clientes.csv`` | $($clientes.Count) | ``client_id`` | é a chave de tudo abaixo |")
$R.Add("| ``integracoes.csv`` | $($integracoes.Count) | ``client_id`` | ``rfis_citadas`` resolve RFI do CX Hub → nosso ID |")
$R.Add("| ``demandas.csv`` | $($demandas.Count) | ``demanda_id`` | ``client_id`` · ``rfi_id`` · ``id_legado`` (CX Hub) |")
$R.Add("| ``rfis.csv`` | $($rfis.Count) | ``rfi_id`` | ``client_id`` · ``id_legado`` (Notion) |")
$R.Add("| ``pessoas.csv`` | $($pessoas.Count) | ``pessoa_id`` | ``clientes`` (lista de ``client_id``) |")
$R.Add("| ``produtos.csv`` | $($produtos.Count) | ``produto_id`` | ``area_cliente`` · ``upstream``/``downstream`` (outros produtos) |")
$R.Add('')
$R.Add('`client_id` é o slug estável de `institucional.md → Identidade → ID do cliente`. **Não é o')
$R.Add('nome da pasta** — justamente para que renomear um cliente não quebre vínculo nenhum.')
$R.Add('')
$R.Add('## O que o índice já responde (e o que ainda não)')
$R.Add('')
$R.Add("- ✅ demanda → cliente: $($demandas.Count) de $($demandas.Count)")
$R.Add("- ✅ demanda → RFI: $comRfi vínculos resolvidos")
$R.Add("- ✅ RFI com narrativa real: $comNar de $($rfis.Count)")
$R.Add("- ✅ pessoa da Casa → clientes atendidos: $(@($pessoas | Where-Object { $_.qtd_clientes -gt 0 }).Count) pessoas com vínculo")
$R.Add("- ✅ integração → cliente: $($integracoes.Count) clientes com ``integracao.md``, $(@($integracoes | Where-Object { $_.tem_documento }).Count) com documento técnico lido")
$R.Add("- ✅ integração → RFI (via ``ID legado``): $(@($integracoes | Where-Object { $_.rfis_citadas -ne '' }).Count) integração(ões) citam RFI, e o número do CX Hub resolve pro nosso ID")
$R.Add('  — **é o primeiro vínculo do cérebro cujo eixo não é cliente**')
$R.Add("- ❌ demanda → **Área organizacional**: $semDestino de $($demandas.Count) sem ``Destino`` — o eixo Área")
$R.Add('  continua vazio, e nenhum índice resolve isso: é conteúdo que falta, não estrutura')
$R.Add('  (ver `_pendencias-gerais.md` item 39)')
$R.Add('')
$R.Add('## Como regenerar')
$R.Add('')
$R.Add('```')
$R.Add('powershell -File scripts/gen-indice.ps1')
$R.Add('```')
[System.IO.File]::WriteAllLines((Join-Path $out 'README.md'), $R, (New-Object System.Text.UTF8Encoding($false)))

Write-Output "clientes: $($clientes.Count) | demandas: $($demandas.Count) | rfis: $($rfis.Count) | pessoas: $($pessoas.Count)"
Write-Output "demandas com rfi_id resolvido: $comRfi | rfis com narrativa: $comNar | demandas sem Destino (Area): $semDestino"
Write-Output "indice gravado em: $out"






