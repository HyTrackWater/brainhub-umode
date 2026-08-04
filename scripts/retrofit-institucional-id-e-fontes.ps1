# Retrofit dos 3 campos novos do template de institucional.md nos clientes escritos a mao
# (os 4 pilotos). Os 42 gerados ja saem prontos pelo gen-clientes-crm.ps1.
#
#   ## Identidade -> ### ID do cliente   (slug estavel; a chave logica deixa de ser o nome da pasta)
#   ## Identidade -> ### Aliases do cliente
#   ## Sistemas e fontes de verdade -> ### Outras fontes
#
# Resolve tambem a divergencia estrutural de Luiza Barcelos (pendencia aberta desde 09 jul 2026):
#   - '### ERP' (duplicava 'ERP / Integracao' de Operacao uMode) e removido; a restricao de escopo
#     que so existia nele e preservada como nota no campo canonico
#   - '### Notion (cadastro de cliente)' deixa de ser heading proprio e passa a ser item de
#     '### Outras fontes'
#
# Uso: .\retrofit-institucional-id-e-fontes.ps1 -CsvCrm '...' -Clientes 'Lofty Style','Cambos' ...

param(
  [Parameter(Mandatory=$true)][string]$CsvCrm,
  [Parameter(Mandatory=$true)][string[]]$Clientes,
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode",
  [string[]]$PastasDrive = @(),
  [string]$CsvRfis
)

$ErrorActionPreference = 'Stop'

function Clean-Value([string]$v) {
  if ($null -eq $v) { return '' }
  $v = $v -replace '\s*\(https?://www\.notion\.so/[^)]*\)', ''
  $v = $v -replace '\\([^a-zA-Z0-9\s])', '$1'
  return ($v -replace "`r", '').Trim()
}
function Has([string]$v) { return ($v -and $v.Trim() -ne '') }
function Flat([string]$v) { return ((Clean-Value $v) -replace "`n", ' · ') }
function Slugify($nome) {
  $s = $nome.Normalize([Text.NormalizationForm]::FormD)
  $sb = New-Object Text.StringBuilder
  foreach ($ch in $s.ToCharArray()) {
    if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($ch) -ne [Globalization.UnicodeCategory]::NonSpacingMark) { [void]$sb.Append($ch) }
  }
  return (($sb.ToString().ToLower() -replace '[^a-z0-9]+','-').Trim('-'))
}

$crm = Import-Csv $CsvCrm
$colNome = @($crm[0].PSObject.Properties.Name | Where-Object { $_ -like '*Nome Fantasia*' })[0]
$colCham = @($crm[0].PSObject.Properties.Name | Where-Object { $_ -like 'Chamado*Atendimento*' })[0]

$aliasRfi = @{}
if ($CsvRfis -and (Test-Path $CsvRfis)) {
  $rf = Import-Csv $CsvRfis
  $cCli = @($rf[0].PSObject.Properties.Name | Where-Object { $_ -like '*Clientes*' -and $_ -notlike '*Demandas*' })[0]
  $cNom = @($rf[0].PSObject.Properties.Name | Where-Object { $_ -eq 'Nome' })[0]
  foreach ($row in $rf) {
    $cls = @($row.$cCli -split '\),' | ForEach-Object { Clean-Value (($_ -split ' \(http')[0]) } | Where-Object { $_ -ne '' })
    $tit = Clean-Value $row.$cNom
    if ($tit -eq '' -or $cls.Count -ne 1) { continue }
    $pre = (($tit -split '\|')[0]).Trim()
    $pre = ($pre -replace '\s*RFI.*$','').Trim()
    if ($pre -eq '' -or $pre.Length -gt 30) { continue }
    $k = $cls[0]
    if (-not $aliasRfi.ContainsKey($k)) { $aliasRfi[$k] = New-Object System.Collections.Generic.List[string] }
    if (-not $aliasRfi[$k].Contains($pre)) { $aliasRfi[$k].Add($pre) }
  }
}

