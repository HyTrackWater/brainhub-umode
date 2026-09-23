# -*- coding: utf-8 -*-
u"""
gera-fichas-pessoa.py - cria UMA FICHA POR PESSOA de cliente.

Decisao do Vinicius em 22 set 2026, textual: "cada pessoa tem sim que ser um
arquivo e realmente ter varios outros nos com ela. Isso nao tem duvida."

Ate aqui, pessoa de cliente era LINHA DE TABELA dentro de `pessoas.md`. Linha de
tabela nao e no de grafo: nao pode ser apontada, nao pode apontar, e nao pode
ligar a ferramenta, area ou demanda. Com ficha, pode.

Fonte: as tabelas `#### Solicitantes de demanda` que a varredura de 22 set 2026
escreveu no `pessoas.md` de cada cliente, a partir do campo `Quem solicitou?` das
demandas. Cada linha vira uma ficha.

O que NAO faz:
  - nao inventa cargo, area, e-mail nem nada que a fonte nao diga;
  - nao unifica grafias (regra do protocolo-varredura-cliente.md secao 9:
    suspeita se levanta, fusao so com confirmacao humana);
  - nao cria ficha para valor que nao e pessoa (area, time, agente, canal).

Estrutura: a MESMA do `_pessoas/_template_pessoa.md`, porque CLAUDE.md trava que
"Areas e Pessoas sao iguais entre Casa e clientes". Campo que so faz sentido para
a Casa fica marcado como nao aplicavel, nao apagado.

Uso:  python scripts/gera-fichas-pessoa.py
"""
import io
import os
import re
import sys
import unicodedata

# Windows entrega stdout em cp1252 e o script imprime emoji de alerta.
# Sem isto, o relatorio de descarte MORRE justo na parte que existe para
# ser vista - foi assim que o `Hermes` sumiu em silencio.
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLI = os.path.join(RAIZ, u"uMode", u"_Clientes")

# Valores que aparecem na coluna de nome e NAO sao pessoa.
# CORRECAO de 22 set 2026: `hermes` SAIU desta lista.
# Eu o tinha filtrado presumindo que fosse o agente `Hermes` da uMode. A pagina
# da NK STORE no Notion mostra `Hermes Goncalves Santiago Junior - Gerente de TI`,
# pessoa real do cliente, com 5 demandas abertas. Presumir que um nome conhecido
# num contexto e o mesmo nome noutro contexto e exatamente o erro que a regra de
# ouro proibe. Homonimo entre agente e pessoa e problema de desambiguacao, e a
# desambiguacao se faz com fonte - nunca com um filtro cego por string.
NAO_PESSOA = set(u"""
compras estilo sourcing merchan planejamento negocios treinamento contrato
ka smb interno time supply faccao qualidade cadastro comercial
""".split())


def slug(s):
    s = unicodedata.normalize(u"NFKD", s).encode(u"ascii", u"ignore").decode(u"ascii")
    s = re.sub(u"[^a-zA-Z0-9]+", u"-", s).strip(u"-").lower()
    return s


def limpa(cel):
    u"""Tira negrito, backtick e emoji de uma celula de tabela."""
    c = cel.strip()
    c = c.replace(u"**", u"").replace(u"`", u"")
    c = re.sub(u"[\U0001F300-\U0001FAFF⚠✅❌]", u"", c)
    return c.strip()


# Tudo que o filtro descarta fica aqui e e IMPRESSO no fim. Filtro silencioso
# foi como o `Hermes` (Gerente de TI da NK STORE, 5 demandas) sumiu do corpus.
COLISOES = []   # dois lacos mirando o mesmo arquivo: o dado sumia calado
DESCARTADOS = []

def e_pessoa(nome):
    n = slug(nome).replace(u"-", u" ")
    if not n or len(n) < 2:
        DESCARTADOS.append((nome, u"regra do filtro"))
        return False
    for t in NAO_PESSOA:
        if n == t or n.startswith(t + u" ") or n.endswith(u" " + t):
            DESCARTADOS.append((nome, u"regra do filtro"))
            return False
    if u" e " in n or u"/" in nome or u"+" in nome:
        DESCARTADOS.append((nome, u"duas pessoas na mesma celula: nao desmembro sem confirmacao"))
        return False
    if u"umode" in n:
        DESCARTADOS.append((nome, u"pessoa da Casa nao se duplica dentro do cliente"))
        return False
    return True


