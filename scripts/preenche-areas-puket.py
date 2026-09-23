# -*- coding: utf-8 -*-
u"""
preenche-areas-puket.py - preenche as 14 areas da Puket, que estavam TODAS
vazias (11-12 `[a preencher]` cada, so boilerplate).

FONTE. `Mapeamento de Conta - Puket`, abril/2025 v1.0, em
`Operacao de Clientes / Area de CX / Documentacao CX / Mapeamento de Contas`.

RESSALVA DE PROCEDENCIA, E ELA IMPORTA. O documento se declara
"seguindo analise do Chat GPT" e "exemplo de documento... a ideia e ILUSTRAR
como os dados reais podem ser organizados". Ou seja: e SINTESE DE IA sobre
tres transcricoes reais (26/02, 06/03 e 13/03 de 2025), assinada por Rafael.

Nao e fonte bruta e nao pode ser tratada como se fosse. Cada bloco aqui leva
a marca da origem, e o que vier de transcricao continua valendo mais. Foi
por confundir sintese com fonte que ja erramos antes.

O QUE COBRE. 13 das 14 areas canonicas. `10_Marketing` NAO e citada em
nenhum ponto do documento - fica como esta, e isso e dado.
"""
import io, os, sys, codecs

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(RAIZ, u"uMode", u"_Clientes", u"Puket")

F = u"`Mapeamento de Conta — Puket`, abril/2025"
AVISO = (u"\n\n⚠ **Procedência:** %s — **síntese de IA sobre três transcrições reais** "
         u"(26/02, 06/03 e 13/03 de 2025), assinada por Rafael. **Não é fonte bruta.**" % F)

