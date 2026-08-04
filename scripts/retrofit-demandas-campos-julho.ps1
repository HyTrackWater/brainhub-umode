# Retrofit dos campos que a v3 do gen-demandas passou a aproveitar, nas demandas que JA existiam
# (as 236 dos 4 clientes-piloto, geradas pela v1).
#
# Por que retrofit e nao regeneracao: as 85 demandas de Lofty Style tem narrativa extraida de
# export HTML por pagina (jul 2026) que NAO esta no CSV — regenerar apagaria isso. O retrofit
# toca somente 3 campos e nunca a Descricao.
#
# Campos aplicados (todos registrados em protocolo-gestao-demanda.md antes desta rodada):
#   ### RFI vinculada      <- coluna 'RFI' do Notion, resolvida contra as RFIs formalizadas
#   ### Motivo de bloqueio <- coluna 'Bloqueio' do Notion (tabela de traducao no protocolo)
#   ### Notas internas     <- bloco "[Campos legados do Notion sem campo equivalente no padrao]"
#
# Casamento por 'ID legado (Notion/CX Hub)' <-> coluna 'ID' do CSV.
#
# Uso: .\retrofit-demandas-campos-julho.ps1 -CsvPath '...\_all.csv' -Clientes 'Lofty Style','Cambos'

param(
  [Parameter(Mandatory=$true)][string]$CsvPath,
  [Parameter(Mandatory=$true)][string[]]$Clientes,
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode"
)

$ErrorActionPreference = 'Stop'

function Limpa($v) {
  if ($null -eq $v) { return '' }
  $bs = [string][char]92
  $pat = '[' + $bs + $bs + ']([^a-zA-Z0-9\s])'
  $x = $v -replace '\s*\(https?://[^)]*\)', ''
  $x = $x -replace $pat, '$1'
  return ($x -replace "`r", '').Trim()
}
function Achata($v) { return ((Limpa $v) -replace "`n", ' · ') }
function Chave($s) { return (($s -replace '[^\p{L}\p{N}]', '').ToLower()) }

function Get-Bloqueio($bloqueio) {
  $b = (Limpa $bloqueio)
  if ($b -eq '') { return '' }
  if ($b -eq 'Aguardando o Cliente') { return 'Aguardando Cliente' }
  return "Outra — valor legado do Notion: ""$b"""
}

$all = Import-Csv $CsvPath
$porId = @{}
foreach ($r in $all) { $k = (Limpa $r.ID); if ($k -ne '') { $porId[$k] = $r } }

$totAlterados = 0; $totRfi = 0; $totBloq = 0; $totLegado = 0; $semMatch = 0