# ---------------------------------------------------------------------------
# SEGUNDA FONTE: a pagina do cliente no Notion (toggle `Pessoas`).
#
# Achado de 22 set 2026: a base de demandas NAO e a unica fonte de pessoa, e
# nao e a melhor. Cada pagina de cliente tem um toggle `Pessoas` com um
# template de 4 blocos - Diretores/Representantes Legais, Responsavel pelo
# Financeiro, Responsaveis pelos Projetos, Responsavel Tecnologia - e quando
# esta preenchido traz NOME COMPLETO, CARGO e AREA.
#
# Ate 22 set 2026 eu afirmei que `cargo` e `area` nao tinham fonte no corpus
# (item 285/315). Tinham. Eu nao tinha aberto a pagina do cliente.
#
# NAO ENTRA AQUI, por decisao de dado sensivel (AGORA.md secao 8.1):
#   CPF, telefone pessoal e e-mail. Registro que existem e onde - nunca o valor.
#
# Formato: cliente -> [(nome como a pagina escreve, cargo, area, bloco)]
DA_PAGINA = {
    u"Luiza Barcelos": [
        (u"Luiz Raul Aleixo Barcelos", u"Diretor / Representante Legal", u"Diretoria",
         u"Diretores e Representantes Legais", u"luiz@luizabarcelos.com.br"),
        (u"Marcinha", u"Diretora Criativa — é a Luiza Barcelos", u"Diretoria Criativa",
         u"Participantes do Projeto", u""),
        (u"Gabriel Jaques da Silva", u"Coordenador de Merchandising — **Líder Central "
         u"do Projeto**", u"Merchandising", u"Responsáveis pelo Projeto",
         u"gabriel.silva@luizabarcelos.com.br"),
        (u"Gustavo Gabriel Santos Sobrinho", u"Gerente Executivo de Estratégia e Gestão "
         u"— **vice-líder do projeto**", u"Estratégia e Gestão",
         u"Responsáveis pelo Projeto", u"gustavo.sobrinho@luizabarcelos.com.br"),
        (u"Samuel Correa", u"Gerente de Inovação e Tecnologia", u"Tecnologia",
         u"Responsável Tecnologia", u"samuel.correa@luizabarcelos.com.br"),
        (u"Ana Lucia Andrade", u"Responsável pelo Financeiro", u"Financeiro",
         u"Responsável pelo Financeiro", u"ana.andrade@luizabarcelos.com.br"),
        (u"Marcelo Tonello", u"Gerente de Operação do Sul — logística e cadastro, "
         u"do desenvolvimento até a precificação", u"Operações",
         u"Participantes do Projeto", u"marcelo.tonello@luizabarcelos.com.br"),
        (u"Romulo Smaniotto", u"Gerente de Desenvolvimento de Produto", u"Desenvolvimento",
         u"Participantes do Projeto", u"romulo.smaniotto@luizabarcelos.com.br"),
        (u"Andre Mello Franco", u"Gerente de Estilo", u"Estilo",
         u"Participantes do Projeto", u"andre.franco@luizabarcelos.com.br"),
        (u"Adriane", u"Gerente de Levantamento de Suprimentos", u"Suprimentos",
         u"Participantes do Projeto", u"adriane.campos@luizabarcelos.com.br"),
        (u"Eduardo Britto", u"Coordenador de Sistemas e Tecnologia", u"Tecnologia",
         u"Responsável Tecnologia", u"eduardo.brito@luizabarcelos.com.br"),
        (u"Ticiane", u"Desenvolvimento", u"Desenvolvimento", u"Participantes do Projeto",
         u"ticiane.rosa@luizabarcelos.com.br"),
        (u"Paulo Victor", u"Assistente Administrativo, **migrando para Estratégia e "
         u"Gestão**", u"Estratégia e Gestão", u"Participantes do Projeto",
         u"paulo.franca@luizabarcelos.com.br"),
        (u"Janaina", u"Processos, Documentação, Estruturação e Mapeamento",
         u"Estratégia, Processos e Projetos", u"Participantes do Projeto",
         u"janaina.araujo@luizabarcelos.com.br"),
        (u"Giuliana", u"Estilo e Merchandising", u"Estilo / Merchandising",
         u"Participantes do Projeto", u""),
        (u"Marcio", u"Cadastro", u"Operações — Cadastro", u"Participantes do Projeto", u""),
        (u"Juliana", u"`[a preencher]`", u"Marketing", u"Ata da reunião de 07/06/2024", u""),
    ],
    u"Cambos": [
        (u"Tony Stefan Lopes", u"Gerente Geral / Diretor de Opera\u00e7\u00e3o da F\u00e1brica",
         u"Opera\u00e7\u00e3o / F\u00e1brica", u"Diretores e Representantes Legais"),
        (u"Valter", u"Head Financeiro", u"Financeiro", u"Respons\u00e1vel pelo Financeiro"),
        (u"Fabiane Sayuri", u"Respons\u00e1vel pelo Desenvolvimento de Produtos",
         u"Desenvolvimento de Produtos", u"Participantes do Projeto"),
        (u"Carolina", u"Estilista", u"Estilo", u"Participantes do Projeto"),
        (u"Gustavo Paiva", u"Head de Tecnologia", u"Tecnologia", u"Respons\u00e1vel Tecnologia"),
    ],
    u"Moda Objetiva": [
        (u"Italo", u"Diretor / Representante Legal", u"Diretoria",
         u"Diretores e Representantes Legais", u""),
        (u"Thamires Ribeiro", u"Respons\u00e1vel pelo Projeto", u"`[a preencher]`",
         u"Respons\u00e1veis pelos Projetos", u""),
        (u"Claudio Gamboni", u"Respons\u00e1vel Tecnologia", u"Tecnologia",
         u"Respons\u00e1vel Tecnologia", u""),
        (u"Maria Carolina", u"`[a preencher]`", u"Estilo", u"Stakeholders", u""),
        (u"Caio", u"`[a preencher]`", u"Planejamento", u"Stakeholders", u""),
        (u"Paula", u"`[a preencher]`", u"Cadastro \u2014 ERP Ilimitar", u"Stakeholders", u""),
    ],
    u"NK STORE": [
        (u"Alexandre de S\u00e1 Pereira", u"Representante Legal",
         u"Diretoria", u"Diretores e Representantes Legais"),
        (u"Gustavo Annechino de Souza e Almeida", u"Representante Legal",
         u"Diretoria", u"Diretores e Representantes Legais"),
        (u"Silvia Shirlei Dias", u"Respons\u00e1vel pelo Financeiro",
         u"Financeiro", u"Respons\u00e1vel pelo Financeiro"),
        (u"Regiane Konopka", u"Diretora de Merchandising \u2014 Compras, Industrial e Compliance",
         u"Merchandising", u"Diretoria Respons\u00e1vel pelo Projeto"),
        (u"Larissa Cid Castilho Batista", u"Gerente de Projeto / Gerente de Produto",
         u"`[a preencher]`", u"L\u00edderes Respons\u00e1veis pelo Projeto"),
        (u"Marina Sacramento", u"PMO \u2014 Compradora de Produtos Acabados",
         u"Compras", u"L\u00edderes Respons\u00e1veis pelo Projeto"),
        (u"Stella Sunaga", u"Diretora de Estilo", u"Estilo",
         u"L\u00edderes de Departamentos"),
        (u"Samuel", u"Coordenador de Estilo", u"Estilo", u"L\u00edderes de Departamentos"),
        (u"Julia", u"Coordenadora de Estilo", u"Estilo", u"L\u00edderes de Departamentos"),
        (u"Robson Bazan", u"Gerente Industrial \u2192 PCP", u"PCP",
         u"L\u00edderes de Departamentos"),
        (u"Andressa", u"Coordenadora do PCP", u"PCP", u"L\u00edderes de Departamentos"),
        (u"Bruna", u"Coordenadora do Planejamento", u"Planejamento",
         u"L\u00edderes de Departamentos"),
        (u"Hermes Gon\u00e7alves Santiago Junior", u"Gerente de TI", u"Tecnologia",
         u"Respons\u00e1vel Tecnologia"),
    ],
}

# Observacao por pessoa, quando a fonte diz algo que nao cabe em cargo/area.
# Nota que nao casa com ficha nenhuma NAO e escrita, e some em silencio - foi o
# que aconteceu ate 22 set 2026, quando NOTA_PAGINA existia e nunca era lida.
USADAS = set()

NOTA_PAGINA = {
    (u"Moda Objetiva", u"Paula"): u"\u26a0 **O papel dela \u00e9 literalmente operar o ERP** \u2014 a fonte escreve `Cadastro ERP Ilimitar`. **\u00c9 a depend\u00eancia de ERP virando cadeira.**",
    (u"Moda Objetiva", u"Maria Carolina"): u"\u26a0 **Veio do bloco `Stakeholders`**, que **s\u00f3 esta conta tem** \u2014 os outros clientes t\u00eam quatro blocos, esta tem cinco. **O template de pessoa N\u00c3O \u00e9 fixo.**",
    (u"Luiza Barcelos", u"Luiz Raul Aleixo Barcelos"): u"🟢 **Trazido pelo Vinícius em 22 set 2026**, copiando à mão um bloco que este conector não renderiza. ⚠ **É o único Diretor/Representante Legal nomeado da conta**, e o e-mail dele é o mesmo do campo `Email Principal Financeiro` da base. 🔴 **A fonte traz telefone e CPF — nenhum dos dois entrou aqui.**",
    (u"Luiza Barcelos", u"Samuel Correa"): u"🟢 **Cargo trazido pelo Vinícius em 22 set 2026:** **Gerente de Inovação e Tecnologia**. Estava `[a preencher]` porque o bloco não renderizava. ⚠ **São DOIS em Tecnologia** — ele e o Eduardo.",
    (u"Luiza Barcelos", u"Marcinha"): u"\U0001F534 **\u00c9 a pr\u00f3pria Luiza Barcelos.** A fonte registra: *o processo est\u00e1 na cabe\u00e7a da Marcinha \u2014 a miss\u00e3o \u00e9 tirar as informa\u00e7\u00f5es da cabe\u00e7a dela e colocar na ferramenta*. **\u00c9 risco de pessoa-chave, escrito pela pr\u00f3pria uMode.** Expectativa dela: *inovar no processo criativo sem perder a criatividade*.",
    (u"Luiza Barcelos", u"Gabriel Jaques da Silva"): u"🟢 **RESOLVIDO em 22 set 2026:** a ata da reunião de 07/06/2024 escreve o nome completo — **`Gabriel Jaques da Silva`**. `Jaques` é nome do meio, `Silva` é o sobrenome do e-mail. **Não eram duas pessoas nem erro: era nome truncado.**",
    (u"Luiza Barcelos", u"Eduardo Britto"): u"⚠ **A mesma página escreve `Britto` e `Brito`, e a ata de 07/06/2024 escreve `Eduardo Brito`.** **Duas grafias na mesma fonte, e eu não escolhi uma.**",
    (u"Luiza Barcelos", u"Andre Mello Franco"): u"🟢 **Nome completo pela ata de 07/06/2024.** A fonte anota: *animado com a implementação*, com expectativa de **foco na coleção e eficiência no setor**.",
    (u"Cambos", u"Fabiane Sayuri"): u"\U0001F7E2 **\u00c9 a `Fabi` de `Fabi e Carol`** \u2014 a p\u00e1gina diz que o l\u00edder do projeto \u00e9 *Tony e Fabi*. **Ambiguidade resolvida com fonte, n\u00e3o com palpite.**",
    (u"Cambos", u"Carolina"): u"\U0001F7E2 **\u00c9 a `Carol` de `Fabi e Carol`**, a c\u00e9lula da base de demandas que eu me recusei a desmembrar. **A p\u00e1gina do cliente desmembrou.**",
    (u"Cambos", u"Tony Stefan Lopes"): u"**L\u00edder do projeto**, junto da Fabi. \U0001F534 **A fonte traz telefone e CPF \u2014 nenhum dos dois entrou aqui** (`T0`).",
    (u"NK STORE", u"Larissa Cid Castilho Batista"): u"a fonte anota: *\"J\u00e1 implantou PLM em v\u00e1rias empresas\"*",
    (u"NK STORE", u"Stella Sunaga"): u"a fonte anota: *\"H\u00e1 10 anos na empresa\"*",
    (u"NK STORE", u"Andressa"): u"\u26a0 a fonte anota: *\"Se ela est\u00e1 feliz com o projeto, estamos bem\"* \u2014 **\u00e9 termometro de projeto, dito pela pr\u00f3pria uMode**",
}


