# Cria a pasta e o produto.md de cada item do Portfolio (CONTEXT.md -> "Portfolio completo de
# produtos e solucoes"), seguindo protocolo-gestao-produto.md e o _template_produto.
#
# Regra aplicada: Score de maturidade SO e preenchido quando a fonte declara producao / piloto /
# conceito de forma explicita. Onde a evidencia e ambigua ou conflitante, fica [a preencher] com a
# evidencia citada em "Fonte e data da avaliacao" — nunca um balde escolhido por intuicao.
#
# Uso: .\gen-produtos.ps1
#
# NOTA: em string com aspas duplas, $VAR seguido de ':' precisa virar ${VAR}: — o PowerShell
# interpretaria 'VAR:' como qualificador de drive e falha no parse.

param([string]$Root = "C:\Ambientes Virtuais\BrainHub\brainhub-umode")
$ErrorActionPreference = 'Stop'
$base = Join-Path $Root "uMode\03_Produto-e-Solucoes"

$V1 = 'documento "ARQUITETURA_UMODE_REF.md — Bússola Arquitetural" (v1.0, abr 2026, João Risoléo — Drive `1xCFtkT5krc-VATCC26MeQHWOWH1BOMlE`), que registra a Arquitetura uMode V1 da sessão de 24/04/2026'
$NOTION = 'página canônica **"Arquitetura uMode — Especificação por Módulo (V1 — sessão 24/04/2026)"** no Notion (`34db1d38e768814b8001d7cb6cacf4e5`, sob "AGENTES E PROJETOS") — a fonte de verdade declarada, lida na íntegra em 03 ago 2026'
$ACESSOS = 'planilha "uMode - Controle de Acessos" (Drive `1JsMyuSR3kl0l2AzOGsKikqVNVrBDbhFvgKVhZMYdSWI`, viva — última modificação 03 ago 2026)'

