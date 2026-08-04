# Injeta nos produto.md do Portfolio o conteudo extraido de fonte real (Notion, briefing do CEO/
# Vinicius, planilha de acessos). Segue protocolo-gestao-produto.md.
#
# Formato do arquivo de lote:
#   @@PRODUTO: DesenvolvAI
#   @@Descricao
#   <linhas>
#   @@Marco
#   DATA | EVENTO | RESPONSAVEL | NOTA
#   @@Fonte
#   - linha que sera ACRESCENTADA em 'Documentos tecnicos consultados'
#   @@PRODUTO: outro
#
# Dois modos por campo, definidos em $MAPA:
#   'sub' = substitui o conteudo da secao   |   'add' = acrescenta ao fim da secao
# 'Fonte' e sempre 'add' (nunca apaga a procedencia que ja estava registrada) e 'Marco' vira linha
# de tabela. Ordem de injecao importa: o lote mais autoritativo deve ser injetado POR ULTIMO.
#
# Uso: .\inject-produto.ps1 -Lote '...\lote-produto-X.md'

param(
  [Parameter(Mandatory=$true)][string]$Lote,
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode",
  [string]$Hoje = "04 ago 2026"
)
$ErrorActionPreference = 'Stop'

$PASTA = [ordered]@{
  'PlanejAI'='01_PlanejAI'; 'CriAI'='02_CriAI'; 'DesenvolvAI'='03_DesenvolvAI'
  'FornecAI'='04_FornecAI'; 'EnriqueceAI'='05_EnriqueceAI'; 'GerenciAI'='06_GerenciAI'
  'AlocAI'='07_AlocAI'; 'VendeAI'='08_VendeAI'; 'CliprocAI'='09_CliprocAI'
  'CadastrAI'='10_CadastrAI'; 'Taxonomia'='11_Taxonomia'; 'CX Hub'='12_CX-Hub'
  'ONB HUB'='13_ONB-HUB'; 'IntHub'='14_IntHub'; 'Gest Hub'='15_Gest-Hub'; 'Sales Hub'='16_Sales-Hub'
}

$MAPA = [ordered]@{
  'Nome legado'                      = @('### Nome legado', 'sub')
  'Descrição'                        = @('### Descrição', 'sub')
  'Score de maturidade'              = @('### Score de maturidade', 'sub')
  'Fonte e data da avaliação'        = @('### Fonte e data da avaliação', 'sub')
  'Consome de (upstream)'            = @('### Consome de (upstream)', 'sub')
  'Produz para (downstream)'         = @('### Produz para (downstream)', 'sub')
  'Módulos relacionados'             = @('### Módulos relacionados', 'sub')
  'Clientes que contrataram'         = @('### Clientes que contrataram', 'sub')
  'Owner / Estratégia'               = @('### Owner / Estratégia', 'sub')
  'Operador'                         = @('### Operador', 'sub')
  'Quem pode alterar este documento' = @('### Quem pode alterar este documento', 'sub')
  'Fonte'                            = @('### Documentos técnicos consultados', 'add')
}

# ---------------- le o lote
$blocos = New-Object System.Collections.Generic.List[object]
$prod = $null; $campo = $null; $dados = $null
foreach ($lin in (Get-Content -Encoding UTF8 $Lote)) {
  if ($lin -match '^@@PRODUTO:\s*(.+?)\s*$') {
    if ($prod) { $blocos.Add([pscustomobject]@{ Produto = $prod; Campos = $dados }) }
    $prod = $Matches[1]; $dados = [ordered]@{}; $campo = $null
    continue
  }
  if ($lin -match '^@@(.+?)\s*$') {
    $campo = $Matches[1]
    if (-not $dados.Contains($campo)) { $dados[$campo] = New-Object System.Collections.Generic.List[string] }
    continue
  }
  if ($campo) { $dados[$campo].Add($lin) }
}
if ($prod) { $blocos.Add([pscustomobject]@{ Produto = $prod; Campos = $dados }) }
Write-Output "lote: $($blocos.Count) produto(s)"

