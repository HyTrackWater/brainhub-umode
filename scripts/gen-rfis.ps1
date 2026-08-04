# Gera RFI-AAAA-NNN.md para um cliente a partir do CSV consolidado de RFIs (export do Notion).
#
# Uso: .\gen-rfis.ps1 -ClientCsvName 'Cambos' -ClientFolder 'Cambos' -CsvPath '...\rfis.csv'
#
# Historico de versoes:
# v1 (10 jul 2026) — gerou as 22 RFIs dos 4 clientes-piloto a partir do export de jul 2026
#    ("RFIs Totais CSV e Markdown", pasta ja removida do repositorio), que tinha CSV + markdown
#    por pagina (narrativa completa).
# v2 (03 ago 2026) — replicacao total, a partir do snapshot de mar 2026 no Drive, que tem
#    SO o CSV (sem narrativa). Mudancas registradas em protocolo-gestao-rfi.md ANTES de rodar:
#      - CSV virou parametro (-CsvPath); pasta de markdown deixou de existir
#      - traducao de 2 valores de Status legado ('RFI Aceita - Criar no Linear e Estimar
#        Entrega' e 'RFI Nao iniciada') para o enum do protocolo
#      - colunas que este export nao tem ('Criado por', formula de Valor calculado) e a
#        narrativa de pagina ficam [a preencher] com o motivo explicito, nunca herdadas

param(
  [Parameter(Mandatory=$true)][string]$ClientCsvName,
  [Parameter(Mandatory=$true)][string]$ClientFolder,
  [Parameter(Mandatory=$true)][string]$CsvPath,
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode",
  # pasta com um .md por RFI (export em markdown do Notion) — casado por ID, preenche a narrativa
  [string]$NarrativaDir,
  [string]$FonteNota = 'export "RFIs Totais CSV e Markdown" (jul 2026, recuperado do histórico do Git — commit 8c6705b^)'
)

$ErrorActionPreference = 'Stop'
$outDir = Join-Path $Root "uMode\_Clientes\$ClientFolder\00_Institucional\_rfis"
New-Item -ItemType Directory -Path $outDir -Force | Out-Null

$mesesEn = @{
  'january'=1;'february'=2;'march'=3;'april'=4;'may'=5;'june'=6;'july'=7;
  'august'=8;'september'=9;'october'=10;'november'=11;'december'=12
}
$mesesPt = @{
  'janeiro'=1;'fevereiro'=2;'março'=3;'abril'=4;'maio'=5;'junho'=6;'julho'=7;
  'agosto'=8;'setembro'=9;'outubro'=10;'novembro'=11;'dezembro'=12
}

function Norm-Nome($v) { if ($null -eq $v) { return '' } return (($v -replace '\s*\(https?://[^)]*\)','') -replace '\\([^a-zA-Z0-9\s])','$1').Trim() }
function Clean($v) { return (Norm-Nome $v) }
function OrPh($v) { $c = Clean $v; if ($c -eq '') { return '[a preencher]' } return $c }

function Parse-CriadoEm($ce) {
  if ($ce -match '(\d{1,2}) de (\w+) de (\d{4})') {
    $mes = $Matches[2].ToLower()
    if ($mesesPt.ContainsKey($mes)) { return [datetime]::new([int]$Matches[3], $mesesPt[$mes], [int]$Matches[1]) }
  }
  if ($ce -match '(\w+)\s+(\d{1,2}),\s*(\d{4})') {
    $mes = $Matches[1].ToLower()
    if ($mesesEn.ContainsKey($mes)) { return [datetime]::new([int]$Matches[3], $mesesEn[$mes], [int]$Matches[2]) }
  }
  return $null
}

# traducao registrada em protocolo-gestao-rfi.md (03 ago 2026)
function Get-StatusRfi($s) {
  $v = (Clean $s)
  switch ($v) {
    'RFI Aceita - Criar no Linear e Estimar Entrega' { return 'RFI Aceita — Criar Demanda e Estimar Entrega' }
    'RFI Não iniciada' { return 'RFI Não Iniciada' }
    '' { return '[a preencher]' }
    default { return $v }
  }
}

