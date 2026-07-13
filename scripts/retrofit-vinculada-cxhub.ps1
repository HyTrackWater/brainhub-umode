# Insere o campo "Vinculada ao CX Hub?" em todas as demandas ja formalizadas (migracao
# historica) com valor "Sim - ID: {ID legado}", pois todas nasceram como card real no CX Hub/
# Notion antes de serem formalizadas no BrainHub.

$ErrorActionPreference = 'Stop'
$root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode"
$files = Get-ChildItem -Path "$root\uMode\_Clientes" -Recurse -Filter "D-*.md" | Where-Object { $_.Name -notlike "_template*" }

$count = 0
foreach ($f in $files) {
  $lines = Get-Content -Path $f.FullName -Encoding UTF8
  $legadoIdx = ($lines | Select-String -Pattern '^### ID legado' -SimpleMatch:$false).LineNumber
  if (-not $legadoIdx) { Write-Warning "SEM 'ID legado': $($f.FullName)"; continue }
  $legadoValor = $lines[$legadoIdx].Trim()

  $taxIdx = -1
  for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -eq '## Taxonomia CX Hub') { $taxIdx = $i; break }
  }
  if ($taxIdx -lt 0) { Write-Warning "SEM '## Taxonomia CX Hub': $($f.FullName)"; continue }

  $emdash = [char]0x2014
  $vinculada = if ($legadoValor -and $legadoValor -ne '[a preencher]') { "Sim $emdash ID: $legadoValor" } else { '[a preencher]' }

  $newLines = New-Object System.Collections.Generic.List[string]
  for ($i = 0; $i -lt $lines.Count; $i++) {
    $newLines.Add($lines[$i])
    if ($i -eq $taxIdx) {
      $newLines.Add('### Vinculada ao CX Hub?')
      $newLines.Add($vinculada)
    }
  }
  [System.IO.File]::WriteAllLines($f.FullName, $newLines, (New-Object System.Text.UTF8Encoding($false)))
  $count++
}
Write-Output "Retrofitados: $count arquivos"
