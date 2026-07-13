# Insere o campo "Status (interno)" em todas as demandas ja formalizadas (migracao historica).
# Todas as 236 tem "Vinculada ao CX Hub? = Sim" (confirmado por varredura antes de rodar este
# script), entao "Status (interno)" e sempre "Concluida" - a parte que cabia ao BrainHub (achar
# a demanda e faze-la virar card real no CX Hub) ja aconteceu. A execucao de fato continua
# rastreada pelo Status operacional do CX Hub, campo separado, ja existente no mesmo arquivo.

$ErrorActionPreference = 'Stop'
$root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode"
$files = Get-ChildItem -Path "$root\uMode\_Clientes" -Recurse -Filter "D-*.md" | Where-Object { $_.Name -notlike "_template*" }

$count = 0
$skipped = 0
foreach ($f in $files) {
  $lines = Get-Content -Path $f.FullName -Encoding UTF8

  $dataIdx = -1
  for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -eq '### Data de abertura') { $dataIdx = $i; break }
  }
  if ($dataIdx -lt 0) { Write-Warning "SEM '### Data de abertura': $($f.FullName)"; continue }

  $vincIdx = -1
  for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -eq '### Vinculada ao CX Hub?') { $vincIdx = $i; break }
  }
  if ($vincIdx -lt 0 -or ($lines[$vincIdx + 1] -notlike 'Sim*')) {
    Write-Warning "NAO vinculada ao CX Hub, pulando: $($f.FullName)"
    $skipped++
    continue
  }

  $emdash = [char]0x2014
  $statusInterno = "Concluída $emdash demanda já criada e vinculada ao CX Hub (ver Vinculada ao CX Hub?); execução acompanhada pelo Status do CX Hub abaixo"

  $newLines = New-Object System.Collections.Generic.List[string]
  for ($i = 0; $i -lt $lines.Count; $i++) {
    $newLines.Add($lines[$i])
    if ($i -eq $dataIdx + 1) {
      $newLines.Add('### Status (interno)')
      $newLines.Add($statusInterno)
    }
  }
  [System.IO.File]::WriteAllLines($f.FullName, $newLines, (New-Object System.Text.UTF8Encoding($false)))
  $count++
}
Write-Output "Retrofitados: $count arquivos (pulados: $skipped)"
