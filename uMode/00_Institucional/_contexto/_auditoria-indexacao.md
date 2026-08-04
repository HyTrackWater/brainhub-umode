# Auditoria de padronização e indexação — 03 ago 2026

> Medição, não opinião: todo número aqui saiu de varredura dos arquivos reais, logo depois da
> replicação total. Serve como **linha de base** para a fase de complementação (reprocessamento
> com a nova fonte institucional) — dá pra repetir a auditoria depois e comparar.

## 1. Padronização — confirmada

Diff de headings de cada arquivo real contra o template correspondente:

| Tipo de documento | Arquivos | Resultado |
|---|---|---|
| cliente · `institucional.md` | 46 | 45 OK · **1 diverge** (conhecida) |
| cliente · `jornada.md` | 46 | OK |
| cliente · `pessoas.md` | 46 | OK |
| cliente · demandas (`D-*.md`) | 993 | OK |
| cliente · RFIs (`RFI-*.md`) | 85 | OK |
| Casa · demandas | 4 | OK |
| Casa · fichas de Pessoa | 13 | OK |
| Casa · `contexto-area.md` | 8 | OK |
| **Total auditado** | **1.241** | **1.240 conformes → 1.241 depois da correção** |

**✅ A divergência de Luiza Barcelos foi resolvida no mesmo dia** (`### ERP` + `### Notion (cadastro
de cliente)`), com decisão tomada e aplicada — ver seção 6 abaixo. Revalidado: **46 de 46
`institucional.md` conformes, 0 divergências.**

**Integridade de identificadores:** 0 IDs de demanda duplicados dentro de um cliente · 0 RFIs
duplicadas · 0 `ID legado` (UMD-xxx) reutilizado em duas demandas · 0 arquivos com mojibake ·
encoding UTF-8 sem BOM uniforme.

## 2. Indexação — o que já se relaciona de verdade

Estes são vínculos **resolvíveis por máquina**, testados:

| Vínculo | Cobertura | Teste feito |
|---|---|---|
| Demanda → casa do cliente | **993 de 993 (100%)** | `Origem (organizacional)` resolve exatamente para uma pasta de cliente existente — 0 falhas |
| Pessoa da Casa → clientes atendidos | **62 de 62 (100%)** | cada nome citado nas fichas resolve para pasta real — 0 falhas |
| Demanda → RFI | **44 de 44 (100%)** | `RFI vinculada` aponta para `RFI-AAAA-NNN` real do mesmo cliente; 0 sobraram como nome bruto |
| Demanda → sistema externo | **993 (100%)** | `Vínculo` = `CX Hub — ID: UMD-xxx`, rastreável de volta à origem |
| Consulta agregada sem índice auxiliar | funciona | "demandas de Osklen por status" respondida só por parsing de heading: 92 Concluído · 13 Backlog · 10 Cancelado · 2 Análise |

**O que isso prova:** a posição do heading é um contrato, e o contrato está 100% cumprido. O
formato **é** indexável hoje, sem precisar de banco nem de mudança de padrão.

## 3. Indexação — os eixos que ainda estão vazios

| Eixo de relação | Cobertura | Por quê |
|---|---|---|
| `Destino (organizacional)` — demanda → **Área** | **0 de 993** | Regra travada: não é derivável de nenhum campo do CX Hub (correção da Sessão 17). Exige conhecimento institucional humano |
| `Contexto consultado` / `Contexto impactado` | **0 de 993** | O ciclo de aprovação/retroalimentação está modelado e sem nenhum dado — nenhuma demanda declara qual MD ela leria ou mudaria |
| `Demanda mãe` / `Demandas filhas` | **0 de 993** | Hierarquia pai/filha existe no modelo, não nos dados (o Notion legado não tinha o conceito) |
| `contexto-area.md` de cliente | **0 de 644** (46 × 14) | Nunca levantado — pendência 9 |
| `produto.md` real | **0 de 16** | Só template; as 16 pastas de Solução não existem ainda |
| RFI → Demanda (caminho de volta) | **0 de 85** resolvem para `D-AAAA-NNN` | Dívida do Notion legado: `Demanda relacionada` traz o nome do cliente, não o ID da demanda |
| Metadado declarado (frontmatter) | **0 de 1.291** | Todo campo é texto sob heading; a indexação é *derivável por convenção*, não *declarada* |

## 4. Diagnóstico

**O cérebro hoje indexa bem o eixo CLIENTE e quase nada os eixos ÁREA e SOLUÇÃO.**

- Um agente **Por Cliente** já tem substância real para responder: quem é, o que contratou, quem
  atende, o histórico de reuniões, 993 demandas com status/tipo/responsável, 85 RFIs com escopo
  negociado e valor.
- Um agente **Por Área** ou **Por Solução** ainda não tem quase nada — porque `contexto-area.md` e
  `produto.md` estão vazios, e porque nenhuma demanda diz a qual Área ela pertence. Isso já estava
  previsto como consequência em `brainwave/CONTEXTO.md`; agora está medido.
- A hierarquia de 4 níveis (`Institucional → Áreas → Subáreas → Pessoas`) está **construída como
  pastas** em todos os 46 clientes, mas **sem conteúdo nos níveis 2 e 3**.

### Densidade
1.268 arquivos reais, 125.989 linhas, **19,2% das linhas são `[a preencher]`**. Isso não é defeito:
é o padrão funcionando como projetado (campo sem fonte fica explícito em vez de virar palpite). Mas
é a medida honesta de quanto o cérebro ainda tem de vazio.

