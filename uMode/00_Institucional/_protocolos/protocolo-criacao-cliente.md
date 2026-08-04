# Protocolo · Criação de cliente

> Projetado para execução por agente — nenhuma etapa requer intervenção manual
> além das aprovações explicitamente indicadas.

## Inputs obrigatórios para iniciar
| Campo | Fonte |
|---|---|
| Nome oficial do cliente | Responsável comercial |
| Responsável de atendimento (uMode) | Liderança de Atendimento |
| Áreas ativas no cliente (lista inicial) | Kick-off ou briefing |
| Aliases de áreas (nomes usados pelo cliente) | Kick-off ou briefing |

## Passo 1 · Criar estrutura de pastas
**Executor:** agente
Dentro de `uMode/_Clientes/`, criar pasta com nome oficial do cliente contendo:
`00_Institucional` + 14 áreas canônicas, cada uma com `_contexto/` e `_protocolos/`.

## Passo 2 · Criar e preencher o Institucional
**Executor:** agente (cria) + responsável de atendimento (revisa)
Arquivo: `[Cliente]/00_Institucional/_contexto/institucional.md`
Campos obrigatórios: identidade, operação uMode, aliases de áreas, responsável.
**Aprovação necessária antes do passo 3.**

### Dois campos obrigatórios de identidade (adicionados em 03 ago 2026)
- **`### ID do cliente`** — slug estável, minúsculo, sem acento, derivado do nome no CRM
  (`NK STORE` → `nk-store`). **Nunca muda**, mesmo que o nome comercial mude. É a chave lógica do
  cliente: o nome da pasta passa a ser apenas apresentação. Motivo: antes disso a única chave era o
  nome da pasta, e renomear um cliente quebraria os vínculos de demanda/RFI/pessoa em silêncio
  (medido: 87 referências só em NK STORE). Como o slug normaliza caixa e acento, variações do tipo
  `NK STORE` / `NK Store` deixam de ser um problema — colapsam no mesmo ID.
- **`### Aliases do cliente`** — todos os nomes pelos quais o cliente aparece nas fontes reais
  (CRM, pasta do Drive, títulos de RFI no Notion). Só entram nomes que **não** colapsam no mesmo
  slug — ex.: `Lofty` para Lofty Style, `Lenny` para Lenny Niemeyer, `OFICINA` para Oficina
  Reserva. Serve para reconhecer o mesmo cliente vindo de fonte diferente, na próxima importação.

### Fontes de verdade: uma seção, não um heading por sistema
`## Sistemas e fontes de verdade` tem exatamente dois subcampos: `### Drive de operação` e
`### Outras fontes` (lista livre — Notion, Portal do Cliente, OKRs, material de apresentação, grupo
de WhatsApp, base de chamados). **Não criar um heading por sistema** — foi exatamente a divergência
que Luiza Barcelos carregava (`### ERP` + `### Notion`), resolvida em 03 ago 2026. ERP/integração
não entra aqui: vive em `## Operação uMode → ### ERP / Integração`.

## Passo 3 · Criar contextos de área
**Executor:** agente
`contexto-area.md` em cada área ativa, com produto conectado preenchido.

## Passo 4 · Criar registro de pessoas por área
**Executor:** agente (cria) + responsável de atendimento (preenche)
`pessoas.md` em cada área ativa.

## Passo 5 · Validação e ativação
**Checklist:**
- [ ] Estrutura de pastas correta
- [ ] `institucional.md` preenchido e aprovado
- [ ] `contexto-area.md` em todas as áreas ativas
- [ ] `pessoas.md` em todas as áreas ativas
- [ ] Aliases mapeados · Responsável uMode registrado

## Governança
Passos 1, 3, 4 → agente. Aprovação passos 2 e 5 → responsável de atendimento + liderança.
