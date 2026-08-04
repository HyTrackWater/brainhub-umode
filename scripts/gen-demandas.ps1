# Gera D-AAAA-NNN.md para um cliente a partir do CSV consolidado de Demandas (export do Notion).
#
# Uso: .\gen-demandas.ps1 -ClientCsvName 'Cambos' -ClientFolder 'Cambos' -CsvPath '...\demandas.csv'
#
# Historico de versoes deste script:
# v1 (10 jul 2026) — gerou as 236 demandas dos 4 clientes-piloto a partir do export
#    "Demandas Totais CSV e Markdown" (jul 2026, pasta ja removida do repositorio).
# v2 (03 ago 2026) — replicacao total. Mudancas, todas registradas em
#    protocolo-gestao-demanda.md ANTES de rodar:
#      - CSV virou parametro (-CsvPath); a pasta de dado bruto nao vive mais no repositorio
#      - coluna de 1o nivel de status: 'Propriedade' (export jul) OU 'Status' (export mar) —
#        resolvida dinamicamente, mesmos valores de enum nas duas
#      - coluna de cliente resolvida por padrao (o emoji do Notion chega mojibake em alguns exports)
#      - 16 combos novos de Status+Etapa
#      - Criticidade 'Critica / Urgente' -> Urgente ; 'Baixa' -> [a preencher] + valor bruto em nota
#      - Area Responsavel sem correspondencia (ex.: 'INOVACAO / IA') -> [a preencher] + valor bruto
#      - emite os campos que o template ganhou depois da v1: 'Status (interno)', 'Vinculada?',
#        'Vinculo' (antes eram aplicados por script de retrofit separado)
#      - fallback de data aceita mes em ingles (export mar) alem de portugues (export jul)

param(
  [Parameter(Mandatory=$true)][string]$ClientCsvName,
  [Parameter(Mandatory=$true)][string]$ClientFolder,
  [Parameter(Mandatory=$true)][string]$CsvPath,
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode",
  [string]$FonteNota = 'export "Demandas de Clientes" (Drive `1U3B3MwvjnImUXB4I4XDP906huCvflFVK`, snapshot de 05 mar 2026)',
  # -Casa: a demanda e da propria Casa uMode (a base tem linhas com Cliente = uMode). Muda o
  # destino do arquivo e a Natureza (interna, nao casa-cliente) — ver protocolo-gestao-demanda.md.
  [switch]$Casa
)

$ErrorActionPreference = 'Stop'
$outDir = if ($Casa) { Join-Path $Root "uMode\00_Institucional\_demandas" } else { Join-Path $Root "uMode\_Clientes\$ClientFolder\00_Institucional\_demandas" }
New-Item -ItemType Directory -Path $outDir -Force | Out-Null

$mesesPt = @{
  'janeiro'=1;'fevereiro'=2;'março'=3;'abril'=4;'maio'=5;'junho'=6;'julho'=7;
  'agosto'=8;'setembro'=9;'outubro'=10;'novembro'=11;'dezembro'=12
}
$mesesEn = @{
  'january'=1;'february'=2;'march'=3;'april'=4;'may'=5;'june'=6;'july'=7;
  'august'=8;'september'=9;'october'=10;'november'=11;'december'=12
}

function Parse-Data($row) {
  $ds = $row.'Data da Solicitação'
  if ($ds -and $ds -match '(\d{1,2})/(\d{1,2})/(\d{4})') {
    return [pscustomobject]@{ Date=[datetime]::new([int]$Matches[3],[int]$Matches[2],[int]$Matches[1]); Display="{0:D2}/{1:D2}/{2}" -f [int]$Matches[1],[int]$Matches[2],[int]$Matches[3]; FromFallback=$false }
  }
  $ce = $row.'Criado em'
  if ($ce -and $ce -match '(\d{1,2}) de (\w+) de (\d{4})') {
    $day=[int]$Matches[1]; $mes=$Matches[2].ToLower(); $year=[int]$Matches[3]
    if ($mesesPt.ContainsKey($mes)) {
      return [pscustomobject]@{ Date=[datetime]::new($year,$mesesPt[$mes],$day); Display="{0:D2}/{1:D2}/{2}" -f $day,$mesesPt[$mes],$year; FromFallback=$true }
    }
  }
  if ($ce -and $ce -match '(\w+)\s+(\d{1,2}),\s*(\d{4})') {
    $mes=$Matches[1].ToLower(); $day=[int]$Matches[2]; $year=[int]$Matches[3]
    if ($mesesEn.ContainsKey($mes)) {
      return [pscustomobject]@{ Date=[datetime]::new($year,$mesesEn[$mes],$day); Display="{0:D2}/{1:D2}/{2}" -f $day,$mesesEn[$mes],$year; FromFallback=$true }
    }
  }
  return $null
}

