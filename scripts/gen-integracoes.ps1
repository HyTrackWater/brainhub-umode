# Cria o integracao.md de cada cliente que TEM integracao, seguindo protocolo-gestao-integracao.md.
#
# Esta rodada preenche apenas a secao "Identificacao" — que sai do mapeamento autoritativo e do
# inventario de arquivos do repositorio. Todo o resto fica [a preencher] com o motivo, porque exige
# leitura do documentacao-geral-*.md de cada cliente (30 a 77 KB cada).
#
# Mapeamento repositorio -> cliente informado pelo desenvolvedor via Vinicius em 03 ago 2026.
# NAO inferir cliente pelo nome do repositorio: 'arzz-sap' e Reserva/Oficina (arzz = AZZAS, nao
# Arezzo) e 'unico-linx' e Puket.
#
# Uso: .\gen-integracoes.ps1

param(
  [string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode",
  [string]$ReposBase = "C:\Ambientes Virtuais\uMode-Integracoes",
  [string]$Hoje = "03 ago 2026"
)
$ErrorActionPreference = 'Stop'

# repo | clientes (pasta do BrainHub) | ERP
$MAP = @(
  @{ repo='arzz-sap';                       clientes=@('Reserva','Oficina Reserva'); erp='SAP' },
  @{ repo='integracao-linx-nv';             clientes=@('NV');                        erp='Linx' },
  @{ repo='unico-linx';                     clientes=@('Puket');                     erp='Linx' },
  @{ repo='integration-vix-linx';           clientes=@('VIX');                       erp='Linx' },
  @{ repo='integration-luiza-barcelos-sft'; clientes=@('Luiza Barcelos');            erp='Safe Tech' },
  @{ repo='integration-baw-linx';           clientes=@('Baw');                       erp='Linx' },
  @{ repo='integration-cambos-spi';         clientes=@('Cambos');                    erp='SPI' },
  @{ repo='integration-lofty-linx';         clientes=@('Lofty Style');               erp='Linx' },
  @{ repo='integration-nk-linx';            clientes=@('NK STORE');                  erp='Linx' },
  @{ repo='integration-osklen-linx';        clientes=@('Osklen');                    erp='Linx' }
)

function Val($ls, $h) {
  $i = [array]::IndexOf($ls, $h)
  if ($i -lt 0) { return '' }
  $j = $i + 1
  while ($j -lt $ls.Count -and ($ls[$j].Trim() -eq '' -or $ls[$j].StartsWith('>'))) { $j++ }
  if ($j -lt $ls.Count -and $ls[$j] -notmatch '^#{1,6}\s') { return $ls[$j].Trim() }
  return ''
}

$gerados = 0
$divergencias = New-Object System.Collections.Generic.List[string]

foreach ($m in $MAP) {
  $repoDir = Join-Path $ReposBase $m.repo
  $existe = Test-Path $repoDir
  $mds = @()
  if ($existe) { $mds = @(Get-ChildItem $repoDir -Recurse -Filter *.md -File | Where-Object { $_.FullName -notlike '*\node_modules\*' }) }

  foreach ($cliente in $m.clientes) {
    $dir = Join-Path $Root "uMode\_Clientes\$cliente\00_Institucional\_contexto"
    if (-not (Test-Path $dir)) { Write-Warning "sem pasta de contexto: $cliente"; continue }

    # --- checagem de consistencia com o institucional.md (regra do protocolo)
    $inst = Join-Path $dir 'institucional.md'
    $erpInst = ''
    if (Test-Path $inst) { $erpInst = Val @(Get-Content -Encoding UTF8 $inst) '### ERP / Integração' }
    $concorda = ($erpInst -like "*$($m.erp)*")
    if (-not $concorda) { $divergencias.Add("$cliente : institucional diz '$erpInst' / repositorio indica '$($m.erp)'") }

    $outros = @($m.clientes | Where-Object { $_ -ne $cliente })

    $L = New-Object System.Collections.Generic.List[string]
    $L.Add("# $cliente · Integração")
    $L.Add("")
    $L.Add("> Criado em $Hoje a partir do repositório de integração real. **Só a seção")
    $L.Add("> ""Identificação"" está preenchida** — o resto exige leitura do documento técnico do")
    $L.Add("> repositório e está marcado com o motivo. Ver ``protocolo-gestao-integracao.md``.")
    $L.Add("")
    $L.Add("## Identificação")
    $L.Add("### Cliente")
    $L.Add($cliente)
    $L.Add("### ERP / sistema integrado")
    $L.Add($m.erp)
    if (-not $concorda) {
      $L.Add("> ⚠ **Divergência não resolvida:** o ``institucional.md`` deste cliente registra")
      $L.Add("> ``ERP / Integração`` = ""$erpInst"", e o repositório de integração indica **$($m.erp)**.")
      $L.Add("> Não foi resolvido por conta própria (regra do protocolo) — pode ser ERP trocado,")
      $L.Add("> integração descontinuada, ou mais de um sistema no mesmo cliente.")
    }
    $L.Add("### Repositório de código")
    $L.Add("``github.com/UmodeApp/$($m.repo)`` · clone local em ``$ReposBase\$($m.repo)``")
    if ($outros.Count -gt 0) {
      $L.Add("> ⚠ **Este repositório atende mais de um cliente:** $cliente + $($outros -join ' + ').")
      $L.Add("> Cada casa tem o seu ``integracao.md`` (isolamento entre casas é regra travada em")
      $L.Add("> ``CONTEXT.md``), os dois apontando para o mesmo repositório. Não é duplicidade — é a")
      $L.Add("> mesma integração registrada em cada casa que ela serve. O nome ``arzz`` é **AZZAS**,")
      $L.Add("> o grupo ao qual os dois pertencem (o CRM já os classifica em ""Grupo 1: Azzas"").")
    }
    $L.Add("### Documentação de referência")
    if (-not $existe) {
      $L.Add("[a preencher — clone do repositório não encontrado em ``$ReposBase``]")
    } elseif ($mds.Count -eq 0) {
      $L.Add("**Nenhuma.** O repositório existe e tem código, mas **não contém nenhum arquivo")
      $L.Add("``.md``** — verificado em $Hoje. Registro explícito porque ""existe integração, falta")
      $L.Add("documentação"" é diferente de ""não existe integração"".")
    } else {
      foreach ($d in ($mds | Sort-Object Length -Descending)) {
        $rel = $d.FullName.Replace($repoDir + '\', '')
        $L.Add("- ``$rel`` — $([Math]::Round($d.Length/1KB)) KB")
      }
    }
    $L.Add("### Status da integração")
    $L.Add("[a preencher — nenhuma fonte lida até agora declara o estágio; o repositório tem código")
    $L.Add("ativo, o que não é o mesmo que declarar ""em produção""]")
    $L.Add("")

    # --- secoes que dependem da leitura do documento tecnico
    $motivo = "[a preencher — exige leitura do documento técnico do repositório, ainda não feita]"
    foreach ($bloco in @(
        @('## Arquitetura', @('### Direções de integração','### Mecanismo','### Ambiente e execução')),
        @('## Escrita (uMode → sistema do cliente)', @('### O que é enviado','### Gatilho e frequência','### Regras e validações')),
        @('## Leitura (sistema do cliente → uMode)', @('### O que é importado','### Gatilho e frequência','### Regras e validações')),
        @('## Tabelas e endpoints', @('### Tabelas do ERP mapeadas','### Endpoints externos utilizados'))
      )) {
      $L.Add($bloco[0])
      foreach ($sub in $bloco[1]) { $L.Add($sub); $L.Add($motivo) }
      $L.Add("")
    }
    $L.Add("## Particularidades deste cliente")
    $L.Add($motivo)
    $L.Add("")
    $L.Add("## Auditoria e monitoramento")
    $L.Add($motivo)
    $L.Add("")
    $L.Add("## Incidentes registrados")
    $L.Add("| Data | Incidente | Resolução | Fonte |")
    $L.Add("|---|---|---|---|")
    $L.Add("")
    $L.Add("## Governança")
    $L.Add("### Responsável técnico")
    $L.Add("[a preencher]")
    $L.Add("### Quem pode alterar este documento")
    $L.Add("[a preencher]")
    $L.Add("")
    $L.Add("## Fontes")
    $L.Add("### Documentos consultados")
    $L.Add("- Mapeamento repositório → cliente informado pelo desenvolvedor via Vinicius em $Hoje")
    $L.Add("  (registrado em ``protocolo-gestao-integracao.md``)")
    if ($mds.Count -gt 0) { $L.Add("- Inventário de arquivos do repositório ``$($m.repo)`` (leitura de conteúdo pendente)") }

    [System.IO.File]::WriteAllLines((Join-Path $dir 'integracao.md'), $L, (New-Object System.Text.UTF8Encoding($false)))
    $gerados++
    Write-Output ("{0,-18} <- {1,-32} ERP={2,-10} docs={3}" -f $cliente, $m.repo, $m.erp, $mds.Count)
  }
}
Write-Output ""
Write-Output "integracao.md gerados: $gerados"
if ($divergencias.Count -gt 0) {
  Write-Output "DIVERGENCIAS de ERP contra institucional.md ($($divergencias.Count)):"
  $divergencias | ForEach-Object { Write-Output "  - $_" }
} else { Write-Output "nenhuma divergencia de ERP contra institucional.md" }

