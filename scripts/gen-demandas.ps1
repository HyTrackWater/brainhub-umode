# Gera D-AAAA-NNN.md para um cliente a partir do CSV consolidado de Demandas.
# Uso: .\gen-demandas.ps1 -ClientCsvName 'Cambos' -ClientFolder 'Cambos'

param(
  [Parameter(Mandatory=$true)][string]$ClientCsvName,
  [Parameter(Mandatory=$true)][string]$ClientFolder
)

$ErrorActionPreference = 'Stop'
$root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode"
$csvPath = Join-Path $root "Demandas Totais CSV e Markdown\uMode Geral\Databases\Demandas de Clientes ddf1951a8dc242e698e6bae3d1f5a865_all.csv"
$outDir = Join-Path $root "uMode\_Clientes\$ClientFolder\00_Institucional\_demandas"
New-Item -ItemType Directory -Path $outDir -Force | Out-Null

$mesesPt = @{
  'janeiro'=1;'fevereiro'=2;'março'=3;'abril'=4;'maio'=5;'junho'=6;'julho'=7;
  'agosto'=8;'setembro'=9;'outubro'=10;'novembro'=11;'dezembro'=12
}

function Parse-Data($row) {
  $ds = $row.'Data da Solicitação'
  if ($ds -and $ds -match '(\d{1,2})/(\d{1,2})/(\d{4})') {
    return [pscustomobject]@{ Date=[datetime]::new([int]$Matches[3],[int]$Matches[2],[int]$Matches[1]); Display="{0:D2}/{1:D2}/{2}" -f [int]$Matches[1],[int]$Matches[2],[int]$Matches[3]; FromFallback=$false }
  }
  $ce = $row.'Criado em'
  if ($ce -and $ce -match '(\d{1,2}) de (\w+) de (\d{4})') {
    $day=[int]$Matches[1]; $mesNome=$Matches[2].ToLower(); $year=[int]$Matches[3]
    if ($mesesPt.ContainsKey($mesNome)) {
      $dt = [datetime]::new($year,$mesesPt[$mesNome],$day)
      return [pscustomobject]@{ Date=$dt; Display="{0:D2}/{1:D2}/{2}" -f $day,$mesesPt[$mesNome],$year; FromFallback=$true }
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

function Get-Status($prop, $etapa) {
  $p = $prop.Trim(); $e = $etapa.Trim()
  $key = "$p|$e"
  switch ($key) {
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
    default { return $null }
  }
}

function Get-Tipo($tipo) {
  $t = $tipo.Trim()
  switch ($t) {
    'Erro/ Bug' { return 'Bug' }
    'Melhoria / Desenvolvimento' { return 'Melhoria' }
    '' { return '[a preencher]' }
    default { return $t }
  }
}

function Get-Prioridade($prioridade, $criticidade) {
  $p = $prioridade.Trim()
  if (@('Média','Alta','Urgente') -contains $p) { return $p }
  $c = $criticidade.Trim()
  if (@('Média','Alta','Urgente') -contains $c) { return $c }
  return '[a preencher]'
}

function Clean-Title($desc, $idLegado) {
  if (-not $desc) { return "Demanda $idLegado" }
  $lines = @($desc -split "`n" | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' })
  if ($lines.Count -eq 0) { return "Demanda $idLegado" }
  $t = $lines[0]
  $t = $t -replace '^[•◦\-\*·]\s*', ''
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

$rows = Import-Csv $csvPath | Where-Object { $_.'👥 Clientes' -like "*$ClientCsvName*" }
Write-Output "$ClientCsvName : $($rows.Count) linhas encontradas"

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

  $areaResp = $r.'Área Responsável'
  $quadroArea = Get-AreaCxHub $areaResp
  $quadro = $quadroArea[0]; $areaCx = $quadroArea[1]

  $status = Get-Status $r.'Propriedade' $r.'Etapa'
  $statusNote = ''
  if (-not $status) {
    $unmappedStatus.Add("$id : Propriedade='$($r.Propriedade)' Etapa='$($r.Etapa)'")
    $status = '[a preencher]'
  }

  $motivoBloqueio = if ($r.'Propriedade'.Trim() -eq 'Standby - Produto') { 'Aguardando Decisão' } else { '[a preencher]' }

  $tipo = Get-Tipo $r.'Tipo de Demanda'
  $prioridade = Get-Prioridade $r.'Prioridade' $r.'Criticidade'

  $criador = if ($r.'Criado por'.Trim() -ne '') { $r.'Criado por'.Trim() } else { '[a preencher]' }
  $responsavel = if ($r.'Key Account/Responsável'.Trim() -ne '') { $r.'Key Account/Responsável'.Trim() } else { '[a preencher]' }

  $quemSolicitou = $r.'Quem solicitou?'.Trim()
  $origem = if ($quemSolicitou -ne '') { "Cliente:$ClientFolder - solicitado por: $quemSolicitou" } else { "Cliente:$ClientFolder" }

  $entregaPrevista = if ($r.'Data de Previsão de Entrega'.Trim() -ne '') { $r.'Data de Previsão de Entrega'.Trim() } else { '[a preencher]' }
  $conclusaoReal = if ($r.'Data de Conclusão'.Trim() -ne '') { $r.'Data de Conclusão'.Trim() } else { '[a preencher]' }

  $horas = if ($r.'Horas de Demanda'.Trim() -ne '') { $r.'Horas de Demanda'.Trim() } elseif ($r.'Horas - Recurso Específico'.Trim() -ne '') { $r.'Horas - Recurso Específico'.Trim() } else { '[a preencher]' }

  $titulo = Clean-Title $r.'Descrição da Solicitação' $r.ID

  $notasInternas = $r.'Observações'.Trim()
  if ($status -eq 'Concluído' -and $r.'Etapa'.Trim() -eq 'Em Validação - Cliente') {
    $conflictNote = "[Observação: dado legado com Status/Etapa conflitantes - Propriedade 'Concluída' mas Etapa 'Em Validação - Cliente'; mapeado como Concluído por prevalência da Propriedade]"
    $notasInternas = if ($notasInternas -ne '') { "$notasInternas`n$conflictNote" } else { $conflictNote }
  }

  $anexos = if ($r.'Arquivos e mídia'.Trim() -ne '') { $r.'Arquivos e mídia'.Trim() } else { '[a preencher]' }

  $ultimaEdicao = $r.'Última edição'.Trim()

  $lines = New-Object System.Collections.Generic.List[string]
  $lines.Add("# $titulo · Demanda")
  $lines.Add("")
  $lines.Add("## Identificação")
  $lines.Add("### ID")
  $lines.Add($id)
  $lines.Add("### ID legado (Notion/CX Hub)")
  $lines.Add($r.ID)
  $lines.Add("### Natureza")
  $lines.Add("casa-cliente")
  $lines.Add("### Origem (organizacional)")
  $lines.Add($origem)
  $lines.Add("### Destino (organizacional)")
  $lines.Add("[a preencher]")
  $lines.Add("### Data de abertura")
  $lines.Add($item.DateInfo.Display)
  $lines.Add("")
  $lines.Add("## Taxonomia CX Hub")
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
  $lines.Add("[a preencher]")
  $lines.Add("")
  $lines.Add("## Relacionamentos")
  $lines.Add("### Demanda mãe")
  $lines.Add("[a preencher]")
  $lines.Add("### Demandas filhas")
  $lines.Add("[a preencher]")
  $lines.Add("")
  $lines.Add("## Conteúdo")
  $lines.Add("### Descrição")
  foreach ($l in (Format-Body $r.'Descrição da Solicitação')) { $lines.Add($l) }
  $lines.Add("### Resultado esperado")
  $lines.Add("[a preencher]")
  $lines.Add("### Notas internas")
  foreach ($l in (Format-Body $notasInternas)) { $lines.Add($l) }
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
