---
aliases:
  - "Prompt de extração do Notion via Claude in Chrome"
tags:
  - tipo/protocolo
  - casa
---
# Prompt de extração do Notion via Claude in Chrome

> **Classe: `TEMPLATE`.** É um prompt para colar no Claude in Chrome, não um documento de leitura.
>
> **Ideia do Vinícius em 22 set 2026**, textual: *"se precisar montar um prompt para, via Claude
> Chrome, indicar todos os caminhos que precisa, com as instruções de abrir todos os blocos que
> forem possíveis, para então gerar arquivos md de cada caminho, organizar por cliente, zipar
> tudo e depois te trazer — sem problemas... Só não quero que tenhamos a sensação de não ter
> algum tipo de informação num destino e na verdade ele estar por lá."*

## 0 · Por que isto existe

O conector de Notion que eu uso **lê a maior parte, mas não tudo**. Já foram dois tipos de perda:

| O que perde | Caso real | Como sei |
|---|---|---|
| **Bloco que não renderiza** | 17 blocos na Luiza Barcelos escondiam **o único Representante Legal da conta** e o cargo do Gerente de Inovação e Tecnologia | o Vinícius copiou e colou, e o conteúdo apareceu |
| **Incorporação do Drive** | `Plano de Sucesso do Cliente` em **3 clientes** — NK STORE, Cambos, Luiza Barcelos | vem como bloco vazio nos três |
| **Acesso negado de verdade** | `Fornecedores da Caedu` — **404** | único caso real de permissão na carteira |

🔴 **O navegador não tem essa limitação: ele vê o que um humano vê.**

## 1 · O prompt — copiar daqui para baixo

```
Você vai extrair páginas do Notion da uMode para arquivos Markdown. É trabalho de
LEITURA. Não edite, não comente, não mova e não apague nada no Notion.

PARA CADA URL DA LISTA ABAIXO:

1. Abra a página.
2. EXPANDA TUDO antes de ler:
   - todo toggle fechado (as setinhas ▸), inclusive toggles dentro de toggles;
   - todo bloco "synced" (conteúdo sincronizado de outra página);
   - toda tabela recolhida e todo database inline — se houver paginação
     ("Load more" / "Carregar mais"), clique até o fim;
   - todo callout e toda coluna.
3. Copie o conteúdo COMPLETO da página, incluindo:
   - o texto de cada linha, com a hierarquia de indentação preservada;
   - NOMES, CARGOS, E-MAILS e TELEFONES que aparecerem;
   - tabelas inteiras, com cabeçalho;
   - o texto de cada link e o endereço dele;
   - o nome de toda sub-página listada na página (mesmo sem abrir a sub-página).
4. Salve como um arquivo .md com este nome exato:
      <NOME-DO-CLIENTE>__<titulo-da-pagina>.md
   trocando espaço por hífen e removendo acento do nome do arquivo.
   Exemplo: Luiza-Barcelos__Warm-Up-Cliente.md
5. No TOPO de cada arquivo, escreva estas quatro linhas:
      FONTE: <a URL completa>
      TITULO: <o título da página como aparece no Notion>
      CLIENTE: <o nome do cliente>
      EXTRAIDO_EM: <data de hoje>

REGRAS QUE NÃO MUDAM:
- Se um bloco não abrir ou der erro, escreva no arquivo, na posição dele:
      [NAO-ABRIU: <o que aparece na tela>]
  NÃO pule em silêncio. Bloco que não abriu é informação.
- Se a página tiver sub-páginas, liste os TÍTULOS e os LINKS delas ao final, sob
  o título "SUB-PAGINAS", e siga para a próxima URL. Não entre nelas nesta
  primeira passada.
- Se a página pedir permissão ou der 404, crie o arquivo mesmo assim, só com o
  cabeçalho e a linha [SEM-ACESSO].

AO FINAL:
- Organize os arquivos em uma pasta por cliente, com o nome do cliente.
- Compacte tudo num único .zip chamado notion-clientes-<data>.zip.
```

## 2 · A lista de URLs — as 50 páginas de cliente

> **Ordem proposital: quem está vivo primeiro.** Se o trabalho for interrompido no meio, o que
> importa mais já terá sido extraído.

### Grupo 1 · `Ongoing` — 9 contas, a operação viva

