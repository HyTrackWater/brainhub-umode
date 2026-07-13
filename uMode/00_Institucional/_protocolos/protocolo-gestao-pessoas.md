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

## Três classes de campo — nunca fundidas
- **Documentável** — vem de fonte real (organograma, CRM "Mapa de Clientes", histórico de
  reuniões/demandas/RFIs): cadeira, área, clientes atendidos, tempo na uMode se conhecido.
  Preenchido pelo agente a partir de varredura, sempre citando a fonte.
- **Personificação** — personalidade, forma de trabalhar, autodescrição, curiosidades. **Nunca
  inferido de documento.** Só entra quando a própria pessoa responde (formulário — ver
  Governança). Até lá, fica `[a preencher]`, nunca um palpite "plausível".
- **Competências** (novo em 13 jul 2026) — experiência anterior, skills, cursos, ferramentas
  que domina. Documentável só quando há fonte real citada (CV, LinkedIn, certificado) **ou**
  resposta da própria pessoa via formulário — nunca inferido do cargo/cadeira. Existe pra virar
  fonte de busca de conhecimento interno ("quem sabe sobre X"), não só registro de organograma.

## Anatomia da ficha (campos)

### Identificação
- Foto (novo em 13 jul 2026, pedido explícito pra tela Home — URL/referência do arquivo,
  vazio até upload real; não é campo de personificação, mas também nunca inferido/inventado)
- Nome completo
- Nome preferido / como é chamado(a)
- Email
- Cadeira / cargo atual
- Nível HIC (novo em 13 jul 2026) — representa a jornada de aprendizagem e uso de
  ferramentas/conhecimento em IA do colaborador (conceito HIC já definido em `CONTEXT.md` →
  Taxonomia: "High Individual Contributor, colaborador potencializado por IA"). **Só o campo
  foi criado agora — a escala/critério de triagem (quantos níveis, o que qualifica cada um)
  ainda não foi definida.** Fica `[a preencher]` até essa triagem existir; não inventar uma
  escala provisória.
- Área (organizacional — uma das 8 Áreas internas de `CONTEXT.md`, quando mapeável; cadeira do
  organograma nem sempre bate 1:1 com Área BrainHub — não forçar encaixe, ver nota abaixo)
- Data de entrada na uMode
- Status na uMode (Ativo / Inativo) + Data de saída da uMode, condicional a Inativo — novo em
  13 jul 2026, achado real: Andrea Goulart Holmer dos Santos saiu do time e não havia como
  registrar isso. Quando uma pessoa fica Inativa, `Clientes atuais atendidos` (Histórico) some
  daquele campo e migra pra `Clientes atendidos historicamente` — ela deixa de atender de
  verdade, mesmo que o registro documental permaneça.

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

### Competências (novo em 13 jul 2026)
- Experiência profissional anterior
- Skills / habilidades técnicas
- Cursos e certificações
- Ferramentas e plataformas que domina

Terceira classe de campo, distinta das outras duas — preenchida **só com fonte real citada**:
currículo/CV, LinkedIn, certificado, ou resposta da própria pessoa via formulário (mesmo canal
da Personificação). Nunca inferido do cargo/cadeira, nem aproximado a partir de como a pessoa
aparece em demanda/RFI/reunião — isso mostra o que ela *fez na uMode*, não o que ela *sabe*.

**Propósito explícito** (motivo pelo qual essa seção existe): quando as fichas estiverem
interligadas com Demanda/Produto/Área, essa seção vira a fonte pra responder "pra quem eu
pergunto sobre X" e "quem tem a skill Y disponível pra esse projeto" — um diretório de
conhecimento interno, não só de organograma. Isso é intenção de produto registrada agora;
nenhuma tela ou busca foi construída ainda.

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
