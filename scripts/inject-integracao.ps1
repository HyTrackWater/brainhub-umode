# Injeta no integracao.md de cada cliente o conteudo extraido da documentacao real do repositorio
# de integracao. Segue protocolo-gestao-integracao.md.
#
# Formato do arquivo de lote:
#   @@CLIENTE: NK STORE
#   @@Status da integração
#   <linhas>
#   @@Direções de integração
#   <linhas>
#   ...
#   @@CLIENTE: outro
#
# 'Reserva/Oficina' e um caso especial: um repositorio (arzz-sap) serve DOIS clientes, entao o
# mesmo conteudo entra em Reserva e em Oficina Reserva (cada casa tem o seu arquivo — isolamento
# entre casas e regra travada em CONTEXT.md).
#
# Uso: .\inject-integracao.ps1 -Lote '...\lote-integracao-A.md'

param(
  [Parameter(Mandatory=$true)][string]$Lote,
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode",
  [string]$Hoje = "03 ago 2026"
)
$ErrorActionPreference = 'Stop'

# campo do lote -> (H2 de contexto | heading destino). H2 vazio = heading unico no arquivo.
$MAPA = [ordered]@{
  'Status da integração'            = @('', '### Status da integração')
  'Direções de integração'          = @('', '### Direções de integração')
  'Mecanismo'                       = @('', '### Mecanismo')
  'Ambiente e execução'             = @('', '### Ambiente e execução')
  'O que é enviado'                 = @('', '### O que é enviado')
  'Gatilho e frequência da escrita'  = @('## Escrita (uMode → sistema do cliente)', '### Gatilho e frequência')
  'Regras e validações da escrita'   = @('## Escrita (uMode → sistema do cliente)', '### Regras e validações')
  'O que é importado'               = @('', '### O que é importado')
  'Gatilho e frequência da leitura'  = @('## Leitura (sistema do cliente → uMode)', '### Gatilho e frequência')
  'Regras e validações da leitura'   = @('## Leitura (sistema do cliente → uMode)', '### Regras e validações')
  'Tabelas do ERP mapeadas'         = @('', '### Tabelas do ERP mapeadas')
  'Endpoints externos utilizados'   = @('', '### Endpoints externos utilizados')
  'Particularidades deste cliente'  = @('', '## Particularidades deste cliente')
  'Auditoria e monitoramento'       = @('', '## Auditoria e monitoramento')
  'Responsável técnico'             = @('', '### Responsável técnico')
}

# ---------------- le o lote
$blocos = New-Object System.Collections.Generic.List[object]
$atualCliente = $null; $atualCampo = $null; $dados = $null
foreach ($lin in (Get-Content -Encoding UTF8 $Lote)) {
  if ($lin -match '^@@CLIENTE:\s*(.+?)\s*$') {
    if ($atualCliente) { $blocos.Add([pscustomobject]@{ Cliente = $atualCliente; Campos = $dados }) }
    $atualCliente = $Matches[1]; $dados = [ordered]@{}; $atualCampo = $null
    continue
  }
  if ($lin -match '^@@(.+?)\s*$') { $atualCampo = $Matches[1]; $dados[$atualCampo] = New-Object System.Collections.Generic.List[string]; continue }
  if ($atualCampo) { $dados[$atualCampo].Add($lin) }
}
if ($atualCliente) { $blocos.Add([pscustomobject]@{ Cliente = $atualCliente; Campos = $dados }) }
Write-Output "lote: $($blocos.Count) cliente(s)"

function Set-Campo($ls, $h2, $h3, $conteudo) {
  $ini = 0
  if ($h2 -ne '') {
    $ini = $ls.IndexOf($h2)
    if ($ini -lt 0) { return $false }
  }
  # acha o heading destino a partir de $ini, sem sair da secao H2 (quando ela existe)
  $i = -1
  for ($k = $ini + 1; $k -lt $ls.Count; $k++) {
    if ($h2 -ne '' -and $ls[$k] -match '^##\s' -and $ls[$k] -ne $h2) { break }
    if ($ls[$k] -eq $h3) { $i = $k; break }
  }
  if ($i -lt 0) { return $false }
  # remove o conteudo atual da secao (ate o proximo heading)
  $fim = $i + 1
  while ($fim -lt $ls.Count -and $ls[$fim] -notmatch '^#{1,6}\s') { $fim++ }
  for ($k = $fim - 1; $k -gt $i; $k--) { $ls.RemoveAt($k) }
  # insere o novo
  $novo = @($conteudo | Where-Object { $_ -ne $null })
  while ($novo.Count -gt 0 -and $novo[0].Trim() -eq '') { $novo = @($novo[1..($novo.Count-1)]) }
  while ($novo.Count -gt 0 -and $novo[-1].Trim() -eq '') { $novo = @($novo[0..($novo.Count-2)]) }
  if ($novo.Count -eq 0) { return $false }
  for ($k = $novo.Count - 1; $k -ge 0; $k--) { $ls.Insert($i + 1, $novo[$k]) }
  return $true
}

