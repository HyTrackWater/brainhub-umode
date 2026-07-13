# Protocolo · Gestão de Pessoas (ficha individual)

> Operacionaliza a regra já travada em `CONTEXT.md`: "Pessoa interna vive só em `Casa ›
> Pessoas`". Este protocolo define a ficha individual — não confundir com `pessoas.md` de
> cliente, que continua existindo e passa a referenciar a ficha da Casa por vínculo de
> atendimento, em vez de repetir dado.

## Onde vive
Um único registro por pessoa, em `00_Institucional/_pessoas/`. `_pessoas/` é uma 3ª subpasta
fixa da Casa (junto de `_demandas/` e `_rfis/` do lado de cliente) — mesma lógica de
não-duplicação já aplicada a Pessoa interna: vive uma vez, é referenciada por vínculo,
nunca copiada dentro do `pessoas.md` de cada cliente que ela atende.
- Nome do arquivo: nome completo em slug (ex.: `laura-delgado-cardoso.md`).
- Endereçamento: `Casa › Pessoas › [nome]`.

## Duas classes de campo — nunca fundidas
- **Documentável** — vem de fonte real (organograma, CRM "Mapa de Clientes", histórico de
  reuniões/demandas/RFIs): cadeira, área, clientes atendidos, tempo na uMode se conhecido.
  Preenchido pelo agente a partir de varredura, sempre citando a fonte.
- **Personificação** — personalidade, forma de trabalhar, autodescrição, curiosidades. **Nunca
  inferido de documento.** Só entra quando a própria pessoa responde (formulário — ver
  Governança). Até lá, fica `[a preencher]`, nunca um palpite "plausível".

## Anatomia da ficha (campos)

### Identificação
- Nome completo
- Nome preferido / como é chamado(a)
- Email
- Cadeira / cargo atual
- Área (organizacional — uma das 8 Áreas internas de `CONTEXT.md`, quando mapeável; cadeira do
  organograma nem sempre bate 1:1 com Área BrainHub — não forçar encaixe, ver nota abaixo)
- Data de entrada na uMode

### Papel
- Missão da cadeira
- Responsabilidades principais
- Interfaces — com quem trabalha / de quem depende

### Histórico
- Áreas de atuação histórica
- Clientes atuais atendidos
- Clientes atendidos historicamente

### Personificação (formulário — ver Governança)
- Como se descreve
- Personalidade / forma de trabalhar
- O que a diferencia
- Curiosidade / algo pessoal

### Governança
- Fonte dos dados documentáveis (ex.: "organograma v2.2 + CRM Mapa de Clientes, varredura de
  09 jul 2026")
- Quem pode alterar este documento

## Nota: Cadeira (organograma) ≠ Área (BrainHub)
O organograma real da Casa (Design Org & Metas 2026) usa "cadeiras" e diretorias próprias
(CEO, Tecnologia/CTO, Vendas, Marketing, Operações, Produto, Administrativo, Pessoas) —
**não é a mesma lista** das 8 Áreas internas já travadas em `CONTEXT.md` (Comercial,
Atendimento, Produto & Soluções, Dados & IA, Financeiro, Tecnologia, People, Operações). Uma
pessoa pode ter uma "cadeira" clara no organograma sem um mapeamento óbvio para uma Área
BrainHub — nesse caso, o campo `Área (organizacional)` fica `[a preencher]` até alguém decidir
o mapeamento, em vez de forçar um encaixe.

## Como preencher (ordem recomendada)
1. Organograma (`organograma.svg.png` / `.pptx` / `.html`) → cadeira, diretoria, acumulações.
2. CRM "Mapa de Clientes" + histórico de demandas/RFIs/reuniões → clientes atendidos (atuais e
   históricos), papel operacional real.
3. Campos de personificação ficam `[a preencher]` até resposta via formulário — não inventar
   nem aproximar com base em como a pessoa aparece nos documentos.

## Formulário de personificação
Fica fora do BrainHub por enquanto (ferramenta simplificada, ex.: Lovable) — quando
respondido, os campos de "Personificação" desta ficha são atualizados manualmente (ou por
agente, com aprovação) a partir da resposta. Este protocolo não define a ferramenta do
formulário, só o destino final do dado.

## Governança
- Criação/atualização de campos documentáveis → qualquer pessoa autorizada, sempre citando
  fonte.
- Preenchimento de campos de personificação → só a própria pessoa (via formulário) ou alguém
  por ela autorizado.
- Este protocolo → Vinicius Risoléo + CEO.
