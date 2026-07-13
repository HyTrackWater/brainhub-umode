# Gera RFI-AAAA-NNN.md para um cliente a partir do CSV consolidado de RFIs.
# Uso: .\gen-rfis.ps1 -ClientCsvName 'Cambos' -ClientFolder 'Cambos' -ClientDisplay 'Cambos'

param(
  [Parameter(Mandatory=$true)][string]$ClientCsvName,
  [Parameter(Mandatory=$true)][string]$ClientFolder,
  [Parameter(Mandatory=$true)][string]$ClientDisplay
)

$ErrorActionPreference = 'Stop'
$root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode"
$csvPath = Join-Path $root "RFIs Totais CSV e Markdown\RFI Escopo - Lista de Entregáveis 24fb1d38e768809db785c3bfcf5835e6_all.csv"
$mdFolder = Join-Path $root "RFIs Totais CSV e Markdown\RFI Escopo - Lista de Entregáveis"
$outDir = Join-Path $root "uMode\_Clientes\$ClientFolder\00_Institucional\_rfis"
New-Item -ItemType Directory -Path $outDir -Force | Out-Null

$mesesPt = @{
  'janeiro'=1;'fevereiro'=2;'março'=3;'abril'=4;'maio'=5;'junho'=6;'julho'=7;
  'agosto'=8;'setembro'=9;'outubro'=10;'novembro'=11;'dezembro'=12
}

function Parse-CriadoEm($ce) {
  if ($ce -and $ce -match '(\d{1,2}) de (\w+) de (\d{4})') {
    $day=[int]$Matches[1]; $mesNome=$Matches[2].ToLower(); $year=[int]$Matches[3]
    if ($mesesPt.ContainsKey($mesNome)) {
      return [datetime]::new($year,$mesesPt[$mesNome],$day)
    }
  }
  return $null
}

function Get-Grupo($status) {
  $s = $status.Trim()
  switch ($s) {
    'RFI em Rascunho' { return 'A fazer' }
    'RFI Stand By' { return 'A fazer' }
    'RFI Não Iniciada' { return 'A fazer' }
    'RFI Não iniciada' { return 'A fazer' }
    'RFI Pronta para Estimar' { return 'Em andamento' }
    'RFI Aceita — Criar Demanda e Estimar Entrega' { return 'Em andamento' }
    'RFI Liberada para Comercial negociar com Cliente' { return 'Em andamento' }
    'RFI Em Andamento' { return 'Em andamento' }
    'RFI Q&A Negócios' { return 'Em andamento' }
    'RFI Post Mortem' { return 'Em andamento' }
    'RFI Entregue ao Cliente' { return 'Concluídos' }
    'RFI Não Aceita' { return 'Concluídos' }
    'RFI Cancelada' { return 'Concluídos' }
    default { return $null }
  }
}

function Normalize-Status($status) {
  $s = $status.Trim()
  if ($s -eq 'RFI Não iniciada') { return 'RFI Não Iniciada' }
  return $s
}

# Mapa de arquivos .md de narrativa disponiveis (por titulo normalizado, sem sufixo notion-id,
# sem caracteres invalidos em nome de arquivo Windows - que o export do Notion ja removeu)
function Normalize-Titulo($s) {
  $t = $s -replace '[|:]', ''
  $t = $t -replace '\s+', ' '
  return $t.Trim().ToLower()
}

$mdFiles = Get-ChildItem -Path $mdFolder -Filter '*.md'
$mdLookup = @{}
foreach ($f in $mdFiles) {
  $t = $f.BaseName -replace '\s+[0-9a-f]{32}$', ''
  $mdLookup[(Normalize-Titulo $t)] = $f.FullName
}

function Find-Narrativa($nome) {
  $key = Normalize-Titulo $nome
  if ($mdLookup.ContainsKey($key)) { return Get-Content -Path $mdLookup[$key] -Raw -Encoding UTF8 }
  return $null
}

