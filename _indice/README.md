# _indice/ — índice derivado do cérebro

> **Gerado por `scripts/gen-indice.ps1` em 03 ago 2026. Não editar a mão.**
> O MD é a fonte de verdade; este índice é derivado dele. Se um número aqui divergir do MD,
> o MD está certo e o índice está velho — basta regerar.

## Por que existe
A auditoria de 03 ago 2026 (`uMode/00_Institucional/_contexto/_auditoria-indexacao.md`)
mostrou que a indexação já funciona por convenção — a posição de heading é um contrato
cumprido em 100% dos arquivos. O que faltava era **materializar** isso: sem o índice,
qualquer pergunta relacional exige varrer 1.292 arquivos.

Decisão explícita: **índice derivado, não frontmatter.** Frontmatter nos MDs criaria duas
fontes de verdade para o mesmo campo (o heading e o metadado), com risco real de divergirem.
Aqui a duplicação é assumida e descartável — regenerar reconcilia sempre.

## Tabelas

| Arquivo | Linhas | Chave | Liga com |
|---|---|---|---|
| `clientes.csv` | 46 | `client_id` | é a chave de tudo abaixo |
| `integracoes.csv` | 11 | `client_id` | `rfis_citadas` resolve RFI do CX Hub → nosso ID |
| `demandas.csv` | 997 | `demanda_id` | `client_id` · `rfi_id` · `id_legado` (CX Hub) |
| `rfis.csv` | 85 | `rfi_id` | `client_id` · `id_legado` (Notion) |
| `pessoas.csv` | 13 | `pessoa_id` | `clientes` (lista de `client_id`) |
| `produtos.csv` | 16 | `produto_id` | `area_cliente` · `upstream`/`downstream` (outros produtos) |

`client_id` é o slug estável de `institucional.md → Identidade → ID do cliente`. **Não é o
nome da pasta** — justamente para que renomear um cliente não quebre vínculo nenhum.

## O que o índice já responde (e o que ainda não)

- ✅ demanda → cliente: 997 de 997
- ✅ demanda → RFI: 44 vínculos resolvidos
- ✅ RFI com narrativa real: 84 de 85
- ✅ pessoa da Casa → clientes atendidos: 13 pessoas com vínculo
- ✅ integração → cliente: 11 clientes com `integracao.md`, 10 com documento técnico lido
- ✅ integração → RFI (via `ID legado`): 1 integração(ões) citam RFI, e o número do CX Hub resolve pro nosso ID
  — **é o primeiro vínculo do cérebro cujo eixo não é cliente**
- ❌ demanda → **Área organizacional**: 997 de 997 sem `Destino` — o eixo Área
  continua vazio, e nenhum índice resolve isso: é conteúdo que falta, não estrutura
  (ver `_pendencias-gerais.md` item 39)

## Como regenerar

```
powershell -File scripts/gen-indice.ps1
```
