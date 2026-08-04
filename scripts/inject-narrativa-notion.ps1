# Injeta em cada D-AAAA-NNN.md a narrativa vinda do CORPO da pagina do Notion (base viva
# "Demandas de Clientes"), e marca como verificada-vazia a demanda cuja pagina nao tem corpo.
#
# Por que existe: o corpo da pagina nao vem em export de CSV nem em propriedade — a coluna `Texto`
# vem preenchida em 2 de 1.010 registros. So `fetch` por pagina traz. Como isso e 1 chamada por
# demanda, a extracao roda em lotes; este script e a parte que grava o lote.
#
# Formato do arquivo de lote (markdown simples):
#   @@UMD-177
#   <linhas da narrativa>
#   @@UMD-187
#   <linhas da narrativa>
#   @@VAZIO
#   UMD-133
#   UMD-50
#
# Uso: .\inject-narrativa-notion.ps1 -Lote '...\lote-01-narrativas.md'

param(
  [Parameter(Mandatory=$true)][string]$Lote,
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode",
  [string]$DataExtracao = "03 ago 2026"
)

$ErrorActionPreference = 'Stop'
$cli = Join-Path $Root "uMode\_Clientes"

# ---- le o lote
$narrativas = @{}
$vazias = New-Object System.Collections.Generic.List[string]
$atual = $null; $modoVazio = $false
foreach ($lin in (Get-Content -Encoding UTF8 $Lote)) {
  if ($lin -match '^@@VAZIO\s*$') { $modoVazio = $true; $atual = $null; continue }
  if ($lin -match '^@@(UMD-\S+)\s*$') { $atual = $Matches[1]; $modoVazio = $false; $narrativas[$atual] = New-Object System.Collections.Generic.List[string]; continue }
  if ($modoVazio) { if ($lin.Trim() -ne '') { $vazias.Add($lin.Trim()) }; continue }
  if ($atual) { $narrativas[$atual].Add($lin) }
}
Write-Output "lote: $($narrativas.Count) narrativas + $($vazias.Count) verificadas-vazias"

# ---- indexa os arquivos de demanda por ID legado
$porUmd = @{}
foreach ($f in (Get-ChildItem $cli -Recurse -Filter 'D-*.md' -File)) {
  $ls = @(Get-Content -Encoding UTF8 $f.FullName)
  $i = [array]::IndexOf($ls, '### ID legado (Notion/CX Hub)')
  if ($i -lt 0) { continue }
  $umd = $ls[$i+1].Trim()
  if ($umd -ne '' -and -not $porUmd.ContainsKey($umd)) { $porUmd[$umd] = $f.FullName }
}

function Injeta($umd, $blocos) {
  if (-not $porUmd.ContainsKey($umd)) { Write-Warning "sem arquivo para $umd"; return $false }
  $arq = $porUmd[$umd]
  $ls = New-Object System.Collections.Generic.List[string]
  Get-Content -Encoding UTF8 $arq | ForEach-Object { $ls.Add($_) }
  if (($ls -join "`n") -like '*corpo da página no Notion*') { Write-Output "  $umd ja tinha narrativa — nao tocado"; return $false }
  $i = $ls.IndexOf('### Descrição')
  if ($i -lt 0) { Write-Warning "sem heading Descricao em $umd"; return $false }
  # fim da secao = proximo heading
  $fim = $i + 1
  while ($fim -lt $ls.Count -and $ls[$fim] -notmatch '^#{1,6}\s') { $fim++ }
  for ($k = $blocos.Count - 1; $k -ge 0; $k--) { $ls.Insert($fim, $blocos[$k]) }
  [System.IO.File]::WriteAllLines($arq, $ls, (New-Object System.Text.UTF8Encoding($false)))
  return $true
}

$okNar = 0; $okVaz = 0
foreach ($umd in $narrativas.Keys) {
  $b = New-Object System.Collections.Generic.List[string]
  $b.Add("")
  $b.Add("> Narrativa vinda do **corpo da página no Notion** (base viva ``Demandas de Clientes``,")
  $b.Add("> ``ddf1951a-8dc2-42e6-98e6-bae3d1f5a865``), extraída em $DataExtracao. O texto acima é o")
  $b.Add("> título da demanda; o de baixo é o relato registrado na página — que nenhum export de CSV")
  $b.Add("> traz. Imagens ficaram como referência: os arquivos vivem fora do Notion (Discord/Gmail).")
  $b.Add("")
  foreach ($x in $narrativas[$umd]) { $b.Add($x) }
  if (Injeta $umd $b) { $okNar++ }
}
foreach ($umd in $vazias) {
  $b = New-Object System.Collections.Generic.List[string]
  $b.Add("")
  $b.Add("> ✔ Verificado em $DataExtracao na base viva do Notion: **a página desta demanda não tem")
  $b.Add("> corpo** — o título acima é todo o conteúdo registrado. Não é lacuna a preencher, e não")
  $b.Add("> precisa ser consultada de novo.")
  if (Injeta $umd $b) { $okVaz++ }
}
Write-Output "narrativas gravadas: $okNar | marcadas como verificadas-vazias: $okVaz"