| Cliente | URL |
|---|---|
| Cambos | `https://www.notion.so/d6d48327e33b4105b67b9db4dbb55af1` |
| Lofty Style | `https://www.notion.so/293c8829d81c44d9ab8360ae66d24aab` |
| Luiza Barcelos | `https://www.notion.so/b0c819c0bda449528d9d984b3200f07f` |
| NK STORE | `https://www.notion.so/0f24dfbef0ae43bbba528218d940b7ed` |
| NV | `https://www.notion.so/c03ae4eca8ff4260a889b660803b4e26` |
| Oficina Reserva | `https://www.notion.so/a27d12dd1749485488ea17df5dd253ac` |
| Puket | `https://www.notion.so/aae6d54c5f854cc9b890f8c0c120bf0a` |
| Reserva | `https://www.notion.so/1be195276d794e1d98a35cddd9d2a508` |
| VIX | `https://www.notion.so/70a10ec2756f4842a04cb12675a09d22` |

### Grupo 2 · `Onboarding` e `Operação Assistida` — 4 contas

| Cliente | URL |
|---|---|
| **Caedu** | `https://www.notion.so/275bd52e58df49078f2f3b6dc76a4755` |
| Loungerie | `https://www.notion.so/345b1d38e7688051a7d1f420d8d7df67` |
| Moda Objetiva | `https://www.notion.so/295b1d38e76880118addca9ad3e85807` |
| Osklen | `https://www.notion.so/6463bb11ee3841b8b948d18b5a71b4d7` |

### Grupo 3 · `Pré Onboarding` e `Sem CS` — 9 contas

| Cliente | URL |
|---|---|
| Arezzo | `https://www.notion.so/345b1d38e7688009b12cf10c9136598e` |
| Hering | `https://www.notion.so/29ab1d38e76880688d63d3efa50f5a36` |
| Baw | `https://www.notion.so/6c36c6a40d904f2fb65ebc1f09933ad4` |
| Camys | `https://www.notion.so/cf4bc0de73ca4102b8484af27a378f4f` |
| Cavallari | `https://www.notion.so/98d4eceeb00b43ec9b89ceff500a8ab5` |
| Mondepars | `https://www.notion.so/31eb1d38e76880f782cde2f695cd43e7` |
| Studio Minah | `https://www.notion.so/ec7653a9d28f49a3998285b3a421ae50` |
| TDC | `https://www.notion.so/d55dc1546298489c84585bedca8c5775` |
| Ton Age | `https://www.notion.so/bc55f907742c443d9e897f50b1d06a73` |

### Grupo 4 · `Churn` — 20 contas, história que ainda ensina

| Cliente | URL |
|---|---|
| 4takes | `https://www.notion.so/c9fc56ab0eaf4d689f18ab615cc59ed6` |
| Básico&Co | `https://www.notion.so/0d33bc21acb0434f9a4a18693446b369` |
| Colmeia | `https://www.notion.so/51b75c831bf4478bb07c9097f7401e3d` |
| DRO | `https://www.notion.so/e508e7111bd14988947e1182de610d31` |
| Estrela | `https://www.notion.so/21179440e5b848b2b0eff0ff77717d86` |
| Highstil | `https://www.notion.so/c856575a8bb74628aeca8c8f9f8fcf1b` |
| Hyperlocal | `https://www.notion.so/f2c38fd5b53446968c2b3c1bb5224283` |
| Laces | `https://www.notion.so/7676f432d63c4d109e4aad275d98837b` |
| Ladeira Bijuterias | `https://www.notion.so/fc534f508cab4cd784640f06761522ad` |
| Lenny Niemeyer | `https://www.notion.so/b3aad92958894c71b1e1ddd096db52ed` |
| Lojão do Brás | `https://www.notion.so/c72d0dac58bd466e9a165e2db56cfd8d` |
| NTK | `https://www.notion.so/dd720bcdadc64156a1092aa8eb8c056e` |
| Phos | `https://www.notion.so/2f8b1d38e7688005b97ed4806230f91c` |
| Plie | `https://www.notion.so/1d2b1d38e76880bf91f9d4fa8ffdc478` |
| Recco | `https://www.notion.so/1c63ebd232894596b911359ca99cfb60` |
| Ricardo Almeida | `https://www.notion.so/201b1d38e76880e38289cdd3e660476f` |
| Seven Global | `https://www.notion.so/533c7f6f444e45a0ba70a452bced6f3e` |
| Studio Z | `https://www.notion.so/34e20142793944e985de595d6f2e1adb` |
| Texneo | `https://www.notion.so/74eee2f6b01548eeb436adfc25b84da4` |
| Vivara | `https://www.notion.so/0328d43ad54447e08ccfd5b7256e24fe` |

### Grupo 5 · `Inativo` — 8, menor valor