function Get-AreaCxHub($areaResp) {
  switch ($areaResp.Trim()) {
    'KA' { return @('Operação','Operação | KA') }
    'PRODUTO' { return @('Operação','Produto | Inovação') }
    'TECH' { return @('Tech','Suporte Tech') }
    'OPERAÇÃO' { return @('Operação','Sem Área') }
    default { return @('[a preencher]','[a preencher]') }
  }
}

function Get-Status($nivel1, $etapa) {
  $key = "$($nivel1.Trim())|$($etapa.Trim())"
  switch ($key) {
    # --- mapeados na v1 (Lofty, jul 2026) e na extensao de 10 jul 2026
    'Não iniciada|Backlog' { return 'Backlog' }
    'Não iniciada|' { return 'Backlog' }
    'Standby - Produto|Backlog' { return 'Backlog' }
    'Standby - Produto|Na Fila' { return 'Backlog' }
    'Nível de Análise|Análise Cliente' { return 'Análise' }
    'Nível de Análise|Em Validação - Cliente' { return 'Análise' }
    'Demanda Aceita|Em Desenvolvimento' { return 'Em Progresso' }
    'Demanda Aceita|Em Validação - Cliente' { return 'Aguardando Validação' }
    'Demanda Aceita|Em Teste' { return 'Em Revisão' }
    'Concluída|Demanda Concluída' { return 'Concluído' }
    'Concluída|Em Validação - Cliente' { return 'Concluído' }
    'Encerrada|Demanda Cancelada' { return 'Cancelado' }
    # --- combos achados em 03 ago 2026 (replicacao total)
    'Não iniciada|Análise uMode' { return 'Backlog' }
    'Não iniciada|Em Desenvolvimento' { return 'Backlog' }
    'Standby - Produto|Análise uMode' { return 'Backlog' }
    'Nível de Análise|Análise uMode' { return 'Análise' }
    'Nível de Análise|Na Fila' { return 'Análise' }
    'Nível de Análise|Backlog' { return 'Análise' }
    'Nível de Análise|' { return 'Análise' }
    'Demanda Aceita|Na Fila' { return 'A fazer' }
    'Demanda Aceita|Análise uMode' { return 'Análise' }
    'Demanda Aceita|Análise Cliente' { return 'Análise' }
    'Demanda Aceita|Demanda Concluída' { return 'Em Progresso' }
    'Concluída|Na Fila' { return 'Concluído' }
    'Encerrada|Demanda Concluída' { return 'Cancelado' }
    'Encerrada|Backlog' { return 'Cancelado' }
    'Encerrada|Em Validação - Cliente' { return 'Cancelado' }
    'Encerrada|Análise uMode' { return 'Cancelado' }
    # --- combos achados em 03 ago 2026, 2a rodada (fonte de jul 2026)
    'Concluída|' { return 'Concluído' }
    'Standby - Produto|' { return 'Backlog' }
    'Standby - Produto|Análise Cliente' { return 'Backlog' }
    'Encerrada|Na Fila' { return 'Cancelado' }
    'Não iniciada|Análise Cliente' { return 'Backlog' }
    'Demanda Aceita|Backlog' { return 'A fazer' }
    default { return $null }
  }
}

# combos em que Status e Etapa se contradizem: Status prevalece, conflito vira nota
$combosConflitantes = @(
  'Concluída|Em Validação - Cliente','Demanda Aceita|Demanda Concluída','Concluída|Na Fila',
  'Não iniciada|Análise uMode','Não iniciada|Em Desenvolvimento','Encerrada|Demanda Concluída',
  'Encerrada|Em Validação - Cliente','Encerrada|Análise uMode','Não iniciada|Análise Cliente'
)

function Get-Tipo($tipo) {
  $t = $tipo.Trim()
  switch ($t) {
    'Erro/ Bug' { return 'Bug' }
    'Melhoria / Desenvolvimento' { return 'Melhoria' }
    '' { return '[a preencher]' }
    default { return $t }
  }
}

