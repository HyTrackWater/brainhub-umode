# Tarefa BrainWave · 01 — Esqueleto de navegação

> Use este arquivo como a **segunda mensagem** da sessão, depois de "Leia START.md" já ter sido
> respondido e confirmado. Este documento descreve uma tarefa específica, não é contexto geral
> (isso já está em `BRAINWAVE.md`).

## Antes de começar

1. Declare seu próprio stack técnico e convenções de projeto (framework, como você monta tela,
   onde vive o código) — não presuma que eu sei disso, e eu não vou presumir por você.
2. Confirme: hoje você **não tem acesso de leitura** ao repositório `brainhub-umode` (onde o
   cérebro institucional real vive, em `uMode/`). Isso é esperado nesta etapa — não tente
   contornar, não invente uma forma de acessar. A integração com dado real é uma tarefa futura,
   fora do escopo de hoje.

## O que construir hoje

**Só a casca de navegação.** Nada de dado real, nada de tela de detalhe, nada de criar/editar.
O objetivo é provar a estrutura antes de plugar conteúdo.

1. As **6 abas** de navegação, exatamente como descritas em `BRAINWAVE.md` → "As 6 abas de
   navegação": Instituições, Pessoas, Produtos, Demandas, RFIs, Agentes.
2. Cada aba abre uma tela própria (rota/menu funcionando de verdade — não é só um mockup
   estático). A tela pode estar vazia de dado, mas **não vazia de contexto**: mostre o nome da
   aba e a descrição de uma linha do que ela vai listar (copie a coluna "Lista" da tabela de
   `BRAINWAVE.md` para cada aba) — assim a casca já comunica a intenção, mesmo sem dado.
3. Áreas **não é uma aba de topo** — não crie uma sétima entrada de menu pra ela. Ela é
   navegável só de dentro de Instituições (pode ficar como um placeholder de "entra aqui
   depois" dentro da tela de Instituições — não precisa da navegação aninhada funcionando
   ainda, só o lugar reservado).

## O que não fazer

- Não busque nem invente dado real de cliente, pessoa, produto ou demanda — nenhum. Onde
  precisar de exemplo visual, use algo claramente marcado como placeholder (ex.: "[exemplo]"),
  nunca um nome que pareça dado real.
- Não construa formulário de criação/edição — isso é uma tarefa futura.
- Não decida sozinho nenhuma estrutura que não esteja em `BRAINWAVE.md`. Se faltar alguma
  definição pra fechar a casca (ex.: ordem das abas no menu, ícone de cada uma), escolha algo
  razoável e **liste como decisão sua** no fim da resposta — não deixe implícito.

## Ao terminar

Responda com:
1. O que foi construído (lista curta).
2. Qualquer decisão que você tomou sozinho por falta de definição em `BRAINWAVE.md` (ver acima).
3. Qualquer coisa que ficou ambígua e você quer confirmar antes da próxima tarefa.

Não prossiga para a próxima tarefa (dado real, telas de detalhe, criação/edição) até receber
confirmação.