# nome | destino | area conectada | descricao | geracao | legado | maturidade | fonte da maturidade | upstream | downstream | clientes
$P = @(
  @{ n='PlanejAI'; d='Voltada ao cliente'; a='Planejamento'; desc='Do histórico ao mix de coleção. É o 1º módulo do fluxo oficial da Arquitetura uMode V1.'; g='Nativa'; leg='uPlan (linhagem confirmada pelo Vinicius, 13 jul 2026)';
     m='MVP'; fm="Decidido em 03 ago 2026 com a leitura da ${NOTION}. A página separa **dois modos operacionais**: ""PRÉ-SEASON (**modo atual** — estúdio sob demanda)"" × ""IN-SEASON (**modo futuro** — a partir do último trimestre do ano)"". Ou seja: opera hoje e tem arquitetura definida (histórico → 4 indicadores → score → sazonalidade → potencial inexplorado → mix → briefing pro CriAI), mas é entregue como estúdio sob demanda e metade do escopo ainda não existe — MVP pela regra do protocolo, não Escalável. Uso real com cliente confirmado no Drive (reuniões ""uMode + RSV - PlanejAI"", 22 jul 2026; ""PlanejAI - Documentação de Negócios"", 05 mai 2026).";
     up='[a preencher — é o início do fluxo V1]'; dn='CriAI (próximo módulo no fluxo V1)'; cli='[a preencher]' },
  @{ n='CriAI'; d='Voltada ao cliente'; a='Estilo / Criação'; desc='Briefing → criação. 2º módulo do fluxo oficial da Arquitetura uMode V1.'; g='Nativa'; leg='[a preencher]';
     m='Escalável'; fm="Decisão registrada em 14 jul 2026 (`_varredura-drive-notas.md`), a partir de repositório real próprio com métrica de ""87.75% robustez"" citada na documentação do produto. Confirmado como módulo oficial da V1 pelo $V1.";
     up='PlanejAI'; dn='DesenvolvAI'; cli='[a preencher]' },
  @{ n='DesenvolvAI'; d='Voltada ao cliente'; a='Desenvolvimento de Coleção'; desc='Croqui → lacre. 3º módulo do fluxo oficial da V1. É o carro-chefe histórico da uMode.'; g='Nativa'; leg='uFlow (linhagem confirmada pelo Vinicius, 13 jul 2026 — módulo de Gestão de Coleção)';
     m='Escalável'; fm="Uso em produção em escala, medido na ${ACESSOS}: 1.376 usuários cadastrados em contas de uFlow, 653 com acesso em jul/2026 (65% de engajamento), distribuídos em ~20 organizações — inclui contas nomeadas explicitamente como uFlow (ex.: ""Cambos - uFlow""). Também é módulo oficial da V1.";
     up='CriAI'; dn='FornecAI'; cli='[a preencher — a planilha de acessos lista as organizações com conta ativa, mas a reconciliação conta↔cliente↔módulo contratado ainda não foi feita; ver _varredura-ferramentas-produtos-areas.md]' },
  @{ n='FornecAI'; d='Voltada ao cliente'; a='Compras / Supply / Sourcing'; desc='Ambiente do fornecedor. 4º módulo do fluxo oficial da V1.'; g='Nativa'; leg='[a preencher — hipótese uBuy ≈ FornecAI levantada e NÃO confirmada pelo Vinicius, ver _pendencias-gerais.md item 10]';
     m='Ideação'; fm="Declaração explícita no ${V1}: ""FornecAI ainda não nasceu"" (justificando por que o VendeAI mantém `organizations` simples). O mesmo documento fala da ""jornada 3 do FornecAI"" como algo a ativar no futuro. Achado em 03 ago 2026 — antes disso o item estava sem evidência.";
     up='DesenvolvAI'; dn='EnriqueceAI'; cli='Nenhum — produto ainda não nasceu' },
  @{ n='EnriqueceAI'; d='Voltada ao cliente'; a='E-commerce / Cadastro'; desc='Lacre → catálogo (atributos, SEO). 5º módulo do fluxo oficial da V1.'; g='Nativa'; leg='[a preencher]';
     m='MVP'; fm="Decidido em 03 ago 2026 com a leitura da ${NOTION}, que afirma em maiúsculas: **""A detecção de atributos a partir da foto do produto JÁ EXISTE e é a espinha dorsal do módulo atual""** — o cerne do módulo está vivo, lendo a foto do produto real lacrado e extraindo atributos via Taxonomia. Somado ao uso iterativo com cliente (reuniões ""enriqueceAI NV"" 09 jul 2026 e ""Melhorias EnriqueceAI NV"" 10 jul 2026; diretriz `enriqueceai_diretriz.json`), fecha em MVP: arquitetura definida e núcleo em uso real, sem declaração de escala multi-cliente que sustentaria Escalável.";
     up='DesenvolvAI · FornecAI'; dn='GerenciAI'; cli='NV (uso real confirmado em reuniões de jul 2026 — qualificador contratado/piloto a confirmar)' },
  @{ n='GerenciAI'; d='Voltada ao cliente'; a='Planejamento + Financeiro'; desc='Planejado × realizado. 6º e último módulo do fluxo oficial da V1.'; g='Nativa'; leg='[a preencher]';
     m='Ideação'; fm="Confirmado em 03 ago 2026 pela ${NOTION}, cuja própria seção ""Status"" do módulo diz: **""Brainstorm consolidado, não decisão final""**, com fala literal do CEO — ""estou no campo do brainstorm, não tenho opinião formada, vou ter que conceber"" — e instrução de ""tratar como visão direcional para discussão com André, não como spec fechada"". Alinha com a declaração no ${V1}: ""GerenciAI ainda em brainstorm"" (justificando por que o VendeAI ainda não emite eventos para ele). O documento prevê que ""quando GerenciAI tiver motor de regras, VendeAI publica eventos"". Achado em 03 ago 2026.";
     up='EnriqueceAI · PlanejAI'; dn='[a preencher — é o fim do fluxo V1]'; cli='Nenhum registrado' },
  @{ n='AlocAI'; d='Voltada ao cliente'; a='Logística / CD'; desc='Alocação e distribuição por loja.'; g='Nativa'; leg='[a preencher]';
     m='[a preencher]'; fm='Nenhuma evidência encontrada na varredura de 03 ago 2026: não aparece no fluxo da Arquitetura uMode V1 (que cobre 6 módulos + 2 pilares), não tem repositório localizado (varredura de 14 jul 2026) e não aparece em documento, reunião ou conta de acesso. Ausência de evidência não é evidência de Ideação — por isso [a preencher] e não um balde.';
     up='[a preencher]'; dn='[a preencher]'; cli='Nenhum registrado' },
  @{ n='VendeAI'; d='Voltada ao cliente'; a='Comercial / Vendas'; desc='Motor de vendas — sessão de atendimento com composição de looks, try-on por IA e swipe do cliente.'; g='Nativa'; leg='[a preencher]';
     m='MVP'; fm="Declaração explícita no ${V1}: ""VendeAI NÃO está na Arquitetura uMode V1"" — é ""piloto de validação de tese com a NK"", com critérios formais de promoção a módulo oficial (conversão sessão→venda ≥ 30%, NPS vendedor ≥ 7, NPS cliente ≥ 8, LGPD auditado, ≥ 50 sessões reais de try-on). Confirma a avaliação já registrada em 14 jul 2026.";
     up='CadastrAI · CriAI (posicionamento provável, a confirmar pós-piloto)'; dn='[a preencher — pendente da promoção a módulo V1]'; cli='NK STORE (piloto)' },
  @{ n='CliprocAI'; d='Voltada ao cliente'; a='Comercial / Vendas'; desc='Decisão CLIente × PROduto × CAnal.'; g='Nativa'; leg='[a preencher]';
     m='MVP'; fm='Registrado em 14 jul 2026 (`_pendencias-gerais.md` item 22) a partir do PRD real na pasta Drive da Cambos: PRD v1.6 com 17 ADRs, protótipo navegável com dado real, mesmo padrão ADR-006 do VendeAI (fora da Arquitetura V1 oficial até validação), com meta de piloto ≥25% de conversão em 90 dias.';
     up='[a preencher]'; dn='[a preencher]'; cli='Cambos (piloto)' },
  @{ n='CadastrAI'; d='Interna'; a=''; desc='Fonte única e governante de dados — sustenta todo o portfólio. É o núcleo da Arquitetura uMode V1 (não está no fluxo linear: é o centro que os módulos consomem).'; g='Nativa'; leg='[a preencher]';
     m='[a preencher]'; fm="Evidências conflitantes, não resolvidas por conta própria: o $V1 o trata como núcleo da arquitetura e responsável pela auditoria de cadastro, mas em tempo futuro — ""produtos importados vão validar contra taxonomia + audit_status **quando CadastrAI estiver vivo**"" (abr 2026). Em paralelo há uso real com cliente (planilha ""NV _ CadastrAI _ Definição de Grupos e Atributos.xlsx"", abr 2026) e um repositório candidato (`catalogcraft-ai`/`umode-catalog-ai`, nome exato não confirmado — `_pendencias-gerais.md` item 21).";
     up='[a preencher]'; dn='Todos os módulos do fluxo V1 (é o núcleo)'; cli='' },
  @{ n='Taxonomia'; d='Interna'; a=''; desc='Padrão de atributos — base transversal. É o idioma comum que conecta histórico de venda → pesquisa → briefing → criação → auditoria → descrição → catálogo de fornecedor.'; g='Nativa'; leg='[a preencher]';
     m='Escalável'; fm="Implementada e tratada como padrão inviolável no $V1, com dimensionamento concreto: **12 zonas, 42 dimensões, 419 valores**. O documento a lista entre os itens que ""a loja NÃO cria"" (só apelida via `taxonomy_nicknames`) e registra que o VendeAI a replica via seed — ou seja, já é consumida por outro módulo. Modelo PLM Padrão associado: 12 premissas, 6 categorias, 9 verticais.";
     up='[a preencher]'; dn='CadastrAI · CriAI · VendeAI · EnriqueceAI (todos consomem o mesmo vocabulário)'; cli='' },
  @{ n='CX Hub'; d='Interna'; a=''; desc='Experiência do cliente — ferramenta oficial de gestão de demandas do atendimento interno.'; g='Nativa'; leg='[a preencher]';
     m='Escalável'; fm='Registrado em 14 jul 2026: documentação real do repositório (`gist-sparkle`) declara "Fases 0-9 concluídas, em produção". É a mesma ferramenta operacional referenciada pelo campo `Vínculo` das 997 demandas formalizadas neste repositório.';
     up='[a preencher]'; dn='[a preencher]'; cli='' },
  @{ n='ONB HUB'; d='Interna'; a=''; desc='Onboarding e operação de implantação.'; g='Nativa'; leg='[a preencher]';
     m='[a preencher]'; fm='Repositório de código ativo confirmado (`umode-gest-o-de-opera-o-2f6bdc59`, via `launch.json` do CEO, registrado em 10 jul 2026), mas nenhuma fonte declara estágio (produção/piloto/conceito). Não aparece na Arquitetura uMode V1, que cobre só os módulos de cliente + 2 pilares.';
     up='[a preencher]'; dn='[a preencher]'; cli='' },
  @{ n='IntHub'; d='Interna'; a=''; desc='Integrações · gold standard.'; g='Nativa'; leg='[a preencher]';
     m='[a preencher]'; fm='Repositório de código ativo confirmado (`integration-pulse-check-e914756f`, via `launch.json` do CEO, registrado em 10 jul 2026), sem declaração de estágio em nenhuma fonte.';
     up='[a preencher]'; dn='[a preencher]'; cli='' },
  @{ n='Gest Hub'; d='Interna'; a=''; desc='Gestão interna.'; g='Nativa'; leg='[a preencher]';
     m='[a preencher]'; fm='Repositório de código ativo confirmado (`umode-gesthub`, via `launch.json` do CEO, registrado em 10 jul 2026), sem declaração de estágio em nenhuma fonte.';
     up='[a preencher]'; dn='[a preencher]'; cli='' },
  @{ n='Sales Hub'; d='Interna'; a=''; desc='Ferramenta interna de vendas.'; g='Nativa'; leg='[a preencher]';
     m='[a preencher]'; fm='A única fonte é a própria tabela de Portfólio em `CONTEXT.md`, que o descreve como "em construção" — expressão que não cai claramente em nenhum dos três baldes da regra de tradução (produção → Escalável / piloto com arquitetura definida → MVP / conceito → Ideação). Nenhum repositório localizado na varredura de 14 jul 2026.';
     up='[a preencher]'; dn='[a preencher]'; cli='' }
)

