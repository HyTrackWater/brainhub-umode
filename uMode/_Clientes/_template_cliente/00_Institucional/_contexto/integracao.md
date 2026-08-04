# [Nome do cliente] · Integração

> Existe apenas para cliente que **tem** integração real — ver `protocolo-gestao-integracao.md`.
> A especificação técnica completa vive no repositório; aqui fica o registro institucional e o
> caminho para ela. Campo sem base no documento do repositório fica `[a preencher]` — nunca
> preenchido por analogia com outro cliente, mesmo que o ERP seja o mesmo.

## Identificação
### Cliente
### ERP / sistema integrado
[tem de concordar com "ERP / Integração" do institucional.md — divergência é pendência, não se
resolve por conta própria]
### Repositório de código
### Documentação de referência
[caminho dos arquivos reais dentro do repositório; se não houver documentação, dizer isso
explicitamente — "existe integração, falta documentação" é diferente de "não existe integração"]
### Status da integração
[Em produção / Em implantação / Descontinuada / [a preencher]]

## Arquitetura
### Direções de integração
[escrita (uMode → sistema do cliente) / leitura (sistema do cliente → uMode) / ambas]
### Mecanismo
[API REST, arquivo/CSV, fila, banco, webhook…]
### Ambiente e execução
[onde roda e como é disparado — serverless, agendamento, fila]

## Escrita (uMode → sistema do cliente)
### O que é enviado
### Gatilho e frequência
### Regras e validações

## Leitura (sistema do cliente → uMode)
### O que é importado
### Gatilho e frequência
### Regras e validações

## Tabelas e endpoints
### Tabelas do ERP mapeadas
[resumo e ponteiro para o documento de tabelas do repositório — não copiar a tabela inteira]
### Endpoints externos utilizados

## Particularidades deste cliente
[o que foge do padrão dos outros clientes do mesmo ERP]

## Auditoria e monitoramento

## Incidentes registrados
| Data | Incidente | Resolução | Fonte |
|---|---|---|---|

## Governança
### Responsável técnico
### Quem pode alterar este documento

## Fontes
### Documentos consultados