function Get-Grupo($status) {
  switch ($status) {
    'RFI em Rascunho' { return 'A fazer' }
    'RFI Stand By' { return 'A fazer' }
    'RFI Não Iniciada' { return 'A fazer' }
    'RFI Pronta para Estimar' { return 'Em andamento' }
    'RFI Aceita — Criar Demanda e Estimar Entrega' { return 'Em andamento' }
    'RFI Liberada para Comercial negociar com Cliente' { return 'Em andamento' }
    'RFI Em Andamento' { return 'Em andamento' }
    'RFI Q&A Negócios' { return 'Em andamento' }
    'RFI Post Mortem' { return 'Em andamento' }
    'RFI Entregue ao Cliente' { return 'Concluídos' }
    'RFI Não Aceita' { return 'Concluídos' }
    'RFI Cancelada' { return 'Concluídos' }
    default { return '[a preencher]' }
  }
}

$all = Import-Csv $CsvPath
$cols = $all[0].PSObject.Properties.Name
$colCli  = @($cols | Where-Object { $_ -like '*Clientes*' -and $_ -notlike '*Demandas*' })[0]
$colDem  = @($cols | Where-Object { $_ -like '*Demandas de Clientes*' })[0]
$colNome = @($cols | Where-Object { $_ -eq 'Nome' })[0]
if (-not $colNome) { $colNome = @($cols | Where-Object { $_ -like '*Nome*' })[0] }
if (-not $colCli) { throw "Coluna de cliente nao encontrada no CSV de RFIs" }
# schema varia entre exports: mar/2026 usa 'Horas Totais'/'Valor'; jul/2026 usa
# 'Horas Estimadas'/'Valor Negociado com Cliente' e ainda traz 'Valor Calculado',
# 'Key Account' e 'criado por' (que o export menor nao tem)
$colHoras = @($cols | Where-Object { $_ -eq 'Horas Estimadas' -or $_ -eq 'Horas Totais' })[0]
$colValor = @($cols | Where-Object { $_ -eq 'Valor Negociado com Cliente' -or $_ -eq 'Valor' })[0]
$colValorCalc = @($cols | Where-Object { $_ -eq 'Valor Calculado' })[0]
$colKA    = @($cols | Where-Object { $_ -eq 'Key Account' })[0]
$colCriadoPor = @($cols | Where-Object { $_ -eq 'criado por' -or $_ -eq 'Criado por' })[0]

# ---------------- narrativa: markdown por pagina, casado por ID
$props = @('Nome','ID','Status','Resumo Assunto','Responsável pela RFI','Criado em','criado por',
  'Key Account','Horas Estimadas','Horas Totais','Horas Trabalhadas','Valor Calculado',
  'Valor Negociado com Cliente','Valor','Cobrado','Cobrada?','Data Liberação RFI',
  'Data Aceite do Cliente','Data Planejada de Execução','Demanda relacionada',
  'Motivo do Cancelamento','Task (Linear)','Task','Selecionar','Clientes','Demandas de Clientes')
$narrativas = @{}
if ($NarrativaDir -and (Test-Path $NarrativaDir)) {
  foreach ($m in (Get-ChildItem $NarrativaDir -Filter *.md -File)) {
    $linhas = @(Get-Content -Encoding UTF8 $m.FullName)
    $idNum = $null
    $fimProps = 0
    for ($i = 0; $i -lt [Math]::Min($linhas.Count, 30); $i++) {
      $lin = $linhas[$i]
      if ($lin -match '^ID:\s*(\d+)\s*$') { $idNum = [int]$Matches[1] }
      $nome = if ($lin -match '^([^:]{1,45}):\s') { $Matches[1].Trim() } else { $null }
      if ($nome) {
        $limpo = ($nome -replace '[^\p{L}\p{N} \-\(\)\?]', '').Trim()
        if ($props -contains $limpo) { $fimProps = $i }
      }
    }
    if ($null -eq $idNum) { continue }
    $corpo = @()
    if ($fimProps -gt 0 -and $fimProps + 1 -lt $linhas.Count) {
      $corpo = @($linhas[($fimProps + 1)..($linhas.Count - 1)])
    }
    # heading markdown da fonte colidiria com os headings do nosso template -> negrito
    # @(...) obrigatorio: pipeline que devolve 1 item viraria string escalar, nao array
    $corpo = @($corpo | ForEach-Object { if ($_ -match '^\s*#{1,6}\s+(.*)$') { '**' + $Matches[1].Trim() + '**' } else { $_ } })
    while ($corpo.Count -gt 0 -and $corpo[0].Trim() -eq '') { $corpo = @($corpo[1..($corpo.Count-1)]) }
    while ($corpo.Count -gt 0 -and $corpo[-1].Trim() -eq '') { $corpo = @($corpo[0..($corpo.Count-2)]) }
    if ($corpo.Count -gt 0) { $narrativas[$idNum] = @{ Linhas = $corpo; Arquivo = $m.Name } }
  }
  Write-Output "narrativas carregadas: $($narrativas.Count)"
}

