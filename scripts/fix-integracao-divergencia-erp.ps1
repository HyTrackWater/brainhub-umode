# Remove do integracao.md o aviso "Divergencia nao resolvida" de ERP quando o institucional.md
# JA concorda com o ERP indicado pelo repositorio.
#
# Por que existe: gen-integracoes.ps1 gravou o aviso lendo um institucional.md que ainda estava
# com '### ERP / Integracao' = [a preencher]. O campo foi preenchido depois (retrofit), entao o
# aviso ficou desatualizado — e "campo vazio" nunca foi divergencia, era ausencia de dado.
# Aviso desatualizado e pior que aviso nenhum: manda o leitor investigar um conflito que nao existe.
#
# Uso: .\fix-integracao-divergencia-erp.ps1

param([string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode")
$ErrorActionPreference = 'Stop'

# cliente -> ERP que o repositorio de integracao indica (mesma tabela de gen-integracoes.ps1)
$MAP = [ordered]@{
  'Reserva'         = 'SAP'
  'Oficina Reserva' = 'SAP'
  'NV'              = 'Linx'
  'Puket'           = 'Linx'
  'VIX'             = 'Linx'
  'Luiza Barcelos'  = 'Safe Tech'
  'Baw'             = 'Linx'
  'Cambos'          = 'SPI'
  'Lofty Style'     = 'Linx'
  'NK STORE'        = 'Linx'
  'Osklen'          = 'Linx'
}

function Valor($ls, $h) {
  $i = [array]::IndexOf($ls, $h)
  if ($i -lt 0) { return '' }
  $j = $i + 1
  while ($j -lt $ls.Count -and ($ls[$j].Trim() -eq '' -or $ls[$j].StartsWith('>'))) { $j++ }
  if ($j -lt $ls.Count -and $ls[$j] -notmatch '^#{1,6}\s') { return $ls[$j].Trim() }
  return ''
}

$limpos = 0; $mantidos = 0; $semAviso = 0
foreach ($c in $MAP.Keys) {
  $dir  = Join-Path $Root "uMode\_Clientes\$c\00_Institucional\_contexto"
  $fInt = Join-Path $dir 'integracao.md'
  $fIns = Join-Path $dir 'institucional.md'
  if (-not (Test-Path $fInt)) { Write-Warning "sem integracao.md: $c"; continue }

  $erpInst = ''
  if (Test-Path $fIns) { $erpInst = Valor @(Get-Content -Encoding UTF8 $fIns) '### ERP / Integração' }

  $ls = New-Object System.Collections.Generic.List[string]
  Get-Content -Encoding UTF8 $fInt | ForEach-Object { $ls.Add($_) }
  $ini = -1
  for ($k = 0; $k -lt $ls.Count; $k++) { if ($ls[$k] -like '*Divergência não resolvida*') { $ini = $k; break } }
  if ($ini -lt 0) { $semAviso++; Write-Output ("{0,-18} sem aviso" -f $c); continue }

  $concorda = ($erpInst -ne '' -and $erpInst -notlike '*a preencher*' -and $erpInst -like "*$($MAP[$c])*")
  if (-not $concorda) {
    $mantidos++
    Write-Output ("{0,-18} MANTIDO (institucional='{1}' / repo='{2}')" -f $c, $erpInst, $MAP[$c])
    continue
  }

  # remove o bloco de citacao inteiro (linhas '>' consecutivas a partir do inicio do aviso)
  $fim = $ini
  while ($fim -lt $ls.Count -and $ls[$fim].StartsWith('>')) { $fim++ }
  for ($k = $fim - 1; $k -ge $ini; $k--) { $ls.RemoveAt($k) }

  # o institucional confirma: registra a confirmacao no lugar, com a fonte
  $ls.Insert($ini, "> Confirmado contra o ``institucional.md`` deste cliente, que registra")
  $ls.Insert($ini + 1, "> ``ERP / Integração`` = ""$erpInst"".")

  [System.IO.File]::WriteAllLines($fInt, $ls, (New-Object System.Text.UTF8Encoding($false)))
  $limpos++
  Write-Output ("{0,-18} aviso removido, confirmacao gravada ('{1}')" -f $c, $erpInst)
}
Write-Output ""
Write-Output "avisos falsos removidos: $limpos | divergencias reais mantidas: $mantidos | sem aviso: $semAviso"