function Slug($n) { return (($n -replace '[^a-zA-Z0-9]+','-').Trim('-')) }
$i = 0
foreach ($p in $P) {
  $i++
  $pasta = Join-Path $base ("{0:D2}_{1}" -f $i, (Slug $p.n))
  foreach ($sub in @('_contexto','_protocolos')) { New-Item -ItemType Directory -Force -Path (Join-Path $pasta $sub) | Out-Null }

  $L = New-Object System.Collections.Generic.List[string]
  $L.Add("# $($p.n) · Produto")
  $L.Add("")
  $L.Add("> Criado em 03 ago 2026 pela varredura geral de ferramentas/produtos/áreas. Segue")
  $L.Add("> ``protocolo-gestao-produto.md``. Campo sem fonte explícita fica ``[a preencher]`` — inclusive")
  $L.Add("> o score de maturidade, que **não** é escolhido por intuição.")
  $L.Add("")
  $L.Add("## Identificação")
  $L.Add("### Nome atual")
  $L.Add($p.n)
  $L.Add("### Nome legado")
  $L.Add($p.leg)
  $L.Add("### Descrição")
  $L.Add($p.desc)
  $L.Add("### Destino")
  $L.Add($p.d)
  $L.Add("### Área canônica do cliente conectada")
  if ($p.d -eq 'Voltada ao cliente') { $L.Add($p.a) } else { $L.Add('[não aplicável — produto interno]') }
  $L.Add("### Geração")
  $L.Add($p.g)
  $L.Add("")
  $L.Add("## Maturidade")
  $L.Add("### Score de maturidade")
  $L.Add($p.m)
  $L.Add("### Fonte e data da avaliação")
  $L.Add($p.fm)
  $L.Add("")
  $L.Add("## Pipeline e relações")
  $L.Add("### Consome de (upstream)")
  $L.Add($p.up)
  $L.Add("### Produz para (downstream)")
  $L.Add($p.dn)
  $L.Add("### Módulos relacionados")
  if ($p.d -eq 'Voltada ao cliente') {
    $L.Add("Fluxo oficial da Arquitetura uMode V1 (24/04/2026): PlanejAI → CriAI → DesenvolvAI →")
    $L.Add("FornecAI → EnriqueceAI → GerenciAI, com CadastrAI como núcleo e Hub de Agentes lateral.")
  } else {
    $L.Add("[a preencher]")
  }
  $L.Add("")
  $L.Add("## Adoção por cliente")
  if ($p.d -eq 'Interna') {
    $L.Add("Não aplicável — produto interno, usado pela Casa para atender clientes, não contratado")
    $L.Add("individualmente por eles")
    $L.Add("### Clientes que contrataram")
    $L.Add("[não aplicável — Destino = Interna]")
  } else {
    $L.Add("### Clientes que contrataram")
    $L.Add($p.cli)
  }
  $L.Add("")
  $L.Add("## Marcos")
  $L.Add("| Data | Evento/decisão | Responsável | Nota |")
  $L.Add("|---|---|---|---|")
  $L.Add("| 24/04/2026 | Arquitetura uMode V1 definida em sessão | João Risoléo | 6 módulos no fluxo + CadastrAI (núcleo) + Hub de Agentes (lateral) |")
  $L.Add("| 03/08/2026 | Registro formalizado no BrainHub | [a preencher] | Primeira vez que este item do Portfólio ganha ``produto.md`` real |")
  $L.Add("")
  $L.Add("## Governança")
  $L.Add("### Owner / Estratégia")
  if ($p.n -eq 'CX Hub') { $L.Add('João Risoléo (registrado em 14 jul 2026)') } else { $L.Add('[a preencher]') }
  $L.Add("### Operador")
  if ($p.n -eq 'CX Hub') { $L.Add('Victor Aragão (registrado em 14 jul 2026)') } else { $L.Add('[a preencher]') }
  $L.Add("### Quem pode alterar este documento")
  $L.Add("[a preencher]")
  $L.Add("")
  $L.Add("## Fontes e referências")
  $L.Add("### Documentos técnicos consultados")
  $L.Add("- ``CONTEXT.md`` → ""Portfólio completo de produtos e soluções"" (lista travada dos 16 itens)")
  $L.Add("- $V1")
  $L.Add("- ⚠ **Fonte de verdade canônica declarada está no Notion**, não no Drive: página ""Arquitetura")
  $L.Add("  uMode V1"" (``34db1d38e768814b8001d7cb6cacf4e5``) e skill ``umode-arquitetura-tese``")
  $L.Add("  (``34db1d38e768819abc2dc7844ff2be59``). O próprio documento de arquitetura diz: ""se")
  $L.Add("  contradição entre este arquivo e a página V1 → página V1 vence"".")
  $L.Add("- ✅ **A página V1 do Notion foi lida na íntegra em 03 ago 2026** (51 KB, especificação módulo a")
  $L.Add("  módulo). É de onde vêm as decisões de maturidade desta rodada. Nota de nomenclatura: a página")
  $L.Add("  canônica escreve **""ForneceAI""**, e ``CONTEXT.md`` escreve **""FornecAI""** — divergência real")
  $L.Add("  entre fontes, registrada em ``_pendencias-gerais.md``; nenhum dos dois foi alterado por conta")
  $L.Add("  própria.")

  [System.IO.File]::WriteAllLines((Join-Path $pasta "_contexto\produto.md"), $L, (New-Object System.Text.UTF8Encoding($false)))
  Write-Output ("{0,-14} {1,-20} maturidade={2}" -f ("{0:D2}_{1}" -f $i, (Slug $p.n)), $p.d, $p.m)
}
Write-Output ""
Write-Output "produtos criados: $i"   # $P.Count nao serve: enumeracao de membro devolveria o Count de cada hashtable





