# Prompt de execução — BrainWave · Tarefa 03: abas "uMode" e "Clientes" (Instituições, Áreas, Subáreas, Pessoas)

> Texto pronto pra colar direto no BrainWave, como está, sem edição. Autocontido — o BrainWave
> não tem acesso a este repositório nem a nenhum outro arquivo, então tudo que ele precisa está
> aqui dentro. Depende das Tarefas 01 (esqueleto de navegação) e 02 (Home) já estarem prontas.

---

Esta tarefa **altera** a casca de navegação da Tarefa 01 e **adiciona** telas novas dentro
dela. Não é só acréscimo — duas abas do menu principal deixam de existir como estão hoje.

## O que muda no menu principal

Remova as abas **"Instituições"** e **"Pessoas"** como abas independentes. No lugar delas,
crie duas novas abas:

1. **uMode**
2. **Clientes**

As abas **Produtos**, **Demandas**, **RFIs** e **Agentes** continuam exatamente como estão —
não mexa nelas.

## Por que essa mudança

A uMode (a empresa) e cada Cliente têm a mesma estrutura interna fixa: Instituição → Áreas →
Subáreas → Pessoas. Em vez de "Pessoas" ser uma aba solta e "Instituições" outra, cada uma
dessas duas abas novas (uMode / Clientes) organiza essa estrutura por dentro, em 4 sub-abas:

**Instituições · Áreas · Subáreas · Pessoas**

Essas 4 sub-abas são **idênticas nas duas telas** (uMode e Clientes) — só o conteúdo muda.

---

## Aba "uMode" (a Casa uMode — é uma instituição só)

### Sub-aba "Instituições"
Mostra só 1 cartão: **"uMode"**. Ao clicar, abre um cadastro com estas seções (algumas vão vir
vazias — mostre normalmente, sem quebrar):

- Identidade: Quem somos · O que fazemos · Para quem fazemos
- Posicionamento: Tese central · Diferenciais · Proposta de valor
- Voz e tom: Como nos comunicamos · O que evitamos
- Taxonomia: Termos próprios
- Contexto crítico: O pivot (tese central da empresa hoje) · De onde veio o pivot · Dogfooding
  (dados reais da própria operação) · O "Sistema Operacional uMode"
- Fontes de verdade: Onde vive o dado oficial
- Governança: Quem pode alterar este documento · Frequência de revisão

### Sub-aba "Áreas"
Mostra 8 cartões, um por área interna da uMode: **Institucional, Comercial, Atendimento,
Produto e Soluções, Dados e IA, Financeiro, Tecnologia, People, Operações**.

Ao clicar em um cartão, abre um cadastro com estas seções:
- O que esta área faz
- Com quem se relaciona (interno e externo)
- Entregas e responsabilidades
- Padrões operacionais: Como trabalhamos · O que não fazemos
- Vocabulário da área: Termos específicos
- Fontes e referências: Documentos que esta área consome · Documentos que esta área produz
- Governança: Responsável pela área · Quem pode alterar este documento

### Sub-aba "Subáreas"
Adicione a sub-aba, mas **desabilitada** (não clicável, sem conteúdo). Ainda não existe
estrutura de dado pra Subáreas.

### Sub-aba "Pessoas"
Mostra um cartão por pessoa do time interno da uMode. Cada cartão traz:
- Nome
- Email
- Área de atuação (uma das 8 áreas acima)

Não construa uma tela de detalhe da pessoa nesta tarefa — o clique no cartão pode ficar
reservado (sem ação ainda). Isso fica pra uma próxima etapa.

---

## Aba "Clientes" (réplica da estrutura acima, para cada cliente)

### Sub-aba "Instituições"
Mostra 1 cartão por cliente (hoje: 4 — nomes de exemplo, não use nome real de cliente:
"[exemplo] Cliente A", "[exemplo] Cliente B", "[exemplo] Cliente C", "[exemplo] Cliente D").