CONTEUDO = {
 u"12_Design": {
  u"O que esta área faz": u"""**Define as estampas da coleção** — personagens e temas — e cria o *guide* correspondente.

> *"Design e Estilo definem as estampas (personagens/temas). No sistema, criam 'pasta' ou 'branch' de guide."* — § 4.2.1

\U0001F534 **E trabalha majoritariamente FORA do uMode:**
> *"Ferramentas: **Email + Pasta em Drive (fora do uMode)**; abastecimento parcial no uMode."* — § 4.2.1
> *"...pois **design faz aquarela fora do sistema**."* — § 4.2.3""" + AVISO,

  u"Como trabalham": u"""- O guide nasce como **pasta ou branch** no sistema, com `Nome do Guide` em texto livre.
- O primeiro upload de imagem é descrito como **inconsistente** (§ 4.2.1).
- A arte final chega à ficha técnica como **anexo parcial**, porque a aquarela é feita fora (§ 4.2.3).""",

  u"O que não fazem": u"""- \U0001F534 **Não registram prazo de aprovação no sistema:**
> *"Gargalo: **falta de prazo amarrado no sistema**, então não há alerta sobre atraso de aprovação."* — § 4.2.1
- \U0001F534 **Não registram as idas e voltas da arte:** *"Falta de controle sobre quantas vezes a arte vai e volta do design"* (§ 4.2.4).""",
 },

 u"02_Estilo-Criacao": {
  u"O que esta área faz": u"""**Responde pelas imagens e artes na ficha técnica**, junto com Design na definição das estampas.

> *"Responsáveis: **Estilo (imagens, artes)**, Modelagem (medidas), Produto (custos)."* — § 4.2.3

\U0001F534 **A dor central da conta está aqui — aprovação fora do sistema:**
> *"Um dos pontos-chave, porém **pouco utilizado no uMode**. O time troca e-mails, faz **PPTs de 100 páginas**, mas **não registra no sistema as aprovações**."* — § 4.2.4
> *"A automação para criar 'Aprovação Piloto' **existe, mas não é alimentada**."*""" + AVISO,

  u"O que não fazem": u"""- \U0001F534 **Não registram aprovação de arte nem de piloto no uMode** — usam e-mail e apresentação (§ 4.2.4).
- ⚠ **Há ação aberta no roadmap para mudar isso:** *"Treinamento 'Aprovações de Piloto'"*, responsável **Time Estilo + uMode**, prazo previsto de **2 semanas** (§ 5.2).""",
 },

 u"03_Desenvolvimento-de-Colecao": {
  u"O que esta área faz": u"""**Faz a subida do esqueleto do produto e responde pelos custos na ficha técnica.**

> *"Em planilha de importação, cadastram **em massa** (preço, cor, linha, ncm, etc.). Responsáveis: **Time de Produto (Cátia ou assistentes)**. Ferramentas: Google Sheets + Import do uMode; Integração com Linx."* — § 4.2.2

\U0001F534 **A planilha de esqueleto tem 37 campos** (§ 2.2), e as validações são condicionais:
> *"`Cor` — se 'Importado', cor obrigatória; `Composição` — **se 'Linha = Meias' o campo é obrigatório**."* — § 4.2.2""" + AVISO,

  u"Entregas e responsabilidades": u"""| Entrega | Validação que a controla |
|---|---|
| Esqueleto do produto importado | planilha de 37 campos, importada em lote |
| Composição preenchida | **obrigatória antes de gerar código Linx** (§ 4.2.3) |
| Custo na ficha técnica | responsável: Produto (§ 4.2.3) |""",

  u"O que não fazem": u"""- \U0001F534 **A dor registrada é de padronização, não de processo:**
> *"**Falta de padronização de cor e ncm** gera retrabalho e suporte."* — § 4.2.2""",
 },

 u"13_Modelagem": {
  u"O que esta área faz": u"""**Responde pela tabela de medidas na ficha técnica.**

> *"Responsáveis: Estilo (imagens, artes), **Modelagem (medidas)**, Produto (custos)."* — § 4.2.3

\U0001F534 **E o campo existe e não é usado:**
> *"`Tabelas de Medidas` (**Rodrigo, Modelagem**) — **não é usado consistentemente**."* — § 4.2.3

⚠ **A aprovação de modelagem é uma das 6 etapas formais de aprovação da conta** (`Mapeamento de Conta Puket — segundo Notion`, 21/03/2025).""" + AVISO,
 },

 u"04_Qualidade": {
  u"O que esta área faz": u"""**Responde pela aprovação de amostras e da peça piloto.**

⚠ **A conta tem seis níveis formais de aprovação**, e dois são desta área — *aprovação de modelagem* e *aprovação de peça piloto*:

> *"Sistema de aprovação estruturado em 6 etapas principais: estampa corrida · estampas localizadas · tecidos sólidos · aviamentos · modelagem · **peça piloto**."*
> — `Mapeamento de Conta Puket — segundo Notion`, 21/03/2025

\U0001F534 **Nenhuma delas é registrada no sistema hoje** (§ 4.2.4 do mapeamento de abril).""" + AVISO,
 },

 u"06_Compras-Supply-Sourcing": {
  u"O que esta área faz": u"""**Responde pela cotação e aprovação de custos**, última das oito etapas de desenvolvimento:

> *"8. **Cotação e Aprovação de Custos**."* — `Mapeamento de Conta Puket — segundo Notion`, 21/03/2025

⚠ **Duas das seis aprovações formais são de insumo:** *aprovação de tecidos sólidos* e *aprovação de aviamentos* (mesma fonte).""" + AVISO,
 },

 u"11_Financeiro": {
  u"O que esta área faz": u"""\U0001F534 **A Controladoria participa do fluxo de produto — e é a única menção de área financeira na conta:**

> *"`NCM e Fiscal` (**Controladoria confere**)."* — § 4.2.5 *Integração e Fechamento*

⚠ **O custo entra pela ficha técnica, sob responsabilidade de Produto, não do Financeiro** (§ 4.2.3).

\U0001F534 **`custo estimado` está entre os campos apontados como subutilizados** (§ 1, Principais Achados).""" + AVISO,
 },

 u"07_Logistica-CD": {
  u"O que esta área faz": u"""\U0001F534 **A logística de importação aparece nomeada, e com um instrumento específico em teste:**

> *"**DUIMP**: está em teste. É uma declaração que permitirá **adiantar o recebimento de produtos importados da China nos portos**, antes dos trâmites burocráticos."* — § 4.2.5

⚠ **A distribuição é definida por campos da ficha:**
> *"Campos de '**Envio loja**', '**Envio site**', '**Envio atacado**' como obrigatórios para definir a distribuição e geração de NFs."* — § 4.2.3""" + AVISO,
 },

 u"14_Engenharia": {
  u"O que esta área faz": u"""⚠ **Não há área de Engenharia nomeada na Puket.** O que existe é **conformidade de produto**, dentro da etapa de fechamento:

> *"`Certificações` (**Inmetro**, DUIMP) — parcial."* — § 4.2.5

\U0001F534 **"Parcial" é a palavra da fonte** — o campo existe e não está completo.

⚠ **A ficha técnica, que seria o artefato típico de engenharia de produto, é responsabilidade dividida entre Estilo, Modelagem e Produto** (§ 4.2.3).""" + AVISO,
 },

 u"08_Ecommerce-Cadastro": {
  u"O que esta área faz": u"""**O cadastro alimenta o e-commerce pela integração com o Linx**, e o campo `Envio site` é o que autoriza o canal:

> *"Campos de 'Envio loja', '**Envio site**', 'Envio atacado' (...) obrigatórios para definir a distribuição e geração de NFs."* — § 4.2.3

\U0001F534 **E o escopo do mapeamento exclui integração nova de e-commerce, por já existir:**
> *"**Não incluso**: (...) integrações adicionais de e-commerce (já em Link c/ Linx)."* — § 2.2""" + AVISO,
 },

 u"09_Comercial-Vendas": {
  u"O que esta área faz": u"""**O Showroom é o marco comercial do ciclo**, e ele depende do fechamento técnico:

> *"Integração final com Linx e geração de código de barras. **Se tardar, gera atrasos no Showroom**."* — § 4.2.5

⚠ **O TO BE propõe um indicador dedicado:** *"Geração de Código → indicador **'Pronto para Showroom'** e aviso automático a Andrea."* — § 5.1

\U0001F534 **O canal atacado é campo obrigatório da ficha** (`Envio atacado`, § 4.2.3).""" + AVISO,
 },

 u"01_Planejamento": {
  u"O que esta área faz": u"""**Responde pelo cronograma da coleção**, que hoje vive **descolado** do fluxo da plataforma:

> *"Necessidade de **integração mais eficiente entre cronograma Puket e etapas do workflow**."*
> — `Mapeamento de Conta Puket — segundo Notion`, 21/03/2025

⚠ **Macroplan e microplan estão no escopo mapeado** como *"Indicadores e Relatórios"* (§ 2.2 do mapeamento de abril).

\U0001F534 **A empresa é descrita como organizada e ainda assim com problema de cronograma:**
> *"empresa organizada, com foco em projetos e processos, porém **com dificuldades de cronograma e desenvolvimento de produtos**."* — § 1""" + AVISO,
 },

 u"10_Marketing": {
  u"O que esta área faz": u"""\U0001F534 **Marketing não é citado em NENHUM ponto do mapeamento de conta.** Não é o mesmo que dizer que a área não existe na Puket — **é dizer que ela não aparece na fonte que descreve como a conta usa a plataforma.**

⚠ **As funções que um Marketing teria aqui estão em outras áreas:**
- **estampa, personagem e tema** → `12_Design`, que os define (§ 4.2.1);
- **arte final e imagem de produto** → `02_Estilo-Criacao` (§ 4.2.3);
- **Showroom**, que é o evento de apresentação da coleção → `09_Comercial-Vendas` (§ 4.2.5).

\U0001F534 **O escopo mapeado é desenvolvimento de produto, ponta a ponta — e para no código de barras.** Nada depois disso foi diagnosticado.""" + AVISO,
 },

 u"05_PCP": {
  u"O que esta área faz": u"""⚠ **Não há área de PCP nomeada na Puket.** O que existe é a lacuna que um PCP cobriria — **planejado contra realizado por etapa**:

> *"Criar indicadores de acompanhamento de cada etapa (**planejado vs. realizado**)."* — § 1, Recomendações
> *"Faltam **KPIs** de desenvolvimento: % de produtos sem composição, pilotagem aprovada etc."* — § 4.3
> *"**Não há dashboard consolidado.**"* — § 4.3

\U0001F534 **Há também etapa de Kanban que o time não usa:** *"Aguardando amostras showroom"* (§ 4.1).""" + AVISO,
 },
}

