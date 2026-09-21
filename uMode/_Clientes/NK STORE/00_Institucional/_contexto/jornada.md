# NK STORE · Jornada

> **Reescrito em 21 set 2026 a partir do Notion ao vivo**, incluindo a sub-página
> *Perfil de Usuário e Permissionamentos*. Campo sem fonte fica `[a preencher]`.

## ⚠ O que este documento NÃO resolve
- **A base de usuários parou em março de 2025.** Criada em 13/03/2025, última data 10/03/2025.
  Os chamados são de **jan/2026**. **Dez meses de buraco** entre cadastro e uso.
- **As bases `Reuniões com Cliente` e `Demandas` não foram varridas.** São duas bases inteiras
  dentro da página.
- **8 sub-páginas e 4 arquivos do Google não foram abertos**, incluindo
  *NK | Dúvidas Pendentes Integração de Escrita (29/05/2025)*, que trata de frente aberta.
- **Os anos dos kick-offs** (18/06, 19/06, 28/06) **não estão escritos**; foram atribuídos a
  **2024** porque a `Data Ativação Cliente` é 10/06/2024. **É inferência, e está marcada.**

## Status atual
**`Ongoing`** · 4 de 7 módulos · ERP **Linx** · grupo **`Médios`** · receita **R$ 144 mi**.

## Fase atual
**Operação com backlog acumulado.** 30 chamados em 24 dias, **21 abertos** —
**a pior proporção da carteira (70%)**. NV tem 16/39, VIX 16/28, Lofty Style 12/15.

E **a dor 7 das 10 mapeadas na venda virou defeito em produção**: a preocupação era
*"integração com o sistema atual, especialmente na parte de cadastro"*, e há chamados abertos
sobre **campos duplicados no cadastro** e **valores da ficha que não chegam ao Linx**.

## Marcos da jornada

| Data | Marco | Fonte |
|---|---|---|
| **07/06/2024** | Linha do cliente criada no Notion | base `Mapa de Clientes` |
| **10/06/2024** | 🟢 **Data de ativação do cliente** — único cliente varrido com o campo preenchido | base `Mapa de Clientes` |
| **18/06/2024** | **Kick-off interno** — escopo e dores validados; decidido que **Taís e Sandro** vão a SP; **OKRs gerados com ChatGPT** | página `NK STORE` |
| **19/06/2024** | **Warm-up com o cliente** — **"Passagem de Bastão Oficial de Sales para Ops"** · departamentos confirmados · risco e oportunidade registrados | idem |
| **28/06/2024** | **Kick-off presencial**, 9h30–13h30 — início do mapeamento com o time | idem |
| **05/12/2024** | Primeiro convite aceito — **Nathalia Gomes (TI, `NK - Admin`)** | base `Usuários` |
| **04/12/2024** | **Validação da matriz de permissão** dos perfis `NK - Admin` e `NK - Time` | *Perfil de Usuário e Permissionamentos* |
| **12/12/2024** | 🔴 **Maior onda de onboarding: 8 convites aceitos no mesmo dia** — Estilo, PCP, Compras | base `Usuários` |
| 12 e 16/12/2024 | **Dois convites enviados e nunca aceitos** | idem |
| 08–27/01/2025 | Onda de **Modelagem** (4) e reforço de **PCP** (3) | idem |
| 12–13/02/2025 | Onda de **Estilo** (2) | idem |
| 27/02 · 10/03/2025 | Últimos convites aceitos | idem |
| **10/03/2025** | 🔴 **Primeira e única inativação declarada** — Vanessa Veiga | idem |
| **13/03/2025** | Base de usuários **criada** no Notion — **e nunca mais atualizada** | idem |
| **25/04/2025** | Última edição registrada da página de permissionamentos | idem |
| **Maio/2025** | *NK | Material Gerencial Diretoria* | página `NK STORE` |
| **29/05/2025** | *NK | Dúvidas Pendentes Integração de Escrita* — **frente aberta datada** | idem |
| **11/07/2025** | Última edição da página de permissionamentos | idem |
| **06–29/01/2026** | **30 chamados de 10 pessoas** — **21 ficam abertos** | `Chamados & Atendimentos` |
| **04/08/2026** | Última edição da página do cliente | base `Mapa de Clientes` |

## Entregas comprometidas
| Entrega | Estado |
|---|---|
| Matriz de perfil e permissionamento | ✅ desenhada e validada em **04/12/2024** — ⚠ **divergiu da implantação** |
| Integração de escrita | 🔴 **dúvidas pendentes desde 29/05/2025** |
| Material de treinamento Go Light uFlow | existe (Slides), **não varrido** |
| Material Gerencial Diretoria | existe, **maio/2025**, não varrido |
| Plano de Sucesso do Cliente | existe (Drive), **não varrido** |
| Base de Upload Importação · Ficha de Produto Completo | existem (Sheets), **não varridas** |

## Módulos em uso
`Gestão de Coleção` · `Integração` · `Relatórios` · `Fornecedores`.
**Não contratados:** `Cronograma` · `Aposta` · `Planejamento`.

> ⚠ **`Cronograma` não está contratado** — e a dor 4 das 10 mapeadas na venda era exatamente
> *"visibilidade sobre o calendário de produção e a capacidade de reprogramar atividades em caso
> de atrasos"*. **Vale checar se a dor segue viva.**