# ---------------------------------------------------------------------------
# TERCEIRA FONTE: a TABELA DE USUARIOS da pagina do cliente.
# Achada em 22 set 2026 na Puket. Nome + e-mail corporativo + perfil + data.
# E a unica fonte que da DATA DE ATIVACAO por pessoa, e a unica com chave de
# identidade. Formato: cliente -> [(nome, email, perfil, ativo_desde, obs)]
DA_PLATAFORMA = {
    u"Caedu": [
        (u"ADRIANA.GERMANO", u"adriana.germano@caedu.com.br", u"Geral", u"21/07/2023",
         u"perfil de acesso `Caedu-Geral`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `21/07/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Alef Vinicius Almeida Rodrigues", u"alef.rodrigues@caedu.com.br", u"Estilo", u"10/01/2024",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `10/01/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"alessandra.rocha", u"alessandra.rocha@caedu.com.br", u"Gerentes", u"[a preencher]",
         u"perfil de acesso `Caedu-Gerentes`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"ALINE.ANTUNES", u"aline.antunes@caedu.com.br", u"Estilo", u"06/09/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `06/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"ALINE.MATOS", u"aline.matos@caedu.com.br", u"Estilo", u"06/09/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `06/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"ALINE.SOARES", u"aline.soares@caedu.com.br", u"Estilo", u"04/09/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `04/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Ana Carolina", u"ana.carolina@caedu.com.br", u"Produto", u"19/06/2024",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `19/06/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Ana Oliveira", u"ana.oliveira@caedu.com.br", u"Estilo", u"24/11/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `24/11/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"ANA.QUEIROZ", u"ana.queiroz@caedu.com.br", u"Estilo", u"06/09/2023 1",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"ana.silva@caedu.com.br", u"ana.silva@caedu.com.br", u"Estilo", u"09/04/2024",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `09/04/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"API Caedu", u"api-caedu@umode.app", u"Dono da Conta", u"05/10/2022",
         u"perfil de acesso `Dono da Conta`, da tabela de usuários da página do cliente. 🔴 **É a única `Dono da Conta` da base** — não é área, é papel na plataforma. 🔴 **`Ativo desde` está corrompido na fonte: `05/10/2022`.** Não deduzi a data."),
        (u"Bárbara Macedo de Oliveira", u"barbara.oliveira@caedu.com.br", u"Produto", u"17/11/2023",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `17/11/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"BEATRIZ.NETTO", u"beatriz.netto@caedu.com.br", u"Estilo", u"04/09/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `04/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Bianca Rocha da Silva", u"bianca.silva@caedu.com.br", u"Estilo", u"10/01/2024",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `10/01/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"BIANCA FONSECA", u"bianca.werneck@caedu.com.br", u"Produto", u"22/11/0202",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"BRIDA.DUCH", u"brida.duch@caedu.com.br", u"Produto", u"27/11/0202",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"BRUNA.GIMENES", u"bruna.gimenes@caedu.com.br", u"Estilo", u"04/09/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `04/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Bruna", u"bruna.guerrero@caedu.com.br", u"Estilo", u"26/10/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `26/10/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"BRUNO.MOREIRA", u"bruno.moreira@caedu.com.br", u"Planejamento", u"11/10/2023",
         u"perfil de acesso `Caedu- Planejamento`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `11/10/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"CAMILA.BLAUDT", u"camila.blaudt@caedu.com.br", u"Modelagem", u"05/09/2023",
         u"perfil de acesso `Caedu-Modelagem`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `05/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"CAMILA.CASTRO", u"camila.castro@caedu.com.br", u"Gerentes", u"04/09/2023",
         u"perfil de acesso `Gerente de Estilo / Caedu-Gerentes`, da tabela de usuários da página do cliente. 🔴 **O campo traz cargo E perfil na mesma célula** (`Gerente de Estilo / Caedu-Gerentes`) — a fonte mistura as duas coisas. 🔴 **`Ativo desde` está corrompido na fonte: `04/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"CAROLINA.CORREA", u"carolina.correa@caedu.com.br", u"Estilo", u"04/09/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `04/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Celso", u"celso.mello@caedu.com.br", u"Planejamento", u"16/07/2024",
         u"perfil de acesso `Caedu- Planejamento`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `16/07/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"CHARLOTTE.PERES", u"charlotte.peres@caedu.com.br", u"Produto", u"12/09/2023",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `12/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"CRISTIANE.MORAES", u"cristiane.moraes@caedu.com.br", u"Gerentes", u"09/10/2023",
         u"perfil de acesso `Caedu-Gerentes`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `09/10/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Daniel Santana da Silva", u"daniel.silva@caedu.com.br", u"Planejamento", u"28/11/2023",
         u"perfil de acesso `Caedu- Planejamento`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `28/11/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"Dayana Layna", u"dayana.virgulino@caedu.com.br", u"Geral", u"08/05/2024",
         u"perfil de acesso `Caedu-Geral`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `08/05/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"DEBORA.FREITAS", u"debora.freitas@caedu.com.br", u"Produto", u"18/07/2023",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `18/07/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Elad", u"elad.lander@caedu.com.br", u"Gerentes", u"28/11/2023",
         u"perfil de acesso `Caedu-Gerentes`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `28/11/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Mapa de Produtos`."),
        (u"EMILLY", u"emilly.lima@caedu.com.br", u"Modelagem", u"05/09/2023",
         u"perfil de acesso `Caedu-Modelagem`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `05/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Mapa de Produtos`."),
        (u"ERIKA.HANEDA", u"erika.haneda@caedu.com.br", u"Estilo", u"05/06/2023",
         u"perfil de acesso `Gerente de Estilo / Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **O campo traz cargo E perfil na mesma célula** (`Gerente de Estilo / Caedu-Estilo`) — a fonte mistura as duas coisas. 🔴 **`Ativo desde` está corrompido na fonte: `05/06/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Evelyn Vasques", u"evelyn.reis@caedu.com.br", u"Estilo", u"03/01/2024",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `03/01/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Fabiana Oliveira dos Santos", u"fabiana.santos@caedu.com.br", u"Planejamento", u"26/01/2024",
         u"perfil de acesso `Caedu- Planejamento`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `26/01/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"FRANCINE.FERREIRA", u"francine.ferreira@caedu.com.br", u"Estilo", u"22/05/2023",
         u"perfil de acesso `Gerente de Estilo / Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **O campo traz cargo E perfil na mesma célula** (`Gerente de Estilo / Caedu-Estilo`) — a fonte mistura as duas coisas. 🔴 **`Ativo desde` está corrompido na fonte: `22/05/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Helen Santos de Lima", u"helen.lima@caedu.com.br", u"Estilo", u"09/01/2024",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `09/01/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"INDIRA.MAGALHAES", u"indira.magalhaes@caedu.com.br", u"Estilo", u"17/07/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `17/07/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Isabelly.Ramos", u"isabelly.ramos@caedu.com.br", u"Estilo", u"06/03/2024",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `06/03/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Jaíne dos Santos de Souza", u"jaine.souza@caedu.com.br", u"Modelagem", u"23/04/2024",
         u"perfil de acesso `Caedu-Modelagem`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `23/04/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"JESSICA.ANDRADE", u"jessica.andrade@caedu.com.br", u"Geral + TM", u"01/04/2024",
         u"perfil de acesso `Caedu-Geral + TM`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `01/04/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"Jessica.Bognar", u"jessica.bognar@caedu.com.br", u"Produto", u"14/03/2024",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `14/03/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"jessica.ferreira", u"jessica.ferreira@caedu.com", u"Estilo", u"14/11/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `14/11/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"JESSICA.DEPAULA", u"jessica.paula@caedu.com.br", u"Estilo", u"06/03/2024",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `06/03/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"JORDANA.FORNI", u"jordana.forni@caedu.com.br", u"Estilo", u"26/10/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `26/10/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"JORGE.SILVA", u"jorge.silva@caedu.com.br", u"Produto", u"10/04/2024",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `10/04/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"JOSE.SOARES", u"jose.soares@caedu.com.br", u"Produto", u"14/11/20",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `14/11/20`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"JULIA.CARREIRO", u"julia.carreiro@caedu.com.br", u"Estilo", u"19/07/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `19/07/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Júlia.gil", u"julia.gil@caedu.com.br", u"Estilo", u"08/02/2024",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `08/02/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"JULIA.SILVA", u"julia.silva@caedu.com.br", u"Estilo", u"04/09/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `04/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Juliana.Nicolini", u"juliana.nicolini@caedu.com.br", u"Produto", u"21/05/2024",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `21/05/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"KARINA.GAINO", u"karina.gaino@caedu.com.br", u"Geral + TM", u"13/11/0202",
         u"perfil de acesso `Caedu-Geral + TM`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"Kevlyn Sá", u"kevlyn.sa@caedu.com.br", u"Produto", u"10/04/2024",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `10/04/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Larissa Ruani", u"larissa.ruani@caedu.com.br", u"Produto", u"10/11/2023",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `10/11/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"LETICIA.SANTOS", u"leticia.santos@caedu.com.br", u"Estilo", u"06/09/2023 1",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"LIVIA.SANTOS", u"livia.santos@caedu.com.br", u"Estilo", u"08/02/2024",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `08/02/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"LUIS.STEPAN", u"luis.stepan@caedu.com.br", u"Estilo", u"05/05/2023",
         u"perfil de acesso `Gerente de Estilo / Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **O campo traz cargo E perfil na mesma célula** (`Gerente de Estilo / Caedu-Estilo`) — a fonte mistura as duas coisas. 🔴 **`Ativo desde` está corrompido na fonte: `05/05/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"MAIRA.SILVA", u"maira.silva@caedu.com.br", u"Estilo", u"17/07/2023",
         u"perfil de acesso `Gerente de Estilo / Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **O campo traz cargo E perfil na mesma célula** (`Gerente de Estilo / Caedu-Estilo`) — a fonte mistura as duas coisas. 🔴 **`Ativo desde` está corrompido na fonte: `17/07/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"MARIA.NASCIMENTO", u"maria.nascimento@caedu.com.br", u"Geral", u"16/06/2023",
         u"perfil de acesso `Gerente de Estilo / Caedu-Geral`, da tabela de usuários da página do cliente. 🔴 **O campo traz cargo E perfil na mesma célula** (`Gerente de Estilo / Caedu-Geral`) — a fonte mistura as duas coisas. 🔴 **`Ativo desde` está corrompido na fonte: `16/06/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Carolina Marchetti", u"maria.vietas@caedu.com.br", u"Produto", u"13/11/0202",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"MARIANA.AMARAL", u"mariana.amaral@caedu.com.br", u"Geral", u"17/07/2023",
         u"perfil de acesso `Gerente de Estilo / Caedu-Geral`, da tabela de usuários da página do cliente. 🔴 **O campo traz cargo E perfil na mesma célula** (`Gerente de Estilo / Caedu-Geral`) — a fonte mistura as duas coisas. 🔴 **`Ativo desde` está corrompido na fonte: `17/07/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"MARINA.BUENO", u"marina.bueno@caedu.com.br", u"Estilo", u"03/01/0202",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"MARISANGELA.SANTANA", u"marisangela.santana@caedu.com.br", u"Qualidade", u"16/08/2023",
         u"perfil de acesso `Caedu-Qualidade`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `16/08/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"MARLON.RIBEIRO", u"marlon.ribeiro@caedu.com.br", u"Geral + TM", u"01/12/0202",
         u"perfil de acesso `Caedu-Geral + TM`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"Mayara Moura", u"mayara.moura@caedu.com.br", u"Produto", u"27/11/2023",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `27/11/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"MIRELLA.ANDRADE", u"mirella.andrade@caedu.com.br", u"Estilo", u"08/05/2023",
         u"perfil de acesso `Gerente de Estilo / Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **O campo traz cargo E perfil na mesma célula** (`Gerente de Estilo / Caedu-Estilo`) — a fonte mistura as duas coisas. 🔴 **`Ativo desde` está corrompido na fonte: `08/05/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"NATALIA.OLIVEIRA", u"natalia.oliveira@caedu.com.br", u"Produto", u"15/09/2023",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `15/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"NATHALIA.GARCIA", u"nathalia.garcia@caedu.com.br", u"Estilo", u"06/09/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `06/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"NATHALIA.KASSAI", u"nathalia.kassai@caedu.com.br", u"Produto", u"10/11/0202",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"PAOLA.ABREU", u"paola.abreu@caedu.com.br", u"Produto", u"15/09/2023",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `15/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Priscilla", u"priscilla.ueda@caedu.com.br", u"Planejamento", u"24/01/2024",
         u"perfil de acesso `Caedu- Planejamento`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `24/01/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"Raphael Santini", u"raphael.santini@caedu.com.br", u"Admim", u"14/06/2024",
         u"perfil de acesso `Caedu-Admim`, da tabela de usuários da página do cliente. ⚠ **`Admim` está escrito assim na fonte** (erro de digitação por `Admin`). Não corrigi. 🔴 **`Ativo desde` está corrompido na fonte: `14/06/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"RAQUEL.BRITO", u"raquel.brito@caedu.com.br", u"Estilo", u"04/09/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `04/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"Rebeca Marques", u"rebeca.souza@caedu.com.br", u"Produto", u"20/06/2024",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `20/06/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Regina", u"regina.silva@caedu.com.br", u"Planejamento", u"19/02/2024",
         u"perfil de acesso `Caedu- Planejamento`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `19/02/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"Renata", u"renata.abinader@caedu.com.br", u"Estilo", u"15/12/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `15/12/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"RENATA.GABELLINI", u"renata.gabellini@caedu.com.br", u"Produto", u"12/09/2023",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `12/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"ROBERTO.FERREIRA", u"roberto.ferreira@caedu.com.br", u"E-commerce", u"02/08/2023",
         u"perfil de acesso `Caedu-E-commerce`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `02/08/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Ronaldo Trentim", u"ronaldo.trentim@caedu.com.br", u"Admim", u"14/06/2024",
         u"perfil de acesso `Caedu-Admim`, da tabela de usuários da página do cliente. ⚠ **`Admim` está escrito assim na fonte** (erro de digitação por `Admin`). Não corrigi. 🔴 **`Ativo desde` está corrompido na fonte: `14/06/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"ROSELENE.FANTI", u"roselene.fanti@caedu.com.br", u"Geral + TM", u"28/03/2024",
         u"perfil de acesso `Caedu-Geral + TM`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `28/03/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"ROSIMEIRE.CASTILHO", u"rosimeire.castilho@caedu.com.br", u"Geral + TM", u"13/05/2024",
         u"perfil de acesso `Caedu-Geral + TM`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `13/05/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"Magoo", u"rpsilva16@stefanini.com", u"Geral", u"19/06/2024",
         u"perfil de acesso `Caedu-Geral`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `19/06/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Samara Lindse", u"samara.santos@caedu.com.br", u"Produto", u"29/11/20",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `29/11/20`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"SOFIA.COSTA", u"sofia.costa@caedu.com.br", u"Produto", u"24/11/0202",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"STEFANY.SILVA", u"stefany.silva@caedu.com.br", u"Estilo", u"17/11/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `17/11/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"THAIS.HAYASHIDA", u"thais.hayashida@caedu.com.br", u"Gerentes", u"10/11/2023",
         u"perfil de acesso `Caedu-Gerentes`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `10/11/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"thais.hucke", u"thais.hucke@caedu.com.br", u"Estilo", u"28/11/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `28/11/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"THAIS.ITICE", u"thais.itice@caedu.com.br", u"Qualidade", u"25/08/2023",
         u"perfil de acesso `Caedu-Qualidade`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `25/08/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"THAMIRIS.DESCIO", u"thamiris.descio@caedu.com.br", u"Gerentes", u"04/09/2023",
         u"perfil de acesso `Gerente de Estilo / Caedu-Gerentes`, da tabela de usuários da página do cliente. 🔴 **O campo traz cargo E perfil na mesma célula** (`Gerente de Estilo / Caedu-Gerentes`) — a fonte mistura as duas coisas. 🔴 **`Ativo desde` está corrompido na fonte: `04/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Victor", u"victor.ponte@caedu.com.br", u"Planejamento", u"16/07/2024",
         u"perfil de acesso `Caedu- Planejamento`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `16/07/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"VITORIA.MENEGHIN", u"vitoria.meneghin@caedu.com.br", u"Admim", u"11/06/2024",
         u"perfil de acesso `Caedu-Admim`, da tabela de usuários da página do cliente. ⚠ **`Admim` está escrito assim na fonte** (erro de digitação por `Admin`). Não corrigi. 🔴 **`Ativo desde` está corrompido na fonte: `11/06/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
        (u"VITORIA.SILVA", u"vitoria.silva@caedu.com.br", u"Estilo", u"04/09/2023",
         u"perfil de acesso `Caedu-Estilo`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `04/09/2023`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`."),
        (u"welvis.lucena", u"welvis.lucena@caedu.com.br", u"Produto", u"16/04/2024",
         u"perfil de acesso `Caedu-Produto`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `16/04/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"Wesley Oliveira", u"wesley.inacio@caedu.com.br", u"Modelagem", u"23/04/2024",
         u"perfil de acesso `Caedu-Modelagem`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `23/04/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Aba de cadastros`, `Meus produtos`."),
        (u"William", u"william.assumpcao@caedu.com.br", u"Planejamento", u"29/01/2024",
         u"perfil de acesso `Caedu- Planejamento`, da tabela de usuários da página do cliente. 🔴 **`Ativo desde` está corrompido na fonte: `29/01/2024`.** Não deduzi a data. ⚠ **Sem acesso a:** `Meus produtos`."),
    ],
    u"NK STORE": [
        (u"Nathalia Gomes", u"nathalia.gomes@nkstore.com.br", u"TI", u"CONVITE ACEITO em 05/12/2024",
         u"perfil de acesso `NK - Admin`. 🆕 **Única pessoa de `TI` na base** — e a NK STORE é o cliente do risco de credencial Linx.", u"Departamento NK", u"Status na base"),
        (u"Cristina", u"cristina@nkstore.com.br", u"Compras", u"CONVITE ACEITO em 12/12/2024",
         u"perfil de acesso `NK - Admin`. ⚠ **`Departamento` e perfil DIVERGEM**: departamento `Compras`, perfil `NK - Admin`. ⚠ **E existe outra `Cristina` na mesma base** (`cristina.amorim`, Modelagem) — não fundi.", u"Departamento NK", u"Status na base"),
        (u"Larissa Castilho", u"larissa.castilho@nkstore.com.br", u"INATIVAR", u"CONVITE ACEITO em 12/12/2024",
         u"perfil de acesso `NK - Admin`. 🔴 **`Departamento NK` = `INATIVAR`** — ⚠ **não é departamento, é INSTRUÇÃO OPERACIONAL escrita no campo de área.** Não afirmo que saiu: afirmo que a fonte pede a inativação.", u"Departamento NK", u"Status na base"),
        (u"Lucas Gabriel de Oliveira Alves de Souza", u"lucas.souza@nkstore.com.br", u"INATIVAR", u"CONVITE ACEITO em 23/01/2025",
         u"perfil de acesso `NK - PCP`. 🔴 **`Departamento NK` = `INATIVAR`** — ⚠ **não é departamento, é INSTRUÇÃO OPERACIONAL escrita no campo de área.** Não afirmo que saiu: afirmo que a fonte pede a inativação.", u"Departamento NK", u"Status na base"),
        (u"Vanessa Veiga", u"vanessa.ventura@nkstore.com.br", u"INATIVAR", u"USUÁRIO INATIVO desde 10/03/2025",
         u"perfil de acesso `NK - Estilo`. 🔴 **Única linha da base com status de INATIVO de fato.** ⚠ **Nome e e-mail divergem** (`Veiga` × `ventura`) — não resolvi.", u"Departamento NK", u"Status na base"),
        (u"Júlia Fontoura", u"julia.fontoura@nkstore.com.br", u"INATIVAR", u"CONVITE ACEITO em 12/12/2024",
         u"perfil de acesso `NK - Estilo`. 🔴 **`Departamento NK` = `INATIVAR`** — ⚠ **não é departamento, é INSTRUÇÃO OPERACIONAL escrita no campo de área.** Não afirmo que saiu: afirmo que a fonte pede a inativação.", u"Departamento NK", u"Status na base"),
        (u"Gabriela Rocin", u"gabriela.rocin@nkstore.com.br", u"INATIVAR", u"CONVITE PENDENTE desde 12/12/2024",
         u"perfil de acesso `NK - Estilo`. 🔴 **`Nome` está `(Não definido)` na fonte** — o nome aqui vem da parte local do e-mail, e **isso é dedução minha, não dado.** 🔴 **`Departamento NK` = `INATIVAR`** — ⚠ **não é departamento, é INSTRUÇÃO OPERACIONAL escrita no campo de área.** Não afirmo que saiu: afirmo que a fonte pede a inativação.", u"Departamento NK", u"Status na base"),
        (u"Kemelly Fernandes", u"kemelly.fernandes@nkstore.com.br", u"Compras", u"CONVITE PENDENTE desde 16/12/2024",
         u"perfil de acesso `NK - Compras`. 🔴 **`Nome` está `(Não definido)` na fonte.** ⚠ **Há uma ficha `kemely.md` vinda da base de demandas** — um `l` de diferença. **NÃO fundi: uma letra não é prova.**", u"Departamento NK", u"Status na base"),
        (u"Sam", u"sam.santos@nkstore.com.br", u"Estilo", u"CONVITE ACEITO em 10/03/2025",
         u"perfil de acesso `NK - Estilo`. 🔴 **Esta pessoa aparece DUAS VEZES na base**, com o mesmo e-mail e a mesma data — linha duplicada na fonte.", u"Departamento NK", u"Status na base"),
        (u"Moreno Ribeiro", u"moreno.ribeiro@nkstore.com.br", u"Estilo", u"CONVITE ACEITO em 13/02/2025",
         u"perfil de acesso `NK - Estilo`.", u"Departamento NK", u"Status na base"),
        (u"Julia Leone", u"julia.leone@nkstore.com.br", u"Estilo", u"CONVITE ACEITO em 18/12/2024",
         u"perfil de acesso `NK - Estilo`. ⚠ **Segunda `Julia` da base** (com `Júlia Fontoura`) — não fundi.", u"Departamento NK", u"Status na base"),
        (u"Thais", u"thais.cerqueira@nkstore.com.br", u"Estilo", u"CONVITE ACEITO em 12/02/2025",
         u"perfil de acesso `NK - Estilo`.", u"Departamento NK", u"Status na base"),
        (u"Ana Ribeiro", u"ana.ribeiro@nkstore.com.br", u"Estilo", u"CONVITE ACEITO em 27/02/2025",
         u"perfil de acesso `NK - Estilo`.", u"Departamento NK", u"Status na base"),
        (u"Stella Sunaga", u"stella.sunaga@nkstore.com.br", u"Estilo", u"CONVITE ACEITO em 12/12/2024",
         u"perfil de acesso `NK - Estilo`.", u"Departamento NK", u"Status na base"),
        (u"Heloisa Lima", u"heloisa.lima@nkstore.com.br", u"Compras", u"CONVITE ACEITO em 12/12/2024",
         u"perfil de acesso `NK - Compras`.", u"Departamento NK", u"Status na base"),
        (u"Negrita Moreira Candido", u"negrita.candido@nkstore.com.br", u"Compras", u"CONVITE ACEITO em 12/12/2024",
         u"perfil de acesso `NK - Compras`.", u"Departamento NK", u"Status na base"),
        (u"Isabely Consul Dantas", u"isabely.consul@nkstore.com.br", u"Compras", u"CONVITE ACEITO em 12/12/2024",
         u"perfil de acesso `NK - Compras`.", u"Departamento NK", u"Status na base"),
        (u"Nelson Tadeu Alves Ferreira", u"expedicao2@nkstore.com.br", u"Compras", u"CONVITE ACEITO em 06/01/2025",
         u"perfil de acesso `NK - Compras`. 🔴 **E-mail FUNCIONAL, não nominal** (`expedicao2@`) com pessoa nomeada atrás. ⚠ **A chave de identidade aqui é de uma CAIXA, não de uma pessoa** — e o `2` sugere que existe uma `expedicao1`.", u"Departamento NK", u"Status na base"),
        (u"Laís", u"lais.batista@nkstore.com.br", u"PCP", u"CONVITE ACEITO em 12/12/2024",
         u"perfil de acesso `NK - PCP`.", u"Departamento NK", u"Status na base"),
        (u"Beatriz Nunes", u"beatriz.nunes@nkstore.com.br", u"PCP", u"CONVITE ACEITO em 12/12/2024",
         u"perfil de acesso `NK - PCP`.", u"Departamento NK", u"Status na base"),
        (u"Caroline Silva", u"caroline.silva@nkstore.com.br", u"PCP", u"CONVITE ACEITO em 23/01/2025",
         u"perfil de acesso `NK - PCP`.", u"Departamento NK", u"Status na base"),
        (u"Milena Machado", u"milena.machado@nkstore.com.br", u"PCP", u"CONVITE ACEITO em 27/01/2025",
         u"perfil de acesso `NK - PCP`.", u"Departamento NK", u"Status na base"),
        (u"Andressa Correa", u"andressa.correa@nkstore.com.br", u"PCP", u"CONVITE ACEITO em 12/12/2024",
         u"perfil de acesso `NK - PCP`.", u"Departamento NK", u"Status na base"),
        (u"ROSANA RIBEIRO DA SILVA CAMPOS", u"rosana.campos@nkstore.com.br", u"PCP", u"CONVITE ACEITO em 23/01/2025",
         u"perfil de acesso `NK - PCP`. ⚠ **O nome está em CAIXA ALTA na fonte** — mantido como está, `protocolo-varredura-cliente.md` § 9.", u"Departamento NK", u"Status na base"),
        (u"Vanessa", u"vanessa.oliveira@nkstore.com.br", u"Modelagem", u"CONVITE ACEITO em 15/01/2025",
         u"perfil de acesso `NK - Modelagem`. ⚠ **Segunda `Vanessa` da base** (com `Vanessa Veiga`, `vanessa.ventura`) — não fundi.", u"Departamento NK", u"Status na base"),
        (u"Silvia", u"silvia.nascimento@nkstore.com.br", u"Modelagem", u"CONVITE ACEITO em 15/01/2025",
         u"perfil de acesso `NK - Modelagem`. ⚠ **Há uma ficha `silvia-shirlei-dias.md`** vinda da base de demandas. **NÃO fundi:** `Shirlei Dias` × `nascimento` não batem.", u"Departamento NK", u"Status na base"),
        (u"Vitoria Fernanda", u"fernanda.coelho@nkstore.com.br", u"Modelagem", u"CONVITE ACEITO em 15/01/2025",
         u"perfil de acesso `NK - Modelagem`. ⚠ **nome e e-mail divergem** (`Vitoria Fernanda` × `fernanda.coelho`) — não resolvi.", u"Departamento NK", u"Status na base"),
        (u"Cristina Amorim", u"cristina.amorim@nkstore.com.br", u"Modelagem", u"CONVITE ACEITO em 08/01/2025",
         u"perfil de acesso `NK - Modelagem`. ⚠ **Segunda `Cristina` da base** — não fundi.", u"Departamento NK", u"Status na base"),
    ],
    u"Puket": [
        (u"Michele Lunkes", u"michele.lunkes@grupounico.com", u"Sourcing Nacional", u"02/12/2022", u""),
        (u"Yves", u"yves.pancotti@puket.com.br", u"Produto", u"02/02/2023", u""),
        (u"Tayna Basile", u"tayna.basile@puket.com.br", u"Design", u"03/06/2022", u""),
        (u"pedro.pereira", u"pedro.pereira@puket.com.br", u"Design", u"03/06/2022", u""),
        (u"gabriela.araujo", u"gabriela.araujo@puket.com.br", u"Design", u"03/06/2022", u""),
        (u"vinicius.cesar", u"vinicius.cesar@grupounico.com", u"BI", u"04/10/2022", u""),
        (u"rosimare.simoes", u"rosimare.simoes@puket.com.br", u"TEX", u"09/06/2022", u""),
        (u"vanessa.facci", u"vanessa.facci@puket.com.br", u"Estilo", u"09/06/2022", u""),
        (u"isadora.koch", u"isadora.koch@grupounico.com", u"Certifica\u00e7\u00e3o", u"09/06/2022", u""),
        (u"luciene.comenalli", u"luciene.comenalli@grupounico.com", u"Sourcing Nacional", u"09/06/2022", u""),
        (u"catarina.bassotto", u"catarina.bassotto@grupounico.com", u"Produto", u"09/06/2022", u""),
        (u"giuliana.zuttion", u"giuliana.zuttion@puket.com.br", u"Estilo", u"09/06/2022", u""),
        (u"ana.ballestero", u"ana.ballestero@grupounico.com", u"Qualidade", u"09/06/2022", u""),
        (u"andreza.zan", u"andreza.zan@grupounico.com", u"Sourcing Nacional", u"09/06/2022", u""),
        (u"renata.ortiz", u"renata.ortiz@puket.com.br", u"Estilo", u"09/06/2022", u""),
        (u"girlaine.rocha", u"girlaine.rocha@puket.com.br", u"TEX", u"09/06/2022", u""),
        (u"gabriela.fonseca", u"gabriela.fonseca@puket.com.br", u"Estilo", u"10/06/2022", u""),
        (u"audria.monteiro", u"audria.monteiro@grupounico.com", u"Sourcing Nacional", u"10/06/2022", u""),
        (u"giulia.gomes", u"giulia.gomes@puket.com.br", u"Estilo", u"13/06/2022", u""),
        (u"thalita.santana", u"thalita.santana@puket.com.br", u"Produto", u"14/12/2022", u""),
        (u"leticia.martins", u"leticia.martins@puket.com.br", u"Produto", u"14/06/2022", u""),
        (u"andressa.grilli", u"andressa.grilli@puket.com.br", u"Produto", u"14/06/2022", u""),
        (u"luciana.ribeiro", u"luciana.ribeiro@puket.com.br", u"PCP", u"16/08/2022", u""),
        (u"Carla", u"carla.luz@grupounico.com", u"Controladoria", u"16/06/2023", u""),
        (u"Sarah Nunes", u"sarah.nunes@grupounico.com", u"Controladoria", u"16/06/2023",
         u"\U0001F534 **O perfil est\u00e1 RISCADO na fonte** \u2014 marca de desativa\u00e7\u00e3o. "
         u"\u26a0 **N\u00e3o afirmo que saiu:** afirmo que a fonte riscou."),
        (u"Isabela Pereira", u"isabela.cipriani@grupounico.com", u"Importa\u00e7\u00e3o", u"19/06/2023",
         u"\u26a0 **nome e e-mail divergem** (`Pereira` \u00d7 `cipriani`) \u2014 n\u00e3o resolvi"),
        (u"karina.ossugui", u"karina.ossugui@puket.com.br", u"Design", u"20/12/2022", u""),
        (u"aline.soares", u"aline.soares@puket.com.br", u"Estilo", u"20/06/2022", u""),
        (u"leticia.lopes", u"leticia.lopes@puket.com.br", u"Estilo", u"20/06/2022", u""),
        (u"Marcela Polyana", u"marcela.figueiredo@puket.com.br", u"Produto", u"20/06/2022",
         u"\u26a0 **nome e e-mail divergem** (`Polyana` \u00d7 `figueiredo`) \u2014 n\u00e3o resolvi"),
        (u"andressa.duarte", u"andressa.duarte@puket.com.br", u"Produto", u"21/06/2022", u""),
        (u"Eduarda de Souza", u"eduarda.souza@grupounico.com", u"Importa\u00e7\u00e3o", u"21/06/2023", u""),
        (u"lara.cunha", u"lara.cunha@grupounico.com", u"Qualidade", u"21/09/2022", u""),
        (u"luiza.pavanate", u"luiza.pavanate@grupounico.com", u"Qualidade", u"21/09/2022", u""),
        (u"jessica.cesar", u"jessica.cesar@grupounico.com", u"Sourcing Nacional", u"22/06/2022", u""),
        (u"andrea.nunes", u"andrea.nunes@grupounico.com", u"Sourcing Nacional", u"23/06/2022", u""),
        (u"paulo.pelaes", u"paulo.pelaes@grupounico.com", u"Qualidade", u"23/09/2022", u""),
        (u"maria.germano", u"maria.germano@grupounico.com", u"Projetos", u"24/05/2022", u""),
        (u"gabriela.begnini", u"gabriela.begnini@grupounico.com", u"Projetos", u"24/05/2022", u""),
        (u"Eli", u"elisangela.silva@puket.com.br", u"Projetos", u"24/05/2023", u""),
        (u"andrea.mendes", u"andrea.mendes@grupounico.com", u"Projetos", u"25/11/2022", u""),
        (u"Romina Torres", u"romina.torres@puket.com.br", u"Sourcing Nacional", u"27/04/2023", u""),
        (u"natasha.maruno", u"natasha.maruno@grupounico.hk", u"Estilo", u"30/06/2022",
         u"\u26a0 **dom\u00ednio `.hk`** \u2014 Hong Kong. \u00danica da carteira fora do Brasil."),
    ],
}


def casa_plataforma(cliente, nome_curto):
    u"""Casa um nome da base de demandas com a tabela de usuarios da plataforma.

    Casa por nome INTEIRO, por primeiro nome OU pela parte local do e-mail.
    Ambiguidade devolve None: suspeita se levanta, fusao so com confirmacao humana.

    O casamento por nome inteiro foi acrescentado em 23 set 2026: sem ele,
    `Stella Sunaga` da pagina e `stella.sunaga@` da plataforma viravam DUAS
    fichas da mesma pessoa, e a segunda sobrescrevia a primeira em silencio.
    Nome completo identico nao e palpite - e a evidencia mais forte que existe
    aqui depois do e-mail.
    """
    alvo = slug(nome_curto)
    hits = []
    for r in DA_PLATAFORMA.get(cliente, ()):
        sn = slug(r[0])
        if sn == alvo or sn.split(u"-")[0] == alvo or slug(r[1].split(u"@")[0]) == alvo:
            hits.append(r)
    return hits[0] if len(hits) == 1 else None


def casa_pagina(cliente, nome_curto):
    u"""Acha o registro da pagina para um nome da base de demandas.

    A base de demandas escreve primeiro nome (`Andressa`); a pagina escreve nome
    completo (`Hermes Goncalves Santiago Junior`). Caso o primeiro nome bata com
    MAIS DE UM registro, devolve None: ambiguidade se declara, nao se resolve no
    palpite (mesma regra da secao 9 do protocolo).
    """
    alvo = slug(nome_curto)
    hits = [r for r in DA_PAGINA.get(cliente, ()) if slug(r[0]).split(u"-")[0] == alvo]
    return hits[0] if len(hits) == 1 else None


def ficha(cliente, nome, demandas, pri, ult, obs, pag=None, plat=None):
    L = []
    L.append(u"# %s · Pessoa · %s" % (cliente, nome))
    L.append(u"")
    L.append(u"> **Ficha gerada por `scripts/gera-fichas-pessoa.py` em 22 set 2026.**")
    L.append(u"> Campo sem fonte fica `[a preencher]` — **nada foi inferido.**")
    L.append(u"> **O nome está exatamente como aparece na fonte. Variantes não foram fundidas** —")
    L.append(u"> ver `protocolo-varredura-cliente.md` § 9.")
    L.append(u"")
    L.append(u"## Identificação")
    L.append(u"### Foto")
    L.append(u"`[a preencher]`")
    L.append(u"### Nome completo")
    if pag:
        L.append(u"**%s** \u2014 da p\u00e1gina do cliente. A base de demandas a escreve como `%s`."
                 % (pag[0], nome))
    else:
        L.append(u"`[a preencher]` \u2014 a fonte registra **`%s`**" % nome)
    L.append(u"### Nome preferido / como é chamado(a)")
    L.append(u"**%s**" % nome)
    L.append(u"### Email")
    if plat:
        L.append(u"**`%s`** — e-mail **corporativo**, da tabela de usuários da "
                 u"plataforma." % plat[1])
        L.append(u"")
        L.append(u"🟢 **É a chave de identidade desta pessoa** — o que resolve "
                 u"grafia diferente sem inventar gente (item 252). Tier `T2`.")
        L.append(u"")
        L.append(u"⚠ **E-mail corporativo entra; e-mail pessoal, telefone e CPF não** "
                 u"— `AGORA.md` § 8.1.")
    elif pag and len(pag) > 4 and pag[4]:
        L.append(u"**`%s`** — e-mail **corporativo**, da página do cliente." % pag[4])
        L.append(u"")
        L.append(u"🟢 **É a chave de identidade desta pessoa** (item 252). "
                 u"Tier `T2`.")
        L.append(u"")
        L.append(u"🔴 **A fonte também traz telefone, e num caso CPF — "
                 u"nenhum dos dois entrou aqui** (`T0`, `AGORA.md` § 8.1).")
    elif pag:
        L.append(u"🔴 **Existe na página do cliente e NÃO foi replicado aqui.**")
        L.append(u"Mesma decisão vale para telefone e CPF — `AGORA.md` § 8.1.")
        L.append(u"**Registro que existe e onde; o valor fica na fonte.**")
    else:
        L.append(u"`[a preencher]`")
    L.append(u"### Cadeira / cargo atual")
    if pag:
        L.append(u"**%s**" % pag[1])
        L.append(u"")
        L.append(u"Fonte: p\u00e1gina do cliente no Notion, toggle `Pessoas` \u203a `%s`." % pag[3])
    else:
        L.append(u"`[a preencher]` \u2014 \u26a0 **esta pessoa n\u00e3o aparece no toggle `Pessoas` da")
        L.append(u"p\u00e1gina do cliente**, que \u00e9 onde o cargo vive quando existe.")
    L.append(u"### Nível HIC")
    L.append(u"⚠ **não se aplica** — é campo da Casa uMode")
    L.append(u"### \u00c1rea (organizacional)")
    if plat:
        L.append(u"**%s** — **`%s`** na tabela de usuários da plataforma."
                 % (plat[2], plat[5] if len(plat) > 5 else u"Perfil de Acesso"))
        L.append(u"")
        L.append(u"⚠ **`%s` NÃO é área canônica** — é como o cliente "
                 u"nomeia. **Não mapeei para a grade de 14** sem sua confirmação."
                 % (plat[5] if len(plat) > 5 else u"Perfil de acesso"))
    elif pag:
        L.append(u"**%s** — ⚠ **como a fonte a nomeia**, não necessariamente uma das"
                 % pag[2])
        L.append(u"14 áreas canônicas. **Não mapeei para a grade** sem sua confirmação.")
    else:
        L.append(u"`[a preencher]` — 🔴 **o vínculo pessoa e área é a "
                 u"lacuna aberta do corpus**")
    L.append(u"### Data de entrada na uMode")
    L.append(u"⚠ **não se aplica** — pessoa de cliente")
    L.append(u"### Status na uMode")
    L.append(u"⚠ **não se aplica** — pessoa de cliente")
    L.append(u"### Data de saída da uMode")
    L.append(u"⚠ **não se aplica** — pessoa de cliente")
    L.append(u"")
    L.append(u"## Papel")
    L.append(u"### Missão da cadeira")
    L.append(u"`[a preencher]`")
    L.append(u"### Responsabilidades principais")
    L.append(u"`[a preencher]`")
    L.append(u"### Interfaces")
    L.append(u"`[a preencher]`")
    nota = NOTA_PAGINA.get((cliente, pag[0] if pag else nome))
    if nota:
        L.append(u"")
        L.append(u"### Observação da fonte")
        L.append(nota)
        USADAS.add((cliente, pag[0] if pag else nome))
    L.append(u"")
    L.append(u"## Histórico")
    L.append(u"### Áreas de atuação histórica")
    L.append(u"`[a preencher]`")
    L.append(u"### Clientes atuais atendidos")
    L.append(u"⚠ **não se aplica** — esta pessoa **é** do cliente `%s`" % cliente)
    L.append(u"### Clientes atendidos historicamente")
    L.append(u"⚠ **não se aplica**")
    L.append(u"")
    L.append(u"## Personificação")
    for h in (u"Como se descreve", u"Personalidade / forma de trabalhar",
              u"O que a diferencia", u"Curiosidade / algo pessoal"):
        L.append(u"### %s" % h)
        L.append(u"`[a preencher]`")
    L.append(u"")
    L.append(u"## Competências")
    for h in (u"Experiência profissional anterior", u"Skills / habilidades técnicas",
              u"Cursos e certificações", u"Ferramentas e plataformas que domina"):
        L.append(u"### %s" % h)
        L.append(u"`[a preencher]`")
    L.append(u"")
    L.append(u"## Atividade observada")
    L.append(u"")
    L.append(u"> **Uma pessoa não é ativa porque tem cadastro. É ativa porque agiu, numa data que")
    L.append(u"> dá para citar.**")
    L.append(u"")
    L.append(u"| Sinal | Valor |")
    L.append(u"|---|---|")
    L.append(u"| **Demandas abertas** | **%s** |" % demandas)
    L.append(u"| Primeira atividade observada | %s |" % (pri or u"`[a preencher]`"))
    L.append(u"| Última atividade observada | %s |" % (ult or u"`[a preencher]`"))
    L.append(u"| Fonte | campo `Quem solicitou?` da base de demandas do Notion |")
    if plat:
        L.append(u"| **%s** | **%s** |" % (plat[6] if len(plat) > 6 else u"Ativo na plataforma desde", plat[3]))
        L.append(u"| Fonte | tabela de usuários da página do cliente |")
    if obs and obs != u"—":
        L.append(u"")
        L.append(u"**Observação da fonte:** %s" % obs)
    L.append(u"")
    L.append(u"## Governança")
    L.append(u"### Quem pode alterar este documento")
    L.append(u"Responsável de atendimento + liderança de Atendimento uMode")
    L.append(u"")
    return u"\n".join(L) + u"\n"


def main():
    criadas = 0
    clientes = 0
    for c in sorted(os.listdir(CLI)):
        base = os.path.join(CLI, c)
        pm = os.path.join(base, u"00_Institucional", u"_contexto", u"pessoas.md")
        if not os.path.exists(pm):
            continue
        s = io.open(pm, encoding="utf-8").read()
        # A pagina do cliente e a tabela de usuarios sao fontes INDEPENDENTES da
        # base de demandas. Antes deste ajuste, cliente sem tabela de solicitante
        # era pulado - e a Luiza Barcelos, com 15 pessoas com cargo na pagina,
        # ficava de fora. Fonte nova nao pode depender da fonte antiga.
        tem_dem = u"#### Solicitantes de demanda" in s
        if not tem_dem and c not in DA_PAGINA and c not in DA_PLATAFORMA:
            continue
        bloco = u""
        if tem_dem:
            bloco = s[s.index(u"#### Solicitantes de demanda"):]
            fim = bloco.find(chr(10) + u"## ")
            if fim > 0:
                bloco = bloco[:fim]
        destino = os.path.join(base, u"00_Institucional", u"_pessoas")
        if not os.path.isdir(destino):
            os.makedirs(destino)
        n_cli = 0
        usados = set()
        usados_plat = set()
        escritos = {}   # caminho -> qual fonte ja escreveu nele
        for linha in bloco.split(u"\n"):
            if not linha.startswith(u"| ") or linha.startswith(u"|---") or u"Demandas |" in linha:
                continue
            cels = [limpa(x) for x in linha.strip().strip(u"|").split(u"|")]
            if len(cels) < 5:
                continue
            nome = cels[0]
            if not e_pessoa(nome):
                continue
            pag = casa_pagina(c, nome)
            plat = casa_plataforma(c, nome)
            if plat:
                usados_plat.add(plat[1])
            if pag:
                usados.add(pag[0])
            p = os.path.join(destino, slug(nome) + u".md")
            novo = ficha(c, nome, cels[1], cels[2], cels[3],
                         cels[4] if len(cels) > 4 else u"", pag, plat)
            escritos[p] = (u"base de demandas", nome)
            if os.path.exists(p) and io.open(p, encoding="utf-8").read() == novo:
                continue
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
            criadas += 1
            n_cli += 1
        # Pessoa que aparece na PAGINA do cliente e nunca abriu demanda
        # tambem e pessoa. Ate aqui ela nao existia no corpus: a base de
        # demandas era a unica fonte, e quem nao abre chamado ficava invisivel.
        for r in DA_PAGINA.get(c, ()):
            if r[0] in usados:
                continue
            p = os.path.join(destino, slug(r[0]) + u".md")
            if p in escritos:
                COLISOES.append((c, p, escritos[p], (u"pagina do cliente", r[0])))
                continue
            escritos[p] = (u"pagina do cliente", r[0])
            # A pagina do cliente da o CARGO; a tabela de usuarios da o E-MAIL.
            # Ate 23 set 2026 os dois lados nasciam como fichas separadas e uma
            # sobrescrevia a outra. Quem esta nas duas fontes merece UMA ficha
            # com as duas metades.
            plat_p = casa_plataforma(c, r[0])
            if plat_p:
                usados_plat.add(plat_p[1])
            novo = ficha(c, r[0], u"0", u"", u"",
                         u"nao aparece na base de demandas", r, plat_p)
            if os.path.exists(p) and io.open(p, encoding="utf-8").read() == novo:
                continue
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
            criadas += 1
            n_cli += 1
        # Quem existe SO na tabela de usuarios da plataforma tambem e pessoa -
        # e traz o que nenhuma outra fonte traz: e-mail e data de ativacao.
        for r in DA_PLATAFORMA.get(c, ()):
            if r[1] in usados_plat:
                continue
            local = r[1].split(u"@")[0]
            e_login = u"." in r[0] or slug(r[0]) == slug(local)
            base_nome = local.replace(u".", u" ") if e_login else r[0]
            pth = os.path.join(destino, slug(r[1].split(u"@")[0]) + u".md")
            if pth in escritos:
                COLISOES.append((c, pth, escritos[pth],
                                 (u"tabela de usuarios", r[1])))
                continue
            escritos[pth] = (u"tabela de usuarios", r[1])
            novo = ficha(c, base_nome, u"0", u"", u"",
                         r[4] or u"nao aparece na base de demandas", None, r)
            if os.path.exists(pth) and io.open(pth, encoding="utf-8").read() == novo:
                continue
            io.open(pth, "w", encoding="utf-8", newline="").write(novo)
            criadas += 1
            n_cli += 1

        if n_cli:
            clientes += 1
            print(u"  %-20s %3d fichas" % (c, n_cli))
    print(u"")
    orfas = sorted(set(NOTA_PAGINA) - USADAS)
    if orfas:
        print(u"")
        print(u"❌ NOTA SEM FICHA - estas notas NAO foram escritas em lugar nenhum:")
        for c, n in orfas:
            print(u"   %s / %s" % (c, n))
        print(u"Corrija a chave para o nome EXATO em DA_PAGINA.")
        return 1

    if COLISOES:
        print(u"")
        print(u"\U0001F534 COLISAO DE ARQUIVO (%d) - duas fontes miraram o mesmo "
              u".md. A PRIMEIRA ficou; a segunda NAO foi escrita:" % len(COLISOES))
        for cli, cam, a, b in COLISOES:
            print(u"   %s" % os.path.basename(cam))
            print(u"      ficou:  %s -> %s" % a)
            print(u"      perdeu: %s -> %s" % b)
            print(u"      cliente: %s" % cli)
        print(u"Decida a mao se sao a MESMA pessoa. "
              u"Fusao nao se faz no palpite.")

    if DESCARTADOS:
        print(u"")
        print(u"\u26a0 NOMES DESCARTADOS PELO FILTRO (%d) - confira se algum e pessoa:"
              % len(DESCARTADOS))
        vistos = set()
        for nome, motivo in DESCARTADOS:
            if nome in vistos:
                continue
            vistos.add(nome)
            print(u"   %-28s %s" % (nome, motivo))
        print(u"Filtro silencioso foi como o `Hermes` sumiu. Descarte tem que ser visivel.")

    print(u"fichas de pessoa de cliente criadas/atualizadas: %d em %d clientes"
          % (criadas, clientes))
    print(u"Rode `python scripts/gera-conexoes.py` em seguida para ligá-las ao grafo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