Ao clicar em um cartão de cliente, abre o cadastro dele com estas seções:
- Identidade: Quem são · O que fazem · Para quem fazem
- Posicionamento: Segmento · Receita anual · Grupo de segmentação uMode
- Operação uMode: Status atual · Data de ativação · Módulos contratados · ERP/Integração ·
  Responsável de atendimento (uMode)
- Aliases de áreas: Mapeamento alias → canônico
- Sistemas e fontes de verdade: Drive de operação
- Contexto crítico
- Governança: Responsável de atendimento (uMode) · Quem pode alterar este documento

**Importante:** ao clicar num cliente aqui, ele passa a ser o "cliente ativo" da aba Clientes —
as sub-abas Áreas e Pessoas abaixo passam a mostrar o conteúdo *daquele* cliente até que outro
seja selecionado. Deixe visível, o tempo todo, qual cliente está ativo (ex.: um rótulo fixo no
topo da aba).

### Sub-aba "Áreas"
Mostra 14 cartões — as áreas canônicas de cliente: **Planejamento, Estilo/Criação,
Desenvolvimento de Coleção, Qualidade, PCP, Compras/Supply/Sourcing, Logística/CD,
E-commerce/Cadastro, Comercial/Vendas, Marketing, Financeiro, Design, Modelagem, Engenharia** —
sempre relativas ao cliente ativo escolhido na sub-aba Instituições.

Ao clicar em um cartão, abre o cadastro com as mesmas seções descritas acima para Área (O que
esta área faz · Com quem se relaciona · Entregas e responsabilidades · Padrões operacionais ·
Vocabulário da área · Fontes e referências · Governança). **A maioria vai vir com "[a
preencher]" em quase tudo — isso é esperado, não é erro seu:** hoje nenhum cliente tem esse
cadastro de área totalmente preenchido ainda. Mostre o estado vazio de forma clara, sem
quebrar o layout.

### Sub-aba "Subáreas"
Mesma regra da aba uMode: presente, porém desabilitada.

### Sub-aba "Pessoas"
Mostra um cartão por pessoa do time do cliente ativo. Cada cartão traz:
- Nome
- Email (pode vir vazio — mostre "[a preencher]" em vez de quebrar)
- Área de atuação (uma das 14 áreas acima)

Mesma regra da aba uMode: sem tela de detalhe por enquanto, clique reservado.

---

## Regras para esta entrega

- Ainda não construa formulário de criação ou edição — nem para Instituição, Área, nem Pessoa.
  Isso é só cadastro/visualização.
- Não use nenhum nome real de cliente, pessoa ou dado de negócio. Use "[exemplo]" nos poucos
  lugares onde é preciso preencher algo pra tela não ficar vazia.
- A tela precisa lidar bem com campo vazio/"[a preencher]" em qualquer seção — a maior parte do
  dado real que vai entrar depois está incompleta, principalmente em Áreas.
- Reaproveite os componentes visuais que você já criou nas Tarefas 01 e 02 (cartão, navegação,
  estado vazio) em vez de criar um padrão novo do zero.
- Siga as convenções que você já usa neste projeto — não mude framework nem padrão de código.

**Ao terminar, me diga:**
1. O que foi construído.
2. Qualquer decisão que você tomou sozinho onde eu não te dei detalhe (ex.: como fica o rótulo
   de "cliente ativo", layout dos cartões, ícone de cada sub-aba).
3. Qualquer dúvida antes de eu pedir a próxima etapa.

Não avance para dado real, tela de detalhe de pessoa, ou formulário de criação/edição até eu
confirmar esta etapa.

---

## Resultado

[a preencher — Vinicius roda o prompt acima no BrainWave e traz o resultado de volta pra cá:
o que foi construído, decisões que o BrainWave tomou sozinho, dúvidas levantadas. Até isso
acontecer, esta tarefa está registrada como enviada, não como concluída.]

### Status
Enviado — aguardando resultado.