## Decisões e restrições registradas
| Decisão / restrição | Fonte | Estado |
|---|---|---|
| **Cliente não cria dado mestre** — 🔴 em novo fornecedor, nova cor, nova grade, nova mp, **inclusive para o Admin** | matriz de permissão | **vigente, por desenho** |
| **`NK - Admin` e `NK - Time` não acessam "Fale com o Suporte"** | idem | **vigente** |
| **`NK - Time` não vê Integração nem Importação** | idem | **vigente** |
| **Admin vê usuários mas sem menu de ação** — *"não pode aparecer os 3 pontinhos"* | idem | validação 04/12 |
| **`Fornecedor` não vê produto, lote, mapa nem custo** | idem | **vigente** |
| **Implantação em ondas** | warm-up 19/06 | acordado |

## Métricas de sucesso definidas
**Declaradas pelo cliente, em *Definições do Projeto*:**
- **Sucesso:** *eliminar retrabalho da equipe* · *reduzir lead time total e das micro operações*
- **Objetivos:** *centralização das informações* · *digitalização dos processos*

> 🟢 **É o único cliente varrido com definição de sucesso escrita** — e **nenhuma das duas é
> medida hoje.** Não há número de retrabalho nem de lead time em nenhuma fonte varrida.

## Próximos passos
1. 🚨 **Rotacionar a credencial do banco de produção** exposta na página — ver
   [`institucional.md`](institucional.md).
2. 🔴 **Confirmar a situação da Larissa Castilho**, Gerente de Projeto marcada `INATIVAR`.
3. 🔴 **Destravar os 21 chamados abertos.**
4. **Reconciliar perfis** — a matriz e a base de usuários usam nomes diferentes.
5. **Resolver as 5 pessoas marcadas `INATIVAR`** — 4 ainda constam como `CONVITE ACEITO`.
6. **Cancelar ou reenviar os 2 convites pendentes** há 21 meses.
7. **Ler *Dúvidas Pendentes Integração de Escrita*** (29/05/2025).
8. **Resolver `Oficina`, `Curadoria` e `Merchandising`** para área canônica.
9. **Medir retrabalho e lead time**, que são a definição de sucesso do cliente.

## Histórico de incidentes / alertas
| Data | Registro | Estado |
|---|---|---|
| 06/01/2026 | **Sistema saiu do ar** | resolvido |
| 09/01/2026 | **Notificações não chegam por e-mail** — `caroline.silva` | **`Em Aberto`** |
| 09/01/2026 | **Valores da ficha de produto não são enviados ao Linx** — `isabely.consul` | **`Em Aberto`** |
| 09/01/2026 | *Forçar integração* — `lais.batista` | fechado |
| 13/01/2026 | **Campos duplicados, cadastrados 2×, preciso corrigir** — `isabely.consul` | **`Em Aberto`** |
| 13 e 20/01/2026 | Instabilidades — `kauane.boska`, `lais.batista` | resolvido / **`Pendente`** |
| 20/01/2026 | **Novo acesso** — `nathalia.gomes` (TI) | **`Não iniciada`** |
| 23–28/01/2026 | **13 chamados em 4 dias**, quase todos `Não iniciada` | **abertos** |
| 29/01/2026 | **Melhoria: subir ao Linx só o custo do tamanho usado** — `carolina.teixeira`; *"Marina vai puxar para conversar"* | **`Em Aberto`** |
| — | 🚨 **Credencial de banco de produção em texto plano na página** | **ação pendente** |

## Observações
- **Risco registrado pela própria uMode no warm-up:** *"Tem séria tendência em assumir mais
  responsabilidades do que conseguem dar vazão"*. **Com 21 chamados abertos, vale reler.**
- **Oportunidade registrada na mesma reunião:** *"Follow Up de Entregas → Pedidos de Compras →
  **uBuy (oportunidade)**"*.
- **IA é canal de fato nesta conta:** o desenho de processo saiu de **Tactiq** e **Gemini** dentro
  de uma reunião; os **OKRs saíram do ChatGPT**, com link salvo na página.
- **30 chamados numa conta de grupo `Médios`** — volume de `Enterprise`, alocação de `Médios`.
- **`expedicao2@nkstore.com.br` é caixa funcional com nome de pessoa** (Nelson Tadeu Alves
  Ferreira). **Caixa compartilhada quebra o vínculo pessoa↔ação** — item para a espec.

## Governança
### Quem pode alterar este documento
Responsável de atendimento + liderança de Atendimento uMode

### Procedência
| Bloco | Fonte | Data |
|---|---|---|
| Kick-offs, dores, definições, risco | Notion — corpo da página `NK STORE` | **varrido 21/09/2026** |
| Datas de convite, inativação, perfis | Notion — base `Usuários` em *Perfil de Usuário e Permissionamentos* | **varrida 21/09/2026** |
| Matriz de permissão | Notion — *Perfil de Usuário e Permissionamentos* | **varrida 21/09/2026** |
| 30 chamados e incidentes | Notion — `Chamados & Atendimentos` | **varrido 21/09/2026** |
| Ativação, receita, módulos, ERP | Notion — base `Mapa de Clientes` | **varrido 21/09/2026** |
