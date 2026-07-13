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