function Set-Campo($ls, $h, $modo, $conteudo) {
  $i = [array]::IndexOf($ls, $h)
  if ($i -lt 0) { return $false }
  $fim = $i + 1
  while ($fim -lt $ls.Count -and $ls[$fim] -notmatch '^#{1,6}\s') { $fim++ }

  $novo = @($conteudo | Where-Object { $_ -ne $null })
  while ($novo.Count -gt 0 -and $novo[0].Trim() -eq '') { $novo = @($novo[1..($novo.Count-1)]) }
  while ($novo.Count -gt 0 -and $novo[-1].Trim() -eq '') { $novo = @($novo[0..($novo.Count-2)]) }
  if ($novo.Count -eq 0) { return $false }

  if ($modo -eq 'sub') {
    for ($k = $fim - 1; $k -gt $i; $k--) { $ls.RemoveAt($k) }
    for ($k = $novo.Count - 1; $k -ge 0; $k--) { $ls.Insert($i + 1, $novo[$k]) }
  } else {
    # 'add': acrescenta antes do proximo heading, sem apagar o que ja existe
    $ins = $fim
    while ($ins - 1 -gt $i -and $ls[$ins - 1].Trim() -eq '') { $ins-- }
    for ($k = $novo.Count - 1; $k -ge 0; $k--) { $ls.Insert($ins, $novo[$k]) }
  }
  return $true
}

$totCampos = 0; $totArquivos = 0
foreach ($b in $blocos) {
  if (-not $PASTA.Contains($b.Produto)) { Write-Warning "produto fora do Portfolio travado: '$($b.Produto)' — ignorado"; continue }
  $arq = Join-Path $Root "uMode\03_Produto-e-Solucoes\$($PASTA[$b.Produto])\_contexto\produto.md"
  if (-not (Test-Path $arq)) { Write-Warning "sem produto.md: $($b.Produto)"; continue }

  $ls = New-Object System.Collections.Generic.List[string]
  Get-Content -Encoding UTF8 $arq | ForEach-Object { $ls.Add($_) }
  $n = 0
  foreach ($campoNome in $b.Campos.Keys) {
    if ($campoNome -eq 'Marco') { continue }   # tratado abaixo, e tabela
    if (-not $MAPA.Contains($campoNome)) { Write-Warning "$($b.Produto): campo desconhecido '$campoNome'"; continue }
    $m = $MAPA[$campoNome]
    if (Set-Campo $ls $m[0] $m[1] $b.Campos[$campoNome]) { $n++ }
    else { Write-Warning "$($b.Produto): nao localizou '$($m[0])'" }
  }
  # --- marcos: 'DATA | EVENTO | RESPONSAVEL | NOTA' vira linha de tabela, no fim da tabela existente
  if ($b.Campos.Contains('Marco')) {
    $linhas = @($b.Campos['Marco'] | Where-Object { $_.Trim() -ne '' })
    $i = [array]::IndexOf($ls, '|---|---|---|---|')
    if ($i -ge 0 -and $linhas.Count -gt 0) {
      $fim = $i + 1
      while ($fim -lt $ls.Count -and $ls[$fim] -match '^\|') { $fim++ }
      $rows = @()
      foreach ($x in $linhas) {
        $p = @($x -split '\|' | ForEach-Object { $_.Trim() })
        while ($p.Count -lt 4) { $p += '[a preencher]' }
        $rows += ('| ' + ($p[0..3] -join ' | ') + ' |')
      }
      for ($k = $rows.Count - 1; $k -ge 0; $k--) { $ls.Insert($fim, $rows[$k]) }
      $n++
    }
  }
  [System.IO.File]::WriteAllLines($arq, $ls, (New-Object System.Text.UTF8Encoding($false)))
  Write-Output ("{0,-14} campos gravados: {1}" -f $b.Produto, $n)
  $totCampos += $n; $totArquivos++
}
Write-Output ""
Write-Output "produto.md atualizados: $totArquivos | campos gravados: $totCampos"