## 5. Risco estrutural a nomear: a chave é o nome da pasta

Não existe identificador estável de cliente — a chave estrangeira de fato é o **nome da pasta**.
Funciona hoje (0 falhas em 1.055 referências testadas), mas é frágil: renomear `NK STORE` para
`NK Store` quebraria 87 vínculos de demanda **em silêncio**, sem erro nenhum. Mesmo risco para
`Básico&Co`, `Simples (by Reserva)` e qualquer cliente cujo nome comercial mude.

`CONTEXT.md` já prevê banco de dados com nomes de campo em inglês; um `client_id` estável resolveria
isso e é barato agora, caro depois. **Decisão do Vinicius/CEO** — registrado em
`_pendencias-gerais.md`.

---

## 6. Decisões tomadas e aplicadas em 03 ago 2026 (posicionamento, não opções)

O Vinicius pediu posicionamento em vez de lista de alternativas. As três decisões abaixo foram
tomadas e **aplicadas na mesma sessão**, com validação.

### 6.1 Luiza Barcelos — a divergência era do template, não do cliente

**Decisão:** os dois headings extras eram sintoma de uma lacuna real do template, não erro do
cliente. Aplicado:
- `### ERP` (sob "Sistemas e fontes de verdade") **removido** — duplicava
  `## Operação uMode → ### ERP / Integração`, que já dizia "Safe Tech". O que **só** existia nele —
  a restrição "fora do escopo de integração: Linx e qualquer outro além do Safe Tech" — foi
  preservado como nota no campo canônico. Nenhuma informação perdida.
- `### Notion (cadastro de cliente)` **não** virou heading do template. Virou item de uma seção
  nova, `### Outras fontes`, porque o problema é geral: o template só permitia `### Drive de
  operação`, e o CRM traz rotineiramente Portal do Cliente, Documentação, OKRs, material de
  apresentação, grupo de WhatsApp e base de chamados. Na 1ª rodada eu tinha jogado tudo isso em
  `## Contexto crítico` por falta de lugar — o que estava errado: link de fonte não é contexto.

**Por que assim, e não formalizando `### ERP`/`### Notion` no template:** um heading fixo por
sistema não escala (cada cliente usa um conjunto diferente) e reintroduziria a duplicação de ERP.
Uma seção com lista livre cobre qualquer combinação sem quebrar a regra de "todo MD do mesmo tipo
tem os mesmos títulos".

**Efeito:** template atualizado, 42 clientes regenerados, 4 pilotos retrofitados, as fontes que
estavam em `Contexto crítico` movidas para o lugar certo. **46 de 46 conformes.**

### 6.2 Índice — implementado agora; frontmatter, não

**Decisão: sim, implementar já** — `_indice/` com `clientes.csv`, `demandas.csv`, `rfis.csv`,
`pessoas.csv`, gerado por `scripts/gen-indice.ps1`.

**Por que agora:** é aditivo (não toca em nenhum MD), reversível (apagar a pasta não perde nada),
custa um script, e resolve exatamente a pergunta "conseguimos relacionar conteúdo?". Sem ele, toda
pergunta relacional exige varrer 1.292 arquivos. Testado logo depois de gerar: "top clientes por
demanda em aberto" (Reserva 78 · NV 36 · Osklen 15 · VIX 14 · Luiza Barcelos 14) e "valor total
negociado em RFI por cliente" (NV R$ 30.651 · NK STORE R$ 26.250 · VIX R$ 16.186) — respostas
imediatas, que antes exigiriam varredura.

**Por que NÃO frontmatter:** criaria **duas fontes de verdade para o mesmo campo** (o heading e o
metadado), com risco real de divergirem em silêncio — e mexeria em 1.292 arquivos para resolver um
problema que a auditoria mostrou não existir (o parsing por heading funciona em 100% dos casos). No
índice, a duplicação é assumida e descartável: regenerar reconcilia sempre.

**Regra que acompanha a decisão:** o índice é derivado. Nunca editar a mão; se divergir do MD, o MD
está certo e o índice está velho.

### 6.3 O problema do nome — resolvido, não registrado como pendência

**Decisão:** `### ID do cliente` — slug estável em todos os 46 (`nk-store`, `basico-co`,
`simples-by-reserva`), aplicado no template e no protocolo de criação. A chave lógica deixa de ser
o nome da pasta.

**Por que isso resolve de verdade:** o slug normaliza caixa e acento, então `NK STORE`, `NK Store` e
`NK store` colapsam no mesmo ID — a variação que o Vinicius apontou deixa de existir como problema,
em vez de virar uma linha de alias. Para os nomes que **não** colapsam (apelidos reais usados nas
fontes: `Lofty` para Lofty Style, `Lenny` para Lenny Niemeyer, `OFICINA` para Oficina Reserva,
`Reservado - Colmeia`), existe `### Aliases do cliente`, extraído dos títulos de RFI do Notion e da
pasta do Drive — nada digitado à mão.

**Efeito:** renomear um cliente passa a ser seguro (muda a pasta, o ID continua), e o índice já usa
`client_id` como chave de todas as tabelas.

> `CONTEXT.md` **não foi alterado** — as decisões acima são de padrão de documento e de ferramenta,
> não de hierarquia ou regra de negócio; ficam no protocolo e aqui. Alterar `CONTEXT.md` exige
> confirmação explícita (`CLAUDE.md`).