# As areas da Puket JA TINHAM uma tabela `### Procedencia`. Criar uma segunda
# seria dois documentos vivos sobre o mesmo assunto - o defeito que o
# CLAUDE.md proibe. Entao as linhas novas sao ANEXADAS a tabela existente.
LINHAS_NOVAS = u"""| O que a área faz, entregas, o que não fazem | Notion — `Mapeamento de Conta — Puket` | 04/2025 |
| Etapas de desenvolvimento e níveis de aprovação | Notion — `Mapeamento de Conta Puket — segundo Notion` | 21/03/2025 |
"""

RESSALVA = u"""
\U0001F534 **O mapeamento de abril/2025 é SÍNTESE DE IA sobre três transcrições** (26/02, 06/03 e
13/03 de 2025), assinada por Rafael. **Não é fonte bruta** — o que vier das transcrições
originais prevalece. ⚠ **E tem 17 meses: revalidar antes de usar como diagnóstico atual.**
"""

# A propria area declarava qual era a proxima fonte a varrer. Foi varrida.
# Deixar a nota como estava seria mandar alguem refazer trabalho feito.
NOTA_VELHA = u"### \U0001F534 Próxima fonte a varrer para esta área"
NOTA_NOVA = u"### \U0001F7E2 Fonte varrida em 23/09/2026 — e o que resta"