$totCampos = 0; $totArquivos = 0
foreach ($b in $blocos) {
  # 'Reserva/Oficina' = um repositorio, dois clientes
  $clientes = if ($b.Cliente -match '^Reserva/Oficina$') { @('Reserva','Oficina Reserva') } else { @($b.Cliente) }
  foreach ($cliente in $clientes) {
    $arq = Join-Path $Root "uMode\_Clientes\$cliente\00_Institucional\_contexto\integracao.md"
    if (-not (Test-Path $arq)) { Write-Warning "sem integracao.md: $cliente"; continue }
    $ls = New-Object System.Collections.Generic.List[string]
    Get-Content -Encoding UTF8 $arq | ForEach-Object { $ls.Add($_) }
    $n = 0
    foreach ($campo in $b.Campos.Keys) {
      if ($campo -eq 'Incidentes registrados') { continue }   # tratado abaixo, e tabela
      if (-not $MAPA.Contains($campo)) { Write-Warning "campo desconhecido no lote: '$campo'"; continue }
      $m = $MAPA[$campo]
      if (Set-Campo $ls $m[0] $m[1] $b.Campos[$campo]) { $n++ }
      else { Write-Warning "$cliente : nao localizou '$($m[1])'$(if($m[0]){" em '$($m[0])'"})" }
    }
    # --- incidentes: linhas "DATA | INCIDENTE | RESOLUCAO | FONTE" viram linhas de tabela
    if ($b.Campos.Contains('Incidentes registrados')) {
      $linhas = @($b.Campos['Incidentes registrados'] | Where-Object { $_.Trim() -ne '' })
      $temIncidente = ($linhas.Count -gt 0 -and $linhas[0].Trim().ToLower() -notmatch '^nenhum')
      if ($temIncidente) {
        $i = $ls.IndexOf('|---|---|---|---|')
        if ($i -ge 0) {
          $rows = @()
          foreach ($x in $linhas) {
            $p = @($x -split '\|' | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' })
            if ($p.Count -ge 2) { while ($p.Count -lt 4) { $p += '[a preencher]' }; $rows += ('| ' + ($p[0..3] -join ' | ') + ' |') }
          }
          for ($k = $rows.Count - 1; $k -ge 0; $k--) { $ls.Insert($i + 1, $rows[$k]) }
          $n++
        }
      }
    }
    # --- nota de origem no rodape de Fontes
    $iF = $ls.IndexOf('### Documentos consultados')
    if ($iF -ge 0) {
      $fim = $iF + 1
      while ($fim -lt $ls.Count -and $ls[$fim] -notmatch '^#{1,6}\s') { $fim++ }
      $ls.Insert($fim, "- **Conteúdo técnico extraído em $Hoje** da documentação real do repositório clonado")
      $ls.Insert($fim + 1, "  (``docs/documentacao-geral-*.md``). Resumo com ponteiro, conforme o protocolo — a")
      $ls.Insert($fim + 2, "  especificação completa continua no repositório, não foi copiada para cá.")
    }
    # --- cabecalho: deixa de dizer que so a Identificacao esta preenchida
    for ($k = 0; $k -lt [Math]::Min($ls.Count, 8); $k++) {
      if ($ls[$k] -like '*Só a seção*') {
        $ls[$k] = "> Criado em $Hoje a partir do repositório de integração real, e **preenchido com a"
        if ($k + 1 -lt $ls.Count) { $ls[$k+1] = "> documentação técnica do próprio repositório** em $Hoje. Ver ``protocolo-gestao-integracao.md``." }
        if ($k + 2 -lt $ls.Count -and $ls[$k+2] -like '*repositório e está marcado*') { $ls.RemoveAt($k+2) }
        break
      }
    }
    [System.IO.File]::WriteAllLines($arq, $ls, (New-Object System.Text.UTF8Encoding($false)))
    Write-Output ("{0,-18} campos preenchidos: {1}" -f $cliente, $n)
    $totCampos += $n; $totArquivos++
  }
}
Write-Output ""
Write-Output "arquivos atualizados: $totArquivos | campos preenchidos: $totCampos"