foreach ($cliente in $Clientes) {
  $dir = Join-Path $Root "uMode\_Clientes\$cliente\00_Institucional\_demandas"
  if (-not (Test-Path $dir)) { Write-Warning "sem pasta de demandas: $cliente"; continue }

  # mapa das RFIs formalizadas deste cliente (nome -> ID nosso)
  $mapaRfi = @{}
  $rfiDir = Join-Path $Root "uMode\_Clientes\$cliente\00_Institucional\_rfis"
  if (Test-Path $rfiDir) {
    foreach ($arq in (Get-ChildItem $rfiDir -Filter "RFI-*.md" -File)) {
      $ls = @(Get-Content -Encoding UTF8 $arq.FullName)
      $iId = [array]::IndexOf($ls, '### ID')
      $iNome = [array]::IndexOf($ls, '### Nome / Descrição')
      if ($iId -ge 0 -and $iNome -ge 0) {
        $k = Chave $ls[$iNome + 1]
        if ($k -ne '' -and -not $mapaRfi.ContainsKey($k)) { $mapaRfi[$k] = @{ Id = $ls[$iId + 1]; Nome = $ls[$iNome + 1] } }
      }
    }
  }

  $alterados = 0
  foreach ($arq in (Get-ChildItem $dir -Filter "D-*.md" -File)) {
    $ls = @(Get-Content -Encoding UTF8 $arq.FullName)
    $iLeg = [array]::IndexOf($ls, '### ID legado (Notion/CX Hub)')
    if ($iLeg -lt 0) { continue }
    $idLegado = $ls[$iLeg + 1].Trim()
    if (-not $porId.ContainsKey($idLegado)) { $semMatch++; continue }
    $r = $porId[$idLegado]
    $mudou = $false

    # ---- RFI vinculada
    $rfiFonte = Limpa $r.'RFI'
    if ($rfiFonte -ne '') {
      $iRfi = [array]::IndexOf($ls, '### RFI vinculada')
      if ($iRfi -ge 0 -and $ls[$iRfi + 1] -eq '[a preencher]') {
        $k = Chave $rfiFonte
        if ($mapaRfi.ContainsKey($k)) {
          $ls[$iRfi + 1] = "$($mapaRfi[$k].Id) — $($mapaRfi[$k].Nome)"
        } else {
          $ls[$iRfi + 1] = "$rfiFonte [nome bruto da RFI no Notion — não casou com nenhuma RFI formalizada deste cliente; reconciliar manualmente, ver protocolo-gestao-rfi.md]"
        }
        $mudou = $true; $totRfi++
      }
    }

    # ---- Motivo de bloqueio (o valor real prevalece sobre o inferido de Standby)
    $bloq = Get-Bloqueio $r.'Bloqueio'
    if ($bloq -ne '') {
      $iB = [array]::IndexOf($ls, '### Motivo de bloqueio')
      if ($iB -ge 0 -and $ls[$iB + 1] -ne $bloq) {
        $antigo = $ls[$iB + 1]
        $ls[$iB + 1] = $bloq
        if ($antigo -eq 'Aguardando Decisão') {
          # valor que a v1 inferiu de 'Standby - Produto'; o motivo real da fonte substitui
          $ls[$iB + 1] = "$bloq (substitui ""Aguardando Decisão"", que a 1ª formalização havia inferido da regra de Standby - Produto; a fonte traz o motivo real)"
        }
        $mudou = $true; $totBloq++
      }
    }

    # ---- bloco de campos legados em Notas internas
    $iNotas = [array]::IndexOf($ls, '### Notas internas')
    $temBloco = ($ls -join "`n") -like '*Campos legados do Notion sem campo equivalente*'
    if ($iNotas -ge 0 -and -not $temBloco) {
      $legado = New-Object System.Collections.Generic.List[string]
      foreach ($col in @('Responsabilidade','Projeto','uMode - Macro Tema','Comentário uMode',
                         'Suporte Integração','Tempo de Resolução','Nível de Esforço')) {
        $v = Achata $r.$col
        if ($v -ne '') { $legado.Add("- ``$col``: $v") }
      }
      if ($legado.Count -gt 0) {
        # acha o fim da secao (proximo heading depois de ### Notas internas)
        $iFim = $iNotas + 1
        while ($iFim -lt $ls.Count -and $ls[$iFim] -notmatch '^#{1,6}\s') { $iFim++ }
        $novo = New-Object System.Collections.Generic.List[string]
        for ($i = 0; $i -lt $iFim; $i++) { $novo.Add($ls[$i]) }
        # se a secao estava vazia (so [a preencher]), o bloco legado substitui o placeholder
        if ($novo.Count -eq $iNotas + 2 -and $novo[$iNotas + 1] -eq '[a preencher]') { $novo.RemoveAt($novo.Count - 1) }
        $novo.Add('[Campos legados do Notion sem campo equivalente no padrão — preservados aqui')
        $novo.Add('para não perder dado; ver protocolo-gestao-demanda.md]')
        foreach ($x in $legado) { $novo.Add($x) }
        for ($i = $iFim; $i -lt $ls.Count; $i++) { $novo.Add($ls[$i]) }
        $ls = $novo.ToArray()
        $mudou = $true; $totLegado++
      }
    }

    if ($mudou) {
      [System.IO.File]::WriteAllLines($arq.FullName, $ls, (New-Object System.Text.UTF8Encoding($false)))
      $alterados++
    }
  }
  Write-Output ("{0,-18} arquivos alterados: {1}" -f $cliente, $alterados)
  $totAlterados += $alterados
}

Write-Output ""
Write-Output "TOTAL alterados: $totAlterados | RFI vinculada: $totRfi | Motivo de bloqueio: $totBloq | bloco legado: $totLegado | sem match de ID: $semMatch"