def anexa_procedencia(txt):
    u"""Anexa as linhas novas a tabela `### Procedencia` que ja existe."""
    if u"Mapeamento de Conta — Puket" in txt.split(u"### Procedência", 1)[-1][:900]:
        return txt                                   # idempotente
    marca = u"### Procedência\n"
    if marca not in txt:
        # area que nunca teve a tabela: cria inteira, antes da Governanca
        alvo = u"## Governança"
        if alvo not in txt:
            return txt
        nova = (u"### Procedência\n| Bloco | Fonte | Data |\n|---|---|---|\n"
                u"| Módulos e ERP | Notion — base `Mapa de Clientes` | varrido 21/09/2026 |\n"
                u"| Pessoas e perfis | Notion — página `Puket`, tabela do PLM | varrido 21/09/2026 |\n"
                + LINHAS_NOVAS + RESSALVA + u"\n")
        return txt.replace(alvo, nova + alvo, 1)
    antes, resto = txt.split(marca, 1)
    linhas = resto.split(u"\n")
    fim = 0
    for i, l in enumerate(linhas):
        if l.strip().startswith(u"|"):
            fim = i + 1
        elif fim:
            break
    novo = linhas[:fim] + LINHAS_NOVAS.rstrip(u"\n").split(u"\n") \
        + RESSALVA.split(u"\n") + linhas[fim:]
    return antes + marca + u"\n".join(novo)


def substitui_secao(txt, titulo, novo):
    for nivel in (u"\n## ", u"\n### "):
        marca = nivel + titulo + u"\n"
        if marca in txt:
            antes, resto = txt.split(marca, 1)
            corte = len(resto)
            for h in (u"\n## ", u"\n### "):
                i = resto.find(h)
                if i != -1:
                    corte = min(corte, i)
            return antes + marca + u"\n" + novo + u"\n" + resto[corte:], True
    return txt, False


def main():
    escritos, blocos, falhas = 0, 0, []
    for area, secoes in sorted(CONTEUDO.items()):
        caminho = os.path.join(BASE, area, u"_contexto", u"contexto-area.md")
        if not os.path.exists(caminho):
            falhas.append((area, u"arquivo nao existe"))
            continue
        txt = io.open(caminho, encoding=u"utf-8").read()
        antes = txt
        for titulo, corpo in secoes.items():
            txt, ok = substitui_secao(txt, titulo, corpo)
            if ok:
                blocos += 1
            else:
                falhas.append((area, u"secao nao encontrada: " + titulo))
        txt = anexa_procedencia(txt)
        txt = txt.replace(NOTA_VELHA, NOTA_NOVA, 1)
        if txt != antes:
            io.open(caminho, u"w", encoding=u"utf-8").write(txt)
            escritos += 1

    w = sys.stdout.write
    w(u"areas preenchidas : %d de 14\n" % escritos)
    w(u"blocos escritos   : %d\n" % blocos)
    if falhas:
        w(u"\U0001F534 falhas:\n")
        for a, m in falhas:
            w(u"   - %s: %s\n" % (a, m))
        return 1
    return 0


if __name__ == u"__main__":
    enc = (getattr(sys.stdout, u"encoding", None) or u"").lower()
    if u"utf" not in enc and hasattr(sys.stdout, u"buffer"):
        sys.stdout = codecs.getwriter(u"utf-8")(sys.stdout.buffer)
    sys.exit(main())
