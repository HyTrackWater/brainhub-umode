# Generaliza o campo "Vinculada ao CX Hub?" para "Vinculada?" + "Vinculo" (lista) em todas as
# demandas ja formalizadas. Decisao do Vinicius (14 jul 2026): o destino de uma demanda aprovada
# nem sempre e o CX Hub (ex.: Vendas pode ter destino proprio no futuro) - o campo precisa
# comportar mais de um sistema de destino, nao so Sim/Nao + ID do CX Hub.
# Formato antigo:
#   ### Vinculada ao CX Hub?
#   Sim - ID: UMD-317
# Formato novo:
#   ### Vinculada?
#   Sim
#   ### Vinculo
#   CX Hub - ID: UMD-317
# Tambem corrige o texto de "Status (interno)" que cita o nome antigo do campo.

$ErrorActionPreference = 'Stop'
$root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode"
$files = Get-ChildItem -Path "$root\uMode\_Clientes" -Recurse -Filter "D-*.md" | Where-Object { $_.Name -notlike "_template*" }

$emdash = [char]0x2014
$count = 0
$skipped = 0
foreach ($f in $files) {
  $lines = Get-Content -Path $f.FullName -Encoding UTF8

  $idx = -1
  for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -eq '### Vinculada ao CX Hub?') { $idx = $i; break }
  }
  if ($idx -lt 0) { Write-Warning "SEM '### Vinculada ao CX Hub?': $($f.FullName)"; continue }

  $valorAntigo = $lines[$idx + 1].Trim()

  if ($valorAntigo -like 'Sim*') {
    # extrai o ID depois de "ID:"
    if ($valorAntigo -match 'ID:\s*(.+)$') {
      $id = $matches[1].Trim()
    } else {
      $id = ''
      Write-Warning "Sim sem ID reconhecido em: $($f.FullName) -> '$valorAntigo'"
    }
    $novaLinha1 = '### Vinculada?'
    $novaLinha2 = 'Sim'
    $novaLinha3 = '### Vínculo'
    $novaLinha4 = "CX Hub $emdash ID: $id"
  } elseif ($valorAntigo -eq '[a preencher]') {
    $novaLinha1 = '### Vinculada?'
    $novaLinha2 = '[a preencher]'
    $novaLinha3 = '### Vínculo'
    $novaLinha4 = '[a preencher]'
  } else {
    Write-Warning "Valor inesperado em: $($f.FullName) -> '$valorAntigo'"
    $skipped++
    continue
  }

  $newLines = New-Object System.Collections.Generic.List[string]
  for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($i -eq $idx) {
      $newLines.Add($novaLinha1)
      $newLines.Add($novaLinha2)
      $newLines.Add($novaLinha3)
      $newLines.Add($novaLinha4)
      $i++  # pula a linha de valor antiga (idx+1), ja consumida
      continue
    }
    $newLines.Add($lines[$i])
  }

  # corrige texto de Status (interno) que cita o nome antigo do campo
  for ($i = 0; $i -lt $newLines.Count; $i++) {
    if ($newLines[$i] -like '*ver Vinculada ao CX Hub?*') {
      $newLines[$i] = $newLines[$i] -replace 'ver Vinculada ao CX Hub\?', 'ver Vinculada?'
    }
  }

  [System.IO.File]::WriteAllLines($f.FullName, $newLines, (New-Object System.Text.UTF8Encoding($false)))
  $count++
}
Write-Output "Retrofitados: $count arquivos (pulados: $skipped)"