function Extract-Narrativa($mdContent) {
  if (-not $mdContent) { return $null }
  # pega tudo a partir da primeira linha "---" (fim do bloco de propriedades) ate o final
  $idx = $mdContent.IndexOf("`n---`n")
  if ($idx -lt 0) { return $null }
  $rest = $mdContent.Substring($idx + 6).Trim()
  if ($rest -eq '') { return $null }
  # headings markdown reais (#, ##...) dentro do texto livre colidiriam com a estrutura do
  # nosso proprio template - convertidos para negrito, preservando o conteudo sem virar heading
  $rest = ($rest -split "`n" | ForEach-Object {
    if ($_ -match '^#+\s+(.*)$') { "**$($Matches[1])**" } else { $_ }
  }) -join "`n"
  return $rest
}

$rows = Import-Csv $csvPath | Where-Object { $_.'👥 Clientes' -like "*$ClientCsvName*" -and $_.'👥 Clientes' -notlike "*,*" }
Write-Output "$ClientCsvName : $($rows.Count) RFIs encontradas"

$parsed = foreach ($r in $rows) {
  $d = Parse-CriadoEm $r.'Criado em'
  if (-not $d) { Write-Warning "SEM DATA: ID $($r.ID) - $($r.Nome)"; continue }
  [pscustomobject]@{ Row=$r; Date=$d }
}
$sorted = $parsed | Sort-Object { $_.Date }
$counters = @{}
$unmappedGrupo = New-Object System.Collections.Generic.List[string]
$generated = New-Object System.Collections.Generic.List[string]