`Agua de Coco` `302b1d38e768804ab010e4bbb961c2fd` · `Fornecedores`
`302b1d38e768805681baed876fc30480` · `La Moda` `302b1d38e76880afa590de7851dc12a4` ·
`Paloma concept` `2e2b1d38e76880b29effe4cf4f73bd78` · `Pampili Mini`
`f8b27518b3db48e2bb7c892a83b810e4` · `Susie Modas` `2e7b1d38e768806ca7a4c841dba4c83a` ·
`uMode` `d777c7bd6bee41afa8c767bcdeb1eeed` · `. Página Cliente [Template]`
`197b1d38e768807e8d5dd5a154767961`

## 3 · Sub-páginas que já sei que existem e nunca foram abertas

> **Só depois da primeira passada.** A extração acima já traz os títulos e links de todas as
> sub-páginas — **e aí a lista real substitui esta, que é só o que eu vi de relance.**

| Cliente | Sub-página | Por que importa |
|---|---|---|
| **CAEDU** | `Reuniões com o cliente` | 🔴 **~47 atas de weekly**, 24/04/2024 → 16/09/2025 |
| **CAEDU** | `Ficha de Produto` · `Playbooks` · `Miro Regras e restrições` · `Onboarding > Ongoing` · `Perfis de Usuario` | 56 sub-páginas no total, 2 abertas |
| **Luiza Barcelos** | `Relatório de Incidente — 2025/08/08` | 🔴 **único registro de incidente com cliente do corpus** |
| **Luiza Barcelos** | 8 páginas de regra datadas | documentação de regra mais disciplinada da carteira |
| **VIX · Lofty Style · Oficina Reserva · Cambos · Luiza Barcelos** | `Perfil de Usuário e Permissionamentos` | **é onde o vínculo pessoa↔área mora** — só a da VIX foi aberta |
| **Osklen · Lofty Style** | pesquisas de **CSat** | 4 pesquisas, nenhuma lida |
| **Puket** | `Passada de bastão` | único handover de atendimento da carteira |
| **Reserva** | `Playbooks` · `Onboarding > Ongoing` · `Termo de abertura — Sourcing` · atas de 2 visitas presenciais | 10 sub-páginas |
| **Cambos** | `Playbook Cambos \| Treinamento > IA + Doc Laura` | primeira documentação homologada com IA |

## 4 · 🔴 O que vem junto e NÃO pode entrar no corpus

A extração **vai trazer dado `T0`** — já sei de pelo menos três casos:

| O quê | Onde |
|---|---|
| 🚨 **Credencial de produção do Linx** | NK STORE, `Documentos › Conexão com Linx` |
| 🚨 **Senha do site de documentação** | Lofty Style, `Documentação/Regras` |
| 🔴 **CPF e telefone pessoal** | Luiza Barcelos e NK STORE, blocos de representante legal |

**Quando o zip chegar, o que eu faço com isso:**

- **e-mail corporativo** → entra, é `T2` e é a chave de identidade;
- **telefone, CPF, senha, token** → 🔴 **não entram por valor.** Registro que existem e **onde**;
- **valor de contrato, preço, margem** → `T1`, fica só no `_contexto/` daquele cliente.

⚠ **O zip em si é `T0` enquanto existir.** Não versionar no repositório, não subir para o Drive
compartilhado. **Ler, extrair o que é `T2`, e apagar.**

## 5 · O que fazer quando o zip chegar

1. Descompactar **fora do repositório** — em `scratchpad`, não em `uMode/`.
2. Para cada arquivo, **comparar com a § 3 do `_pendencias-e-fontes.md` daquele cliente**: o que
   já estava varrido não se relê.
3. **Procurar `[NAO-ABRIU]` e `[SEM-ACESSO]` primeiro** — é o que o navegador também não
   alcançou, e vai para a **§ 1-bis** do cliente.
4. Extrair pessoa, área, ferramenta e demanda **pelos geradores**, nunca à mão.
5. **Rodar os quatro rituais** e só então commitar.
6. 🔴 **Apagar o zip e os .md extraídos.** O corpus fica com o que é `T2`; o bruto não fica.

## Governança

### Quem pode alterar este documento
Vinícius. **A lista de URLs sai da base `Mapa de Clientes` e se regera** — se um cliente entrar
ou sair, esta tabela envelhece.

### Quando usar
🔴 **Quando a dúvida for "será que tem algo nesse destino que eu não estou vendo?"** — que é
exatamente a pergunta que ele fez. **Para varredura de rotina, o conector basta.**