foreach ($nome in $Clientes) {
  $arq = Join-Path $Root "uMode\_Clientes\$nome\00_Institucional\_contexto\institucional.md"
  if (-not (Test-Path $arq)) { Write-Warning "nao achei: $nome"; continue }
  $r = $crm | Where-Object { (Clean-Value $_.$colNome) -eq $nome } | Select-Object -First 1
  $ls = New-Object System.Collections.Generic.List[string]
  Get-Content -Encoding UTF8 $arq | ForEach-Object { $ls.Add($_) }

  # ---------------------------------------- 1. Luiza Barcelos: '### ERP' -> nota em ERP / Integracao
  $iErp = $ls.IndexOf('### ERP')
  if ($iErp -ge 0) {
    $fim = $iErp + 1
    while ($fim -lt $ls.Count -and $ls[$fim] -notmatch '^#{1,6}\s') { $fim++ }
    $conteudo = @()
    for ($i = $iErp + 1; $i -lt $fim; $i++) { if ($ls[$i].Trim() -ne '') { $conteudo += $ls[$i].Trim() } }
    for ($i = $fim - 1; $i -ge $iErp; $i--) { $ls.RemoveAt($i) }
    $iCanon = $ls.IndexOf('### ERP / Integração')
    if ($iCanon -ge 0 -and $conteudo.Count -gt 0) {
      $ins = $iCanon + 1
      while ($ins -lt $ls.Count -and $ls[$ins] -notmatch '^#{1,6}\s') { $ins++ }
      $nota = @("> Escopo de integração (vinha de um heading ``### ERP`` extra em ""Sistemas e fontes de")
      $nota += "> verdade"", removido em 03 ago 2026 por duplicar este campo — o conteúdo abaixo é o que"
      $nota += "> só existia lá): " + ($conteudo -join ' ')
      for ($k = $nota.Count - 1; $k -ge 0; $k--) { $ls.Insert($ins, $nota[$k]) }
    }
    Write-Output "  [$nome] heading '### ERP' removido; restrição de escopo preservada em ERP / Integração"
  }

  # ---------------------------------------- 2. '### Notion (cadastro de cliente)' -> item de fonte
  $fontesExtra = @()
  $iNot = -1
  for ($i = 0; $i -lt $ls.Count; $i++) { if ($ls[$i] -like '### Notion*') { $iNot = $i; break } }
  if ($iNot -ge 0) {
    $rotulo = ($ls[$iNot] -replace '^###\s*','').Trim()
    $fim = $iNot + 1
    while ($fim -lt $ls.Count -and $ls[$fim] -notmatch '^#{1,6}\s') { $fim++ }
    for ($i = $iNot + 1; $i -lt $fim; $i++) { if ($ls[$i].Trim() -ne '') { $fontesExtra += "- $rotulo`: $($ls[$i].Trim())" } }
    for ($i = $fim - 1; $i -ge $iNot; $i--) { $ls.RemoveAt($i) }
    Write-Output "  [$nome] heading '### Notion (cadastro de cliente)' virou item de '### Outras fontes'"
  }

  # ---------------------------------------- 3. ### Outras fontes (depois de Drive de operacao)
  if ($ls.IndexOf('### Outras fontes') -lt 0) {
    $iDrive = $ls.IndexOf('### Drive de operação')
    if ($iDrive -ge 0) {
      $ins = $iDrive + 1
      while ($ins -lt $ls.Count -and $ls[$ins] -notmatch '^#{1,6}\s') { $ins++ }
      $bloco = New-Object System.Collections.Generic.List[string]
      $bloco.Add('### Outras fontes')
      foreach ($x in $fontesExtra) { $bloco.Add($x) }
      if ($r) {
        if (Has $r.'Portal do Cliente')      { $bloco.Add("- Portal do Cliente (CRM): $(Flat $r.'Portal do Cliente')") }
        if (Has $r.'Documentação Clientes')  { $bloco.Add("- Documentação Clientes (CRM): $(Flat $r.'Documentação Clientes')") }
        if (Has $r.'OKRs')                   { $bloco.Add("- OKRs (CRM): $(Flat $r.'OKRs')") }
        if (Has $r.'Material/Apresentação')  { $bloco.Add("- Material/Apresentação (CRM): $(Flat $r.'Material/Apresentação')") }
        if (Has $r.'Grupo do Whatsapp Oficial') { $bloco.Add("- Grupo de WhatsApp oficial (CRM): $(Flat $r.'Grupo do Whatsapp Oficial')") }
        if (Has $r.'3A - Controle de Troca de Emails') { $bloco.Add("- 3A · controle de troca de e-mails (CRM): $(Flat $r.'3A - Controle de Troca de Emails')") }
        if ($colCham -and (Has $r.$colCham)) { $bloco.Add("- Chamados/Atendimento vinculados no CRM: $(Flat $r.$colCham)") }
      }
      if ($bloco.Count -eq 1) { $bloco.Add('[a preencher]') }
      for ($k = $bloco.Count - 1; $k -ge 0; $k--) { $ls.Insert($ins, $bloco[$k]) }
    }
  }

  # ---------------------------------------- 4. ID do cliente + Aliases (inicio de ## Identidade)
  if ($ls.IndexOf('### ID do cliente') -lt 0) {
    $iId = $ls.IndexOf('## Identidade')
    if ($iId -ge 0) {
      $bloco = New-Object System.Collections.Generic.List[string]
      $bloco.Add('### ID do cliente')
      $bloco.Add((Slugify $nome))
      $bloco.Add('> Slug estável derivado do nome no CRM. **Não muda** se o nome comercial mudar — é a chave')
      $bloco.Add('> lógica deste cliente (o nome da pasta é só apresentação). Ver `_auditoria-indexacao.md`.')
      $bloco.Add('### Aliases do cliente')
      $bloco.Add("- $nome (CRM ""Mapa de Clientes"" — nome canônico)")
      foreach ($pd in $PastasDrive) {
        if ($pd -ne $nome -and $pd.ToLower() -eq $nome.ToLower()) { $bloco.Add("- $pd (pasta Drive ""Clientes"" — mesma grafia, caixa diferente)") }
      }
      if ($aliasRfi.ContainsKey($nome)) {
        foreach ($a in $aliasRfi[$nome]) { if ($a -ne $nome) { $bloco.Add("- $a (prefixo usado nos títulos de RFI no Notion)") } }
      }
      for ($k = $bloco.Count - 1; $k -ge 0; $k--) { $ls.Insert($iId + 1, $bloco[$k]) }
    }
  }

  [System.IO.File]::WriteAllLines($arq, $ls, (New-Object System.Text.UTF8Encoding($false)))
  Write-Output "[$nome] institucional.md atualizado (ID: $(Slugify $nome))"
}

