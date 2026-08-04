# Gera ficha de Pessoa (uMode/00_Institucional/_pessoas/) para as pessoas da Casa nomeadas no
# CRM "Mapa de Clientes" nos campos Key Account e Consultor de Negocios.
#
# Segue protocolo-gestao-pessoas.md: preenche SO campos documentaveis com fonte citada.
# Personificacao e Competencias ficam [a preencher] — nunca inferidas de documento.
#
# Uso: .\gen-pessoas-crm.ps1 -CsvCrm '...\crm-mapa-clientes.csv' [-ApenasRelatorio]

param(
  [Parameter(Mandatory=$true)][string]$CsvCrm,
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode",
  [switch]$ApenasRelatorio
)

$ErrorActionPreference = 'Stop'
$outDir = Join-Path $Root "uMode\00_Institucional\_pessoas"
$FONTE = 'CRM "Mapa de Clientes" (Drive `1_Bt8qKNeTVnlDAaeM1oOdoWgBmb6ek8k`, snapshot de 05 mar 2026) — varredura de 03 ago 2026, cobrindo os 46 clientes reais'

# pessoas que JA tem ficha: nao sobrescrever (foram escritas a mao, com nota de contexto proprio)
$jaTemFicha = @(
  'Laura Delgado Cardoso','Andrea Goulart Holmer dos Santos',
  'Marina Gonçalves Santoro','Vanessa Rinaldi Ornelas Engman'
)

$naoClientes = @('uMode', '. Página Cliente [Template]', 'Fornecedores')

function Desescapa($v) {
  if ($null -eq $v) { return '' }
  $bs = [string][char]92
  $pat = '[' + $bs + $bs + ']([^a-zA-Z0-9\s])'   # classe com a contrabarra, seguida do char escapado
  return ($v -replace $pat, '$1').Trim()
}

function Nomes($v) {
  if (-not $v) { return @() }
  $out = @()
  foreach ($part in ($v -split '\),')) {
    $n = ($part -split ' \(http')[0]
    $n = (Desescapa $n)
    if ($n -ne '') { $out += $n }
  }
  return $out
}

function Slug($nome) {
  $s = $nome.Normalize([Text.NormalizationForm]::FormD)
  $sb = New-Object Text.StringBuilder
  foreach ($ch in $s.ToCharArray()) {
    if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($ch) -ne [Globalization.UnicodeCategory]::NonSpacingMark) { [void]$sb.Append($ch) }
  }
  $r = $sb.ToString().ToLower()
  $r = $r -replace '[^a-z0-9]+', '-'
  return $r.Trim('-')
}

$crm = Import-Csv $CsvCrm
$colN  = ($crm[0].PSObject.Properties.Name | Where-Object { $_ -like '*Nome Fantasia*' })
$colKA = ($crm[0].PSObject.Properties.Name | Where-Object { $_ -like '*Key Account*' })
$colCN = ($crm[0].PSObject.Properties.Name | Where-Object { $_ -like '*Consultor de Neg*' })

# ---- inventario: pessoa -> clientes, por papel
$mapa = @{}
foreach ($r in $crm) {
  $cli = Desescapa $r.$colN
  if ($naoClientes -contains $cli) { continue }
  foreach ($p in (Nomes $r.$colKA)) {
    if (-not $mapa.ContainsKey($p)) { $mapa[$p] = [pscustomobject]@{ KA=@(); CN=@() } }
    $mapa[$p].KA += $cli
  }
  foreach ($p in (Nomes $r.$colCN)) {
    if (-not $mapa.ContainsKey($p)) { $mapa[$p] = [pscustomobject]@{ KA=@(); CN=@() } }
    $mapa[$p].CN += $cli
  }
}

Write-Output "===== INVENTARIO: pessoa da Casa -> clientes (fonte: CRM) ====="
foreach ($p in ($mapa.Keys | Sort-Object)) {
  $tem = if ($jaTemFicha -contains $p) { 'JA TEM FICHA' } else { 'ficha nova' }
  Write-Output ("--- {0}  [{1}]" -f $p, $tem)
  if ($mapa[$p].KA.Count -gt 0) { Write-Output ("    Key Account ({0}): {1}" -f $mapa[$p].KA.Count, (($mapa[$p].KA | Sort-Object) -join ' · ')) }
  if ($mapa[$p].CN.Count -gt 0) { Write-Output ("    Consultor(a) de Negocios ({0}): {1}" -f $mapa[$p].CN.Count, (($mapa[$p].CN | Sort-Object) -join ' · ')) }
}
if ($ApenasRelatorio) { return }