# Bloqueio (Notion) -> Motivo de bloqueio. Tabela registrada em protocolo-gestao-demanda.md.
# So 'Aguardando o Cliente' tem equivalente exato; o resto vai pra 'Outra' mantendo o valor
# original visivel, porque o enum nao cobre esses motivos.
function Get-Bloqueio($bloqueio) {
  $b = (Limpa $bloqueio)
  if ($b -eq '') { return '' }
  if ($b -eq 'Aguardando o Cliente') { return 'Aguardando Cliente' }
  return "Outra — valor legado do Notion: ""$b"""
}

function Limpa($v) {
  if ($null -eq $v) { return '' }
  $bs = [string][char]92
  $pat = '[' + $bs + $bs + ']([^a-zA-Z0-9\s])'
  $x = $v -replace '\s*\(https?://[^)]*\)', ''
  $x = $x -replace $pat, '$1'
  return ($x -replace "`r", '').Trim()
}

function Achata($v) { return ((Limpa $v) -replace "`n", ' · ') }

function Clean-Title($desc, $idLegado) {
  if (-not $desc) { return "Demanda $idLegado" }
  $lines = @($desc -split "`n" | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' })
  if ($lines.Count -eq 0) { return "Demanda $idLegado" }
  $t = $lines[0]
  $t = $t -replace '^[•◦\-\*·]\s*', ''
  $t = $t -replace '\\([^a-zA-Z0-9\s])', '$1'
  $t = $t.Trim()
  if ($t.Length -gt 90) { $t = $t.Substring(0,87).Trim() + '…' }
  if ($t -eq '') { return "Demanda $idLegado" }
  return $t
}

function Format-Body($text) {
  if (-not $text -or $text.Trim() -eq '') { return @('[a preencher]') }
  $lines = @($text -split "`n" | ForEach-Object { $_.TrimEnd() })
  $out = New-Object System.Collections.Generic.List[string]
  foreach ($l in $lines) {
    $tl = $l.Trim()
    if ($tl -eq '') { continue }
    if ($tl -match '^◦\s*(.*)$') { $out.Add("  - " + $Matches[1]) }
    elseif ($tl -match '^[•\-]\s*(.*)$') { $out.Add("- " + $Matches[1]) }
    else { $out.Add($tl) }
  }
  if ($out.Count -eq 0) { return @('[a preencher]') }
  return $out
}

# ---------------------------------------------------------------- fonte
$all = Import-Csv $CsvPath
$cols = $all[0].PSObject.Properties.Name
$colCli = ($cols | Where-Object { $_ -like '*Clientes*' } | Select-Object -First 1)
$colNivel1 = if ($cols -contains 'Propriedade') { 'Propriedade' } else { 'Status' }
if (-not $colCli) { throw "Coluna de cliente nao encontrada no CSV de demandas" }

# normaliza os dois lados: o export do Notion escapa markdown no valor (ex.: "Básico\&Co")
function Norm-Nome($v) { return (Limpa $v) }
$alvo = Norm-Nome $ClientCsvName
$rows = $all | Where-Object { @($_.$colCli -split '\),' | ForEach-Object { Norm-Nome (($_ -split ' \(http')[0]) }) -contains $alvo }

# ---- mapa das RFIs ja formalizadas deste cliente, pra resolver o vinculo bidirecional
# (coluna 'RFI' do Notion traz o NOME da pagina da RFI; nossos arquivos guardam nome + ID)
function Chave($s) { return (($s -replace '[^\p{L}\p{N}]', '').ToLower()) }
$mapaRfi = @{}
$rfiDir = if ($Casa) { $null } else { Join-Path $Root "uMode\_Clientes\$ClientFolder\00_Institucional\_rfis" }
if ($rfiDir -and (Test-Path $rfiDir)) {
  foreach ($arq in (Get-ChildItem $rfiDir -Filter "RFI-*.md" -File)) {
    $ls = @(Get-Content -Encoding UTF8 $arq.FullName)
    $iId = [array]::IndexOf($ls, '### ID')
    $iNome = [array]::IndexOf($ls, '### Nome / Descrição')
    if ($iId -ge 0 -and $iNome -ge 0) {
      $k = Chave $ls[$iNome + 1]
      if ($k -ne '' -and -not $mapaRfi.ContainsKey($k)) { $mapaRfi[$k] = @{ Id = $ls[$iId + 1]; Nome = $ls[$iNome + 1] } }
    }
  }
}
Write-Output "$ClientCsvName : $($rows.Count) linhas encontradas (coluna nivel1='$colNivel1')"
if ($rows.Count -eq 0) { return }

$parsed = foreach ($r in $rows) {
  $d = Parse-Data $r
  if (-not $d) { Write-Warning "SEM DATA: ID $($r.ID) - $($r.'Descrição da Solicitação')"; continue }
  [pscustomobject]@{ Row=$r; DateInfo=$d }
}

$sorted = $parsed | Sort-Object { $_.DateInfo.Date }
$counters = @{}
$unmappedStatus = New-Object System.Collections.Generic.List[string]
$generated = New-Object System.Collections.Generic.List[string]

foreach ($item in $sorted) {
  $r = $item.Row
  $year = $item.DateInfo.Date.Year
  if (-not $counters.ContainsKey($year)) { $counters[$year] = 0 }
  $counters[$year]++
  $id = "D-{0}-{1:D3}" -f $year, $counters[$year]

  $notas = New-Object System.Collections.Generic.List[string]
  $obsFonte = $r.'Observações'.Trim()

  $areaResp = $r.'Área Responsável'
  $quadroArea = Get-AreaCxHub $areaResp
  $quadro = $quadroArea[0]; $areaCx = $quadroArea[1]
  if ($areaResp.Trim() -ne '' -and $quadro -eq '[a preencher]') {
    $notas.Add("[Dado legado preservado: ``Área Responsável`` (Notion) = ""$($areaResp.Trim())"" — sem correspondência no enum de Área (CX Hub); Quadro/Área ficaram [a preencher], ver protocolo-gestao-demanda.md]")
  }

  $nivel1 = $r.$colNivel1
  $status = Get-Status $nivel1 $r.'Etapa'
  if (-not $status) {
    $unmappedStatus.Add("$id : nivel1='$($nivel1)' Etapa='$($r.Etapa)'")
    $status = '[a preencher]'
  }
  $comboKey = "$($nivel1.Trim())|$($r.'Etapa'.Trim())"
  if ($combosConflitantes -contains $comboKey) {
    $notas.Add("[Observação: dado legado com Status/Etapa conflitantes — ""$($nivel1.Trim())"" (status) vs ""$($r.'Etapa'.Trim())"" (etapa); mapeado como $status por prevalência do Status, conforme protocolo-gestao-demanda.md]")
  }

  # o campo 'Bloqueio' real prevalece sobre a regra automatica de Standby (motivo real > inferido)
  $bloqReal = Get-Bloqueio $r.'Bloqueio'
  $motivoBloqueio = if ($bloqReal -ne '') { $bloqReal }
                    elseif ($nivel1.Trim() -eq 'Standby - Produto') { 'Aguardando Decisão' }
                    else { '[a preencher]' }

  # ---- RFI vinculada (vinculo bidirecional exigido pelo protocolo)
  $rfiFonte = Limpa $r.'RFI'
  if ($rfiFonte -ne '') {
    $k = Chave $rfiFonte
    if ($mapaRfi.ContainsKey($k)) {
      $rfiVinculada = "$($mapaRfi[$k].Id) — $($mapaRfi[$k].Nome)"
    } else {
      $rfiVinculada = "$rfiFonte [nome bruto da RFI no Notion — não casou com nenhuma RFI formalizada deste cliente; reconciliar manualmente, ver protocolo-gestao-rfi.md]"
    }
  } else {
    $rfiVinculada = '[a preencher]'
  }

  $tipo = Get-Tipo $r.'Tipo de Demanda'

  # Prioridade: enum (Media/Alta/Urgente), com Criticidade como fallback
  $prioridade = '[a preencher]'
  $p = $r.'Prioridade'.Trim(); $c = $r.'Criticidade'.Trim()
  if (@('Média','Alta','Urgente') -contains $p) { $prioridade = $p }
  elseif (@('Média','Alta','Urgente') -contains $c) { $prioridade = $c }
  elseif ($c -eq 'Crítica / Urgente') { $prioridade = 'Urgente' }
  if ($prioridade -eq '[a preencher]') {
    if ($p -ne '') { $notas.Add("[Dado legado preservado: ``Prioridade`` (Notion) = ""$p"" — fora do enum de Prioridade (Média/Alta/Urgente), não convertido por suposição de escala]") }
    if ($c -ne '') { $notas.Add("[Dado legado preservado: ``Criticidade`` (Notion) = ""$c"" — sem valor equivalente no enum de Prioridade, ver protocolo-gestao-demanda.md]") }
  }

  $criador = if ($r.'Criado por'.Trim() -ne '') { $r.'Criado por'.Trim() } else { '[a preencher]' }
  $responsavel = if ($r.'Key Account/Responsável'.Trim() -ne '') { $r.'Key Account/Responsável'.Trim() } else { '[a preencher]' }

  $quemSolicitou = $r.'Quem solicitou?'.Trim()
  $escopo = if ($Casa) { "Casa uMode" } else { "Cliente:$ClientFolder" }
  $origem = if ($quemSolicitou -ne '') { "$escopo - solicitado por: $quemSolicitou" } else { $escopo }
  $natureza = if ($Casa) { "interna" } else { "casa-cliente" }

  $entregaPrevista = if ($r.'Data de Previsão de Entrega'.Trim() -ne '') { $r.'Data de Previsão de Entrega'.Trim() } else { '[a preencher]' }
  $conclusaoReal = if ($r.'Data de Conclusão'.Trim() -ne '') { $r.'Data de Conclusão'.Trim() } else { '[a preencher]' }

  $horas = if ($r.'Horas de Demanda'.Trim() -ne '') { $r.'Horas de Demanda'.Trim() } elseif ($r.'Horas - Recurso Específico'.Trim() -ne '') { $r.'Horas - Recurso Específico'.Trim() } else { '[a preencher]' }

  $titulo = Clean-Title $r.'Descrição da Solicitação' $r.ID
  $anexos = if ($r.'Arquivos e mídia'.Trim() -ne '') { $r.'Arquivos e mídia'.Trim() } else { '[a preencher]' }
  $ultimaEdicao = $r.'Última edição'.Trim()
  $idLegado = if ($r.ID.Trim() -ne '') { $r.ID.Trim() } else { '[a preencher]' }

  # ---- colunas legadas sem campo equivalente no padrao: preservadas, nunca descartadas
  # (tabela registrada em protocolo-gestao-demanda.md)
  $legado = New-Object System.Collections.Generic.List[string]
  foreach ($par in @(
      @('Responsabilidade','Responsabilidade'), @('Projeto','Projeto'),
      @('uMode - Macro Tema','uMode - Macro Tema'), @('Comentário uMode','Comentário uMode'),
      @('Suporte Integração','Suporte Integração'), @('Tempo de Resolução','Tempo de Resolução'),
      @('Nível de Esforço','Nível de Esforço'))) {
    $v = Achata $r.($par[0])
    if ($v -ne '') { $legado.Add("- ``$($par[1])``: $v") }
  }

  $notasInternas = @()
  if ($obsFonte -ne '') { $notasInternas += (Format-Body $obsFonte) }
  if ($notas.Count -gt 0) { $notasInternas += $notas }
  if ($legado.Count -gt 0) {
    $notasInternas += '[Campos legados do Notion sem campo equivalente no padrão — preservados aqui'
    $notasInternas += 'para não perder dado; ver protocolo-gestao-demanda.md]'
    $notasInternas += $legado
  }
  if ($notasInternas.Count -eq 0) { $notasInternas = @('[a preencher]') }

  $lines = New-Object System.Collections.Generic.List[string]
  $lines.Add("# $titulo · Demanda")
  $lines.Add("")
  $lines.Add("## Identificação")
  $lines.Add("### ID")
  $lines.Add($id)
  $lines.Add("### ID legado (Notion/CX Hub)")
  $lines.Add($idLegado)
  $lines.Add("### Natureza")
  $lines.Add($natureza)
  $lines.Add("### Origem (organizacional)")
  $lines.Add($origem)
  $lines.Add("### Destino (organizacional)")
  $lines.Add("[a preencher]")
  $lines.Add("### Data de abertura")
  $lines.Add($item.DateInfo.Display)
  $lines.Add("### Status (interno)")
  $lines.Add("Concluída — demanda já criada e vinculada ao CX Hub (ver Vinculada?); execução acompanhada pelo Status do CX Hub abaixo")
  $lines.Add("")
  $lines.Add("## Taxonomia CX Hub")
  $lines.Add("### Vinculada?")
  $lines.Add("Sim")
  $lines.Add("### Vínculo")
  $lines.Add("CX Hub — ID: $idLegado")
  $lines.Add("### Quadro")
  $lines.Add($quadro)
  $lines.Add("### Área (CX Hub)")
  $lines.Add($areaCx)
  $lines.Add("### Status")
  $lines.Add($status)
  $lines.Add("### Prioridade")
  $lines.Add($prioridade)
  $lines.Add("### Tipo")
  $lines.Add($tipo)
  $lines.Add("### Origem (CX Hub)")
  $lines.Add("[a preencher]")
  $lines.Add("### Criador")
  $lines.Add($criador)
  $lines.Add("### Responsável")
  $lines.Add($responsavel)
  $lines.Add("### Co-responsáveis")
  $lines.Add("[a preencher]")
  $lines.Add("### Datas")
  $lines.Add("Início Previsto: [a preencher] · Entrega Prevista: $entregaPrevista · Início Real: [a preencher] · Conclusão Real: $conclusaoReal")
  $lines.Add("### Horas atribuídas")
  $lines.Add($horas)
  $lines.Add("### Motivo de bloqueio")
  $lines.Add($motivoBloqueio)
  $lines.Add("### RFI vinculada")
  $lines.Add($rfiVinculada)
  $lines.Add("")
  $lines.Add("## Relacionamentos")
  $lines.Add("### Demanda mãe")
  $lines.Add("[a preencher]")
  $lines.Add("### Demandas filhas")
  $lines.Add("[a preencher]")
  $lines.Add("")
  $lines.Add("## Conteúdo")
  $lines.Add("### Descrição")
  foreach ($ln in (Format-Body $r.'Descrição da Solicitação')) { $lines.Add($ln) }
  # coluna 'Texto' = corpo da pagina; vem preenchida em pouquissimos casos, mas quando vem e a
  # unica narrativa real que o export de CSV entrega
  $textoPagina = if ($r.PSObject.Properties.Name -contains 'Texto') { (Limpa $r.'Texto') } else { '' }
  if ($textoPagina -ne '') {
    $lines.Add("")
    $lines.Add("> Corpo da página (coluna ``Texto`` do export do Notion):")
    foreach ($ln in (Format-Body $r.'Texto')) { $lines.Add($ln) }
  }
  $lines.Add("### Resultado esperado")
  $lines.Add("[a preencher]")
  $lines.Add("### Notas internas")
  foreach ($l in $notasInternas) { $lines.Add($l) }
  $lines.Add("### Resolução")
  $lines.Add("[a preencher]")
  $lines.Add("### Anexos e links")
  $lines.Add($anexos)
  $lines.Add("")
  $lines.Add("## Subdemandas")
  $lines.Add("[a preencher]")
  $lines.Add("")
  $lines.Add("## Conversas")
  $lines.Add("[a preencher]")
  $lines.Add("")
  $lines.Add("## Contexto")
  $lines.Add("### Contexto consultado")
  $lines.Add("[a preencher]")
  $lines.Add("### Contexto impactado")
  $lines.Add("[a preencher]")
  $lines.Add("")
  $lines.Add("## Aprovação de contexto")
  $lines.Add("### Aprovação necessária")
  $lines.Add("Não")
  $lines.Add("### Quem aprova")
  $lines.Add("[a preencher]")
  $lines.Add("### Status da aprovação")
  $lines.Add("Nenhuma aprovação pendente")
  $lines.Add("")
  $lines.Add("## Marcos")
  $lines.Add("| Data | Evento/decisão | Responsável | Novo status |")
  $lines.Add("|---|---|---|---|")
  $lines.Add("| $($item.DateInfo.Display) | Solicitação registrada (dado legado Notion) | $criador | $status |")
  if ($ultimaEdicao -ne '') {
    $lines.Add("| $ultimaEdicao | Última edição registrada no Notion (legado) | [a preencher] | $status |")
  }
  $lines.Add("| 03/08/2026 | Formalizada no padrão BrainHub a partir do $FonteNota | [a preencher] | $status |")
  $lines.Add("")
  $lines.Add("## Governança")
  $lines.Add("### Quem pode alterar este documento")
  $lines.Add("[a preencher]")

  $outPath = Join-Path $outDir "$id.md"
  [System.IO.File]::WriteAllLines($outPath, $lines, (New-Object System.Text.UTF8Encoding($false)))
  $generated.Add($id)
}

Write-Output "Gerados: $($generated.Count) arquivos"
if ($unmappedStatus.Count -gt 0) {
  Write-Warning "COMBOS DE STATUS NAO MAPEADOS ($($unmappedStatus.Count)):"
  $unmappedStatus | ForEach-Object { Write-Warning $_ }
}