foreach ($item in $sorted) {
  $r = $item.Row
  $year = $item.Date.Year
  if (-not $counters.ContainsKey($year)) { $counters[$year] = 0 }
  $counters[$year]++
  $id = "RFI-{0}-{1:D3}" -f $year, $counters[$year]

  $statusNorm = Normalize-Status $r.Status
  $grupo = Get-Grupo $statusNorm
  if (-not $grupo) { $unmappedGrupo.Add("$id : Status='$($r.Status)'"); $grupo = '[a preencher]' }

  $motivoCancel = if ($statusNorm -eq 'RFI Cancelada' -and $r.'Motivo do Cancelamento'.Trim() -ne '') { $r.'Motivo do Cancelamento'.Trim() } else { '[a preencher]' }

  $horasEst = if ($r.'Horas Estimadas'.Trim() -ne '') { $r.'Horas Estimadas'.Trim() } else { '[a preencher]' }
  $valorNegociado = if ($r.'Valor Negociado com Cliente'.Trim() -ne '') { $r.'Valor Negociado com Cliente'.Trim() } else { '[a preencher]' }

  $cobrada = switch ($r.Cobrado.Trim()) {
    'Sim' { 'sim' }
    'Não' { 'não' }
    default { '[a preencher]' }
  }

  $valorCalc = if ($r.'Valor Calculado'.Trim() -ne '') { $r.'Valor Calculado'.Trim() } else { '[a preencher]' }
  $dataPlanejada = if ($r.'Data Planejada de Execução'.Trim() -ne '') { $r.'Data Planejada de Execução'.Trim() } else { '[a preencher]' }
  $horasTrab = if ($r.'Horas Trabalhadas'.Trim() -ne '') { $r.'Horas Trabalhadas'.Trim() } else { '[a preencher]' }
  $dataLiberacao = if ($r.'Data Liberação RFI'.Trim() -ne '') { $r.'Data Liberação RFI'.Trim() } else { '[a preencher]' }
  $dataAceite = if ($r.'Data Aceite do Cliente'.Trim() -ne '') { $r.'Data Aceite do Cliente'.Trim() } else { '[a preencher]' }

  $pista = if ($r.'🤿 Demandas de Clientes'.Trim() -ne '') { $r.'🤿 Demandas de Clientes'.Trim() } else { '[a preencher]' }
  $demandaRel = "$($r.'Demanda relacionada'.Trim()) [dado bruto do Notion, nao confiavel como ID de demanda especifica - ver protocolo-gestao-rfi.md. Pista adicional (campo Demandas de Clientes): $pista]"

  $criadoPor = if ($r.'criado por'.Trim() -ne '') { $r.'criado por'.Trim() } else { '[a preencher]' }
  $responsaveis = if ($r.'Responsável pela RFI'.Trim() -ne '') { $r.'Responsável pela RFI'.Trim() } else { '[a preencher]' }
  $ka = if ($r.'Key Account'.Trim() -ne '') { $r.'Key Account'.Trim() } else { '[a preencher]' }

  $mdContent = Find-Narrativa $r.Nome
  $narrativa = Extract-Narrativa $mdContent
  $narrativaLines = if ($narrativa) { @($narrativa -split "`n" | ForEach-Object { $_.TrimEnd() }) } else { @('[a preencher]') }

  $lines = New-Object System.Collections.Generic.List[string]
  $lines.Add("# $($r.Nome.Trim()) · RFI")
  $lines.Add("")
  $lines.Add("## Identificação")
  $lines.Add("### ID")
  $lines.Add($id)
  $lines.Add("### ID legado (Notion/CX Hub)")
  $lines.Add("RFI-$($r.ID.Trim())")
  $lines.Add("### Cliente")
  $lines.Add($ClientDisplay)
  $lines.Add("### Demanda relacionada")
  $lines.Add($demandaRel)
  $lines.Add("### Criado por")
  $lines.Add($criadoPor)
  $lines.Add("### Data de criação")
  $lines.Add($r.'Criado em'.Trim())
  $lines.Add("")
  $lines.Add("## Conteúdo")
  $lines.Add("### Nome / Descrição")
  $lines.Add($r.Nome.Trim())
  $lines.Add("### Resumo do assunto")
  $lines.Add($(if ($r.'Resumo Assunto'.Trim() -ne '') { $r.'Resumo Assunto'.Trim() } else { '[a preencher]' }))
  $lines.Add("")
  $lines.Add("## Taxonomia")
  $lines.Add("### Grupo")
  $lines.Add($grupo)
  $lines.Add("### Status")
  $lines.Add($statusNorm)
  $lines.Add("### Motivo do cancelamento")
  $lines.Add($motivoCancel)
  $lines.Add("")
  $lines.Add("## Comercial")
  $lines.Add("### Horas estimadas")
  $lines.Add($horasEst)
  $lines.Add("### Valor negociado com o cliente")
  $lines.Add($valorNegociado)
  $lines.Add("### Cobrada?")
  $lines.Add($cobrada)
  $lines.Add("### Taxa aplicada (R`$/h)")
  $lines.Add("[a preencher]")
  $lines.Add("### Valor calculado")
  $lines.Add($valorCalc)
  $lines.Add("### Data planejada de execução")
  $lines.Add($dataPlanejada)
  $lines.Add("### Horas trabalhadas")
  $lines.Add($horasTrab)
  $lines.Add("")
  $lines.Add("## Datas")
  $lines.Add("### Data liberação RFI")
  $lines.Add($dataLiberacao)
  $lines.Add("### Data aceite do cliente")
  $lines.Add($dataAceite)
  $lines.Add("")
  $lines.Add("## Conteúdo / narrativa")
  foreach ($l in $narrativaLines) { $lines.Add($l) }
  $lines.Add("")
  $lines.Add("## Responsáveis")
  $lines.Add("### Responsável(is) interno(s)")
  $lines.Add($responsaveis)
  $lines.Add("### Key Account no momento da criação")
  $lines.Add($ka)
  $lines.Add("")
  $lines.Add("## Governança")
  $lines.Add("### Quem pode alterar este documento")
  $lines.Add("[a preencher]")

  $outPath = Join-Path $outDir "$id.md"
  [System.IO.File]::WriteAllLines($outPath, $lines, (New-Object System.Text.UTF8Encoding($false)))
  $generated.Add($id)
}

Write-Output "Gerados: $($generated.Count) arquivos"
if ($unmappedGrupo.Count -gt 0) {
  Write-Warning "STATUS NAO MAPEADOS ($($unmappedGrupo.Count)):"
  $unmappedGrupo | ForEach-Object { Write-Warning $_ }
}