# ---- geracao das fichas novas
$gerados = 0
foreach ($nome in ($mapa.Keys | Sort-Object)) {
  if ($jaTemFicha -contains $nome) { continue }
  $info = $mapa[$nome]
  $arq = Join-Path $outDir ((Slug $nome) + '.md')

  $papeis = @()
  if ($info.KA.Count -gt 0) { $papeis += 'Key Account' }
  if ($info.CN.Count -gt 0) { $papeis += 'Consultor(a) de Negócios' }
  $cadeira = ($papeis -join ' · ') + " (papel conforme o campo em que a pessoa aparece no CRM ""Mapa de Clientes"" — não é a mesma coisa que Cadeira do organograma, ver protocolo-gestao-pessoas.md)"

  $atendidos = New-Object System.Collections.Generic.List[string]
  if ($info.KA.Count -gt 0) { $atendidos.Add("Como Key Account (" + $info.KA.Count + "): " + (($info.KA | Sort-Object) -join ' · ')) }
  if ($info.CN.Count -gt 0) { $atendidos.Add("Como Consultor(a) de Negócios (" + $info.CN.Count + "): " + (($info.CN | Sort-Object) -join ' · ')) }
  $atendidos.Add("> Lista extraída do CRM sobre os 46 clientes reais — inclui clientes em Churn/Inativo,")
  $atendidos.Add("> que são vínculo histórico e não atendimento ativo. A separação ativo × histórico exige")
  $atendidos.Add("> confirmação de quem atende hoje: não foi presumida a partir do Status do cliente.")

  $L = New-Object System.Collections.Generic.List[string]
  $L.Add("# $nome · Pessoa")
  $L.Add("")
  $L.Add("## Identificação")
  $L.Add("### Foto")
  $L.Add("[a preencher]")
  $L.Add("### Nome completo")
  $L.Add($nome)
  $L.Add("### Nome preferido / como é chamado(a)")
  $L.Add("[a preencher]")
  $L.Add("### Email")
  $L.Add("[a preencher]")
  $L.Add("### Cadeira / cargo atual")
  $L.Add($cadeira)
  $L.Add("### Nível HIC")
  $L.Add("[a preencher — critério de triagem/escala ainda não definido]")
  $L.Add("### Área (organizacional)")
  $L.Add("[a preencher — o CRM não traz Área organizacional, e o papel de atendimento não define")
  $L.Add("por si a Área das 8 travadas em CONTEXT.md; não presumido]")
  $L.Add("### Data de entrada na uMode")
  $L.Add("[a preencher]")
  $L.Add("### Status na uMode")
  $L.Add("[a preencher — aparecer no CRM não prova vínculo ativo hoje; o CRM é snapshot de mar 2026]")
  $L.Add("### Data de saída da uMode")
  $L.Add("[a preencher]")
  $L.Add("")
  $L.Add("## Papel")
  $L.Add("### Missão da cadeira")
  $L.Add("[a preencher]")
  $L.Add("### Responsabilidades principais")
  if ($info.KA.Count -gt 0 -and $info.CN.Count -gt 0) {
    $L.Add("Atendimento a clientes nos dois papéis registrados no CRM: Key Account e Consultor(a) de Negócios")
  } elseif ($info.KA.Count -gt 0) {
    $L.Add("Gestão de relacionamento com clientes como Key Account")
  } else {
    $L.Add("Atendimento a clientes como Consultor(a) de Negócios")
  }
  $L.Add("### Interfaces")
  $L.Add("[a preencher]")
  $L.Add("")
  $L.Add("## Histórico")
  $L.Add("### Áreas de atuação histórica")
  $L.Add("[a preencher]")
  $L.Add("### Clientes atuais atendidos")
  foreach ($a in $atendidos) { $L.Add($a) }
  $L.Add("### Clientes atendidos historicamente")
  $L.Add("[a preencher]")
  $L.Add("")
  $L.Add("## Personificação")
  $L.Add("[só a própria pessoa preenche, via formulário — nunca inferido de documento]")
  $L.Add("### Como se descreve")
  $L.Add("[a preencher]")
  $L.Add("### Personalidade / forma de trabalhar")
  $L.Add("[a preencher]")
  $L.Add("### O que a diferencia")
  $L.Add("[a preencher]")
  $L.Add("### Curiosidade / algo pessoal")
  $L.Add("[a preencher]")
  $L.Add("")
  $L.Add("## Competências")
  $L.Add("[preenchido só com fonte real citada — currículo/CV, LinkedIn, certificado, ou resposta da")
  $L.Add("própria pessoa via formulário. Nunca inferido do cargo/cadeira ou de como a pessoa aparece em")
  $L.Add("outro documento — ver protocolo-gestao-pessoas.md]")
  $L.Add("### Experiência profissional anterior")
  $L.Add("[a preencher]")
  $L.Add("### Skills / habilidades técnicas")
  $L.Add("[a preencher]")
  $L.Add("### Cursos e certificações")
  $L.Add("[a preencher]")
  $L.Add("### Ferramentas e plataformas que domina")
  $L.Add("[a preencher]")
  $L.Add("")
  $L.Add("## Governança")
  $L.Add("### Fonte dos dados documentáveis")
  $L.Add($FONTE)
  $L.Add("### Quem pode alterar este documento")
  $L.Add("[a preencher]")

  [System.IO.File]::WriteAllLines($arq, $L, (New-Object System.Text.UTF8Encoding($false)))
  $gerados++
  Write-Output "gerada: $((Slug $nome)).md"
}
Write-Output "Fichas novas geradas: $gerados"