# uma celula pode listar mais de um cliente. Regra travada em protocolo-gestao-rfi.md
# ("Multi-cliente"): RFI e sempre de 1 cliente -> a linha legada vira N RFIs, uma por cliente.
function Clientes-Da-Linha($v) {
  if (-not $v) { return @() }
  return @($v -split '\),' | ForEach-Object { Norm-Nome (($_ -split ' \(http')[0]) } | Where-Object { $_ -ne '' })
}
$alvo = Norm-Nome $ClientCsvName
$rows = @($all | Where-Object { (Clientes-Da-Linha $_.$colCli) -contains $alvo })
Write-Output "$ClientCsvName : $($rows.Count) RFIs encontradas"
if ($rows.Count -eq 0) { return }

$parsed = foreach ($r in $rows) {
  $dt = Parse-CriadoEm (Clean $r.'Criado em')
  if (-not $dt) { Write-Warning "SEM DATA DE CRIACAO: ID $($r.ID)"; continue }
  [pscustomobject]@{ Row=$r; Date=$dt }
}
$sorted = $parsed | Sort-Object Date
$counters = @{}
$gerados = 0
$comNarrativa = 0

foreach ($item in $sorted) {
  $r = $item.Row
  $year = $item.Date.Year
  if (-not $counters.ContainsKey($year)) { $counters[$year] = 0 }
  $counters[$year]++
  $id = "RFI-{0}-{1:D3}" -f $year, $counters[$year]

  $status = Get-StatusRfi $r.Status
  $grupo = Get-Grupo $status
  $idLegado = if ((Clean $r.ID) -ne '') { "RFI-$(Clean $r.ID)" } else { '[a preencher]' }
  $nome = OrPh $r.$colNome

  # Demanda relacionada: divida conhecida do Notion legado (ver protocolo-gestao-rfi.md)
  $demRel = Clean $r.'Demanda relacionada'
  $pista = if ($colDem) { Clean $r.$colDem } else { '' }
  if ($demRel -eq '' -and $pista -ne '') { $demRel = $pista }
  if ($demRel -eq '') {
    $demandaRel = "[a preencher — este export não trouxe vínculo de demanda para esta RFI; a reconciliação é manual, RFI a RFI, conforme protocolo-gestao-rfi.md]"
  } else {
    $pistaTxt = if ($pista -ne '') { $pista } else { '[a preencher]' }
    $demandaRel = "$demRel [dado bruto do Notion, não confiável como ID de demanda específica — ver protocolo-gestao-rfi.md. Pista adicional (campo Demandas de Clientes): $pistaTxt]"
  }

  $motivoFonte = Clean $r.'Motivo do Cancelamento'
  if ($status -eq 'RFI Cancelada') {
    $motivo = if ($motivoFonte -ne '') { $motivoFonte } else { '[a preencher]' }
  } elseif ($motivoFonte -ne '') {
    $motivo = "$motivoFonte [observação: a fonte traz motivo de cancelamento apesar de Status = $status — dado legado preservado, não resolvido por conta própria]"
  } else {
    $motivo = '[a preencher]'
  }

  $L = New-Object System.Collections.Generic.List[string]
  $L.Add("# $nome · RFI")
  $L.Add("")
  $L.Add("## Identificação")
  $L.Add("### ID")
  $L.Add($id)
  $L.Add("### ID legado (Notion/CX Hub)")
  $L.Add($idLegado)
  $L.Add("### Cliente")
  $L.Add($ClientFolder)
  $outros = @((Clientes-Da-Linha $r.$colCli) | Where-Object { $_ -ne $alvo })
  if ($outros.Count -gt 0) {
    $L.Add("> ⚠ A linha legada do Notion (ID $(Clean $r.ID)) listava mais de um cliente:")
    $L.Add("> **$ClientFolder** + $($outros -join ' + '). Pela regra travada em")
    $L.Add("> ``protocolo-gestao-rfi.md`` (""RFI é sempre de 1 cliente só""), a linha foi desdobrada em")
    $L.Add("> uma RFI por cliente — esta é a de $ClientFolder, com o mesmo ``ID legado``. Não é")
    $L.Add("> duplicidade: é a mesma negociação de origem, registrada em cada casa envolvida.")
  }
  $L.Add("### Demanda relacionada")
  $L.Add($demandaRel)
  $L.Add("### Criado por")
  if ($colCriadoPor) { $L.Add((OrPh $r.$colCriadoPor)) } else { $L.Add("[a preencher — este export do Notion não traz a coluna ""Criado por""]") }
  $L.Add("### Data de criação")
  $L.Add((OrPh $r.'Criado em'))
  $L.Add("")
  $L.Add("## Conteúdo")
  $L.Add("### Nome / Descrição")
  $L.Add($nome)
  $L.Add("### Resumo do assunto")
  $L.Add((OrPh $r.'Resumo Assunto'))
  $L.Add("")
  $L.Add("## Taxonomia")
  $L.Add("### Grupo")
  $L.Add($grupo)
  $L.Add("### Status")
  $L.Add($status)
  $L.Add("### Motivo do cancelamento")
  $L.Add($motivo)
  $L.Add("")
  $L.Add("## Comercial")
  $L.Add("### Horas estimadas")
  $L.Add((OrPh $r.$colHoras))
  $L.Add("### Valor negociado com o cliente")
  $L.Add((OrPh $r.$colValor))
  $L.Add("### Cobrada?")
  $L.Add((OrPh $r.'Cobrado'))
  $L.Add("### Taxa aplicada (R`$/h)")
  $L.Add("[a preencher — a fonte não declara a taxa; não foi derivada de Valor calculado ÷ Horas estimadas para não afirmar uma taxa que a fonte não diz]")
  $L.Add("### Valor calculado")
  if ($colValorCalc) { $L.Add((OrPh $r.$colValorCalc)) } else { $L.Add("[a preencher — este export não traz a coluna calculada do Notion]") }
  $L.Add("### Data planejada de execução")
  $L.Add((OrPh $r.'Data Planejada de Execução'))
  $L.Add("### Horas trabalhadas")
  $L.Add((OrPh $r.'Horas Trabalhadas'))
  $L.Add("")
  $L.Add("## Datas")
  $L.Add("### Data liberação RFI")
  $L.Add((OrPh $r.'Data Liberação RFI'))
  $L.Add("### Data aceite do cliente")
  $L.Add((OrPh $r.'Data Aceite do Cliente'))
  $L.Add("")
  $L.Add("## Conteúdo / narrativa")
  $idNum = if ((Clean $r.ID) -match '^\d+$') { [int](Clean $r.ID) } else { -1 }
  if ($narrativas.ContainsKey($idNum)) {
    # ATENCAO: variavel de loop NAO pode ser $l — PowerShell nao diferencia maiuscula de
    # minuscula, e $l sobrescreveria a lista de saida $L (bug real, corrigido em 03 ago 2026)
    foreach ($ln in $narrativas[$idNum].Linhas) { $L.Add($ln) }
    $L.Add("")
    $L.Add("> Narrativa vinda do $FonteNota — arquivo ``$($narrativas[$idNum].Arquivo)``, casado por")
    $L.Add("> ``ID`` da base. Headings markdown da fonte foram convertidos em negrito para não colidir")
    $L.Add("> com os headings deste template; o resto do conteúdo (tabelas, blocos ""De Acordo"") está")
    $L.Add("> como na origem.")
    $comNarrativa++
  } else {
    $L.Add("[a preencher — nenhum markdown de página encontrado para o ID $(Clean $r.ID) neste export]")
  }
  $L.Add("")
  $L.Add("## Responsáveis")
  $L.Add("### Responsável(is) interno(s)")
  $L.Add((OrPh $r.'Responsável pela RFI'))
  $L.Add("### Key Account no momento da criação")
  if ($colKA) { $L.Add((OrPh $r.$colKA)) } else { $L.Add("[a preencher]") }
  $L.Add("")
  $L.Add("## Governança")
  $L.Add("### Quem pode alterar este documento")
  $L.Add("[a preencher]")

  [System.IO.File]::WriteAllLines((Join-Path $outDir "$id.md"), $L, (New-Object System.Text.UTF8Encoding($false)))
  $gerados++
}

Write-Output "Gerados: $gerados arquivos ($comNarrativa com narrativa de página)"




