#!/usr/bin/env python3
"""
Gates de qualidade do site · rode da raiz do repo:  python3 goals/gates.py

Cada onda fecha rodando isto. Sai com código 1 se algum gate falhar, então
serve como hook de pre-commit se um dia a gente quiser.

Regra que vale para escrever gate novo aqui:
  1. Gate com exceção permanente deixa de ser gate. Se precisa de exceção,
     conserta o código, não o gate.
  2. Gate que procura uma palavra NÃO PODE rodar contra o arquivo que enuncia
     a regra sobre aquela palavra, senão se auto-reprova. Ver EXCLUI_REGRA.
"""
import re, glob, os, sys
from html.parser import HTMLParser

EM = chr(0x2014)                       # o travessão, escrito por escape de propósito
AULAS = sorted(glob.glob("m1/a*/index.html"))
HTML  = sorted(glob.glob("*.html")) + sorted(glob.glob("m1/**/*.html", recursive=True))
MD    = sorted(glob.glob("*.md")) + sorted(glob.glob("**/*.md", recursive=True))
# arquivos que ENUNCIAM as regras. Procurar a palavra proibida aqui é falso positivo.
EXCLUI_REGRA = {"CLAUDE.md", "goals/goal-01-infra-e-padrao.md", "goals/gates.py",
                "goals/README.md", "README.md", "_shared/design-tokens.md"}

falhas = []
def diz(cond, gate, alvo="", extra=""):
    print(f"  {'OK   ' if cond else 'FALHA'} {alvo:44}{extra}")
    if not cond: falhas.append(f"{gate} {alvo}".strip())

def titulo(t): print("\n" + t)

# ─────────────────────────────────────────────────── G1 · anatomia da aula
titulo("G1 · ESTRUTURA · os blocos obrigatórios da página de aula")
MARC = ["o que você vai saber fazer", "a situação", "o conceito", "como funciona",
        "demonstração", "sua vez", "confira", "pegadinhas", "a cerca",
        "confira você mesmo",                       # o validador de fim de aula
        "checkpoint", "cobertura da ementa"]
for f in AULAS:
    s = open(f, encoding="utf-8").read().lower()
    falta = [m for m in MARC if m not in s]
    # o hook fecha toda aula. Na última do módulo ele fecha o módulo, e vale igual.
    if not re.search(r"a trava que est[ae] (aula|módulo) não resolve", s):
        falta.append("hook")
    diz(not falta, "G1", f, f"{len(MARC)+1-len(falta)}/{len(MARC)+1}  {falta or ''}")

# ─────────────────────────────────────────────────── G2 · gabarito escondido
titulo("G2 · GABARITO ATRÁS DE <details>, NUNCA ABERTO")
for f in AULAS:
    s = open(f, encoding="utf-8").read()
    det = len(re.findall(r'<details class="gabarito"', s))
    ab  = len(re.findall(r'<details class="gabarito" open', s))
    diz(det >= 1 and ab == 0, "G2", f, f"details={det} open={ab}")

# ─────────────────────────────────────────────────── G3 · higiene de dados
titulo("G3 · HIGIENE · o site é público")
# 3a. Página nenhuma usa o nome real do cliente: o universo é a Gráfica Aurora.
for f in HTML:
    s = open(f, encoding="utf-8").read()
    diz(not re.search(r"\bPouchain\b", s), "G3a", f,
        "nome do cliente em página de conteúdo" if re.search(r"\bPouchain\b", s) else "")
# 3b. Achado de consultoria não entra em lugar nenhum, nem em .md de governança.
ACHADO = [r"\bshadow ai\b", r"\bLGPD\b", r"\d+\s+casos? confirmados?",
          r"fragilidade estrutural", r"risco confirmado", r"\bCPF\b\s*[:\d]"]
for f in HTML + MD:
    if f in EXCLUI_REGRA: continue
    s = open(f, encoding="utf-8").read()
    hits = [p for p in ACHADO if re.search(p, s, re.I)]
    diz(not hits, "G3b", f, str(hits) if hits else "")

# ─────────────────────────────────────────────────── G4 · fato de produto datado
titulo("G4 · AFIRMAÇÃO SOBRE PRODUTO PRECISA DE DATA DE VERIFICAÇÃO")
AFIRMA = r"Pro, Max|Team ou Enterprise|proprietário da conta|individual de cada|não sincroniza"
for f in AULAS:
    s = open(f, encoding="utf-8").read()
    n = len(re.findall(AFIRMA, s))
    d = len(re.findall(r"verificad[oa].{0,40}\d{2}/\d{2}/\d{4}", s, re.I))
    diz(n == 0 or d >= 1, "G4", f, f"afirmações={n} datas={d}")

# ─────────────────────────────────────────────────── G6 · navegação
titulo("G6 · NAVEGAÇÃO · link interno que não existe")
mortos = []
for f in HTML:
    base = os.path.dirname(f)
    for href in re.findall(r'href="([^"#][^"]*)"', open(f, encoding="utf-8").read()):
        if href.startswith(("http", "mailto")): continue
        alvo = os.path.normpath(os.path.join(base, href))
        if os.path.isdir(alvo): alvo = os.path.join(alvo, "index.html")
        if not os.path.exists(alvo): mortos.append(f"{f} -> {href}")
diz(not mortos, "G6", "todos os links", str(mortos) if mortos else "0 morto(s)")

# ─────────────────────────────────────────────────── G7 · render
titulo("G7 · RENDER · balanço de tags")
class Bal(HTMLParser):
    VOID = {"meta","link","br","img","hr","input","source","col"}
    def __init__(s): super().__init__(); s.p=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in s.VOID: s.p.append(t)
    def handle_endtag(s,t):
        if not s.p: s.err.append(f"</{t}> sobrando"); return
        if s.p[-1]==t: s.p.pop()
        elif t in s.p:
            while s.p and s.p[-1]!=t: s.err.append(f"<{s.p.pop()}> não fechada")
            s.p.pop()
for f in HTML:
    p = Bal(); p.feed(open(f, encoding="utf-8").read())
    diz(not p.err and not p.p, "G7", f, str((p.err+p.p)[:3]) if (p.err or p.p) else "")

# ─────────────────────────────────────── G7-ter · classe usada sem CSS
titulo("G7-ter · CLASSE USADA SEM NENHUM CSS QUE A PEGUE")
for f in HTML:
    src = open(f, encoding="utf-8").read()
    style = "\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    body  = re.sub(r"<style>.*?</style>", "", src, flags=re.S)
    usadas = set()
    for m in re.findall(r'class="([^"]+)"', body): usadas.update(m.split())
    falta = sorted(usadas - set(re.findall(r"\.([A-Za-z][\w-]*)", style)))
    diz(not falta, "G7ter", f, str(falta) if falta else "")

# ─────────────────────────────────────────────────── G9 · travessão
titulo("G9 · TRAVESSÃO")
tot = {f: open(f, encoding="utf-8").read().count(EM) for f in HTML + MD}
tot = {f: n for f, n in tot.items() if n}
diz(not tot, "G9", "todo o repo", str(tot) if tot else f"0 em {len(HTML)+len(MD)} arquivos")

# ─────────────────────────────────────────────────── G10 · formato de insumo
titulo("G10 · FORMATO DOS INSUMOS")
ruins = glob.glob("m1/**/*.csv", recursive=True) + glob.glob("m1/**/*.txt", recursive=True)
ins = sorted(glob.glob("m1/**/exercicio/*", recursive=True) +
             glob.glob("m1/**/gabarito/*", recursive=True))
for i in ins: print(f"        {i}")
diz(not ruins, "G10", "insumos", f"{len(ins)} arquivo(s), {len(ruins)} em formato proibido")

# ─────────────────────────────────────── G11 · inline forçada a bloco
titulo("G11 · TAG INLINE FORÇADA A display:block")
print("        (quebra a frase no meio quando a tag aparece dentro de um <p>)")
INLINE = {"strong","em","b","i","span","a","code","small","abbr"}
for f in HTML:
    style = "\n".join(re.findall(r"<style>(.*?)</style>",
                                 open(f, encoding="utf-8").read(), re.S))
    bad = []
    for sel, b in re.findall(r"([^{}@]+)\{([^}]*)\}", style):
        if "display:block" not in b.replace(" ", "").replace("\n", ""): continue
        sel = sel.strip()
        if sel.split(",")[0].split()[-1].strip() in INLINE and ">" not in sel:
            bad.append(sel)
    diz(not bad, "G11", f, str(bad) if bad else "")

# ─────────────────────────────────── G11b · flex/grid engolindo frase
titulo("G11b · CONTAINER flex/grid COM TEXTO SOLTO + TAG INLINE")
print("        (cada pedaço vira item de flex e a frase quebra no meio)")
INLINE_T = {"strong","em","b","i","span","a","code","small","abbr"}

class Flexy(HTMLParser):
    """Acha elemento flex/grid que tem, como filho DIRETO, texto solto e tag inline.
    Regex não serve aqui: com <div> dentro de <div> ela fecha na tag errada."""
    VOID = {"meta","link","br","img","hr","input","source","col"}
    def __init__(s, alvo):
        super().__init__(); s.alvo = alvo; s.pilha = []; s.achados = set()
    def handle_starttag(s, t, attrs):
        cls = dict(attrs).get("class", "").split()
        marcado = next((c for c in cls if c in s.alvo), None)
        if s.pilha and t in INLINE_T: s.pilha[-1]["inline"] = True
        if t not in s.VOID:
            s.pilha.append({"tag": t, "cls": marcado, "texto": 0, "inline": False})
    def handle_endtag(s, t):
        while s.pilha:
            n = s.pilha.pop()
            if n["cls"] and n["texto"] > 12 and n["inline"]: s.achados.add(n["cls"])
            if n["tag"] == t: break
    def handle_data(s, d):
        if s.pilha: s.pilha[-1]["texto"] += len(d.strip())

for f in HTML:
    src = open(f, encoding="utf-8").read()
    style = "\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    body  = re.sub(r"<style>.*?</style>", "", src, flags=re.S)
    alvo = set()
    for sel, b in re.findall(r"([^{}@]+)\{([^}]*)\}", style):
        bb = b.replace(" ", "").replace("\n", "")
        if "display:flex" in bb or "display:grid" in bb:
            u = sel.strip().split(",")[0].split()[-1].strip()
            if u.startswith("."): alvo.add(u[1:].split(":")[0])
    fp = Flexy(alvo); fp.feed(body)
    diz(not fp.achados, "G11b", f, str(sorted(fp.achados)) if fp.achados else "")

# ─────────────────────── G12 · o nome do nível é o aprovado, e vem com o recurso
titulo("G12 · NOME DE NÍVEL APROVADO + RECURSO OFICIAL DO CLAUDE AO LADO")
print("        (vocabulário interno não vai para a tela · ver CLAUDE.md §5 e §7-bis)")
NOMES_OK = ["Por que ele piora na conversa longa",
            "Pedir uma vez e receber pronto",
            "Ele já começa sabendo as suas regras",
            "Cada tarefa puxa o seu próprio procedimento",
            "Ele abre os arquivos onde você trabalha",
            "Você prova que está certo antes de mandar",
            "Roda sem você apertar o play"]
land = open("index.html", encoding="utf-8").read()
achados = re.findall(r'class="nivel-nome">([^<]+)<', land)
diz(achados == NOMES_OK, "G12", "index.html · nomes da trilha",
    "" if achados == NOMES_OK else f"divergem de CLAUDE.md §5: {set(achados) ^ set(NOMES_OK)}")
# toda linha da trilha mostra pelo menos um recurso oficial
linhas = land.split('class="nivel-row')[1:]
sem = [i for i, b in enumerate(linhas) if 'class="rec' not in b.split("</div>\n      </div>")[0]]
diz(not sem, "G12", "index.html · recurso em toda linha",
    "" if not sem else f"linhas sem .rec: {sem}")
# hero de aula e card do hub carregam o recurso
for f in AULAS + ["m1/index.html"]:
    src = open(f, encoding="utf-8").read()
    n = len(re.findall(r'class="rec[" ]', src))
    esperado = 4 if f.endswith("m1/index.html") else 1
    diz(n >= esperado, "G12", f, f"chips de recurso={n} (mínimo {esperado})")

# ─────────────── G13 · número sobre a planilha tem que sair da planilha
titulo("G13 · OS NÚMEROS DA GRÁFICA AURORA BATEM COM O .XLSX")
print("        (nenhum número sobre insumo é digitado à mão: tudo recalculado aqui)")
try:
    from openpyxl import load_workbook
    from datetime import datetime, timedelta
    HOJE = datetime(2026, 7, 16)
    MES = {"jan":1,"fev":2,"mar":3,"abr":4,"mai":5,"jun":6,
           "jul":7,"ago":8,"set":9,"out":10,"nov":11,"dez":12}

    def data(v):
        if isinstance(v, datetime): return v
        s = str(v).strip()
        for f in ("%d/%m/%Y", "%Y-%m-%d"):
            try: return datetime.strptime(s, f)
            except ValueError: pass
        p = s.split("-")
        if len(p) == 3 and p[1] in MES:
            return datetime(2000 + int(p[2]), MES[p[1]], int(p[0]))
        return None

    def texto(p):
        return re.sub(r"<[^>]+>", " ", open(p, encoding="utf-8").read()).lower()

    N = {1:"um",2:"dois",3:"três",4:"quatro",5:"cinco",6:"seis",8:"oito",
         9:"nove",10:"dez",12:"doze",14:"quatorze"}

    # ── PLANILHA DO EXERCÍCIO · PCP, 120 OS ────────────────────────────────
    ws = load_workbook("m1/a1-ecossistema-e-fisica/exercicio/"
                       "pedidos-em-producao.xlsx", data_only=True).active
    linhas = [r for r in ws.iter_rows(min_row=5, values_only=True)
              if r[0] and str(r[0]).isdigit()]
    vivas = [r for r in linhas if str(r[6]).strip().lower() != "entregue"]
    atras = [r for r in vivas if (d := data(r[5])) and d < HOJE]
    marcadas = [r for r in linhas if str(r[6]).strip() == "Atrasado"]
    todas_os = [r[0] for r in linhas]
    dups = sorted({o for o in todas_os if todas_os.count(o) > 1})
    print(f"        {'PCP · linhas':28} {len(linhas)}")
    print(f"        {'PCP · em aberto':28} {len(vivas)}")
    print(f"        {'PCP · atrasadas pela data':28} {len(atras)}")
    print(f"        {'PCP · marcadas no sistema':28} {len(marcadas)}   (a mentira do campo)")
    print(f"        {'PCP · OS repetidas':28} {dups}")

    ex   = texto("m1/a1-ecossistema-e-fisica/exemplo/index.html")
    a1   = texto("m1/a1-ecossistema-e-fisica/index.html")
    a3   = texto("m1/a3-regra-que-fica/index.html")
    a3d  = texto("m1/a3-regra-que-fica/demonstracao/index.html")
    a2d  = texto("m1/a2-pedir-para-entregar/demonstracao/index.html")

    for ok, nome in [
        (f">{len(vivas)}<" in open("m1/a1-ecossistema-e-fisica/exemplo/index.html",
                                   encoding="utf-8").read(), "PCP · exemplo · em produção"),
        (f'alerta">{len(atras)}<' in open("m1/a1-ecossistema-e-fisica/exemplo/index.html",
                                          encoding="utf-8").read(), "PCP · exemplo · atrasadas"),
        (f"{len(linhas)} linhas" in ex,            "PCP · exemplo · tamanho do arquivo"),
        (f"{len(dups)} os repetidas" in ex,        "PCP · exemplo · OS duplicadas"),
        (f"{len(linhas)} ordens de serviço" in a1, "PCP · aula 1.1 · tamanho no download"),
        (f"{len(linhas)} ordens de serviço" in a2d,"PCP · aula 1.2 · tamanho no download"),
        (f"{len(atras)} atrasadas" in a3,          "PCP · aula 1.3 · atrasadas"),
        (f"marca <strong>{len(marcadas)}</strong>" in
         open("m1/a3-regra-que-fica/index.html", encoding="utf-8").read(),
                                                   "PCP · aula 1.3 · marcadas no sistema"),
        (f"{len(atras)} os atrasadas" in a3d,      "PCP · demo 1.3 · atrasadas"),
        (f"marca <b>{len(marcadas)}</b>" in
         open("m1/a3-regra-que-fica/demonstracao/index.html", encoding="utf-8").read(),
                                                   "PCP · demo 1.3 · marcadas no sistema"),
    ]: diz(bool(ok), "G13", nome)

    # ── PLANILHA DA DEMONSTRAÇÃO · Compras, 104 linhas ─────────────────────
    wc = load_workbook("m1/a1-ecossistema-e-fisica/demonstracao/"
                       "cotacoes-fornecedores.xlsx", data_only=True).active
    FOLGA = (datetime(2026, 7, 22) - HOJE).days
    cot = [r for r in wc.iter_rows(min_row=5, values_only=True) if r[0] and r[4]]
    forn = {}
    for r in cot:
        f = forn.setdefault(r[4], {"prazo": r[6], "sem": 0, "caixa": None})
        if r[5] in (None, ""):        f["sem"] += 1
        if "cx" in str(r[2]).lower(): f["caixa"] = str(r[2])
    itens   = {r[0] for r in cot}
    atrasa  = {f: d["prazo"] - FOLGA for f, d in forn.items() if d["prazo"] > FOLGA}
    pior    = max((d["sem"] for d in forn.values()), default=0)
    caixa   = next((d["caixa"] for d in forn.values() if d["caixa"]), None)
    por_cx  = int(re.search(r"\d+", caixa).group()) if caixa else 0
    viaveis = [f for f, d in forn.items() if not d["sem"] and d["prazo"] <= FOLGA]
    print(f"        {'cotações · linhas':28} {len(cot)}")
    print(f"        {'cotações · itens × forn.':28} {len(itens)} × {len(forn)}")
    print(f"        {'cotações · maior atraso':28} {max(atrasa.values(), default=0)} dias")
    print(f"        {'cotações · itens sem cotar':28} {pior} (pior fornecedor)")
    print(f"        {'cotações · cotou tudo E no prazo':28} {viaveis}")

    d1  = texto("m1/a1-ecossistema-e-fisica/demonstracao/index.html")
    for ok, nome in [
        (f"{len(cot)} linhas de cotação" in d1 and f"{len(cot)} linhas" in a1,
         "cotações · tamanho da planilha"),
        (f"{len(forn)} fornecedores" in d1 and f"{len(forn)} fornecedores" in a1,
         "cotações · quantos fornecedores"),
        (f"{len(itens)} insumos" in d1, "cotações · quantos insumos"),
        (len(atrasa) == 1 and f"{N[list(atrasa.values())[0]]} dias" in d1,
         "cotações · de quantos dias é o atraso"),
        (pior and f"cotar {N[pior]} itens" in d1, "cotações · itens sem cotar"),
        (por_cx and f"caixa com {N[por_cx]}" in d1, "cotações · a armadilha da caixa"),
        (len(viaveis) == 1 and "um único fornecedor" in d1,
         "cotações · sobra um fornecedor só"),
    ]: diz(bool(ok), "G13", nome)

    # ── piso de tamanho · CLAUDE.md §8-ter ─────────────────────────────────
    for nome, n in [("pedidos-em-producao", len(linhas)), ("cotacoes-fornecedores", len(cot))]:
        diz(n >= 100, "G13", f"piso de 100 linhas · {nome}", f"{n} linhas")
except ImportError:
    print("        openpyxl ausente, gate pulado")

# ─── G14 · a demonstração é passo a passo PARA O ALUNO, não roteiro de palco
titulo("G14 · DEMONSTRAÇÃO ESCRITA PARA O ALUNO, SEM DIREÇÃO DE CENA")
print("        (o site é do aluno · direção de palco vive fora dele · CLAUDE.md §9)")
# frases que só fazem sentido ditas pelo instrutor para a turma
PALCO = ["pergunte à sala", "pergunte a sala", "pergunte à turma", "plano b",
         "se der errado", "se a sala", "antes de a turma", "minutos de palco",
         "anote no quadro", "no quadro", "espere o silêncio", "a sala responde",
         "não responda você", "vire para a sala", "aponte na tela",
         "aponte isto", "diga em voz alta", "leia em voz alta", "a turma"]
for f in AULAS:
    dir_aula = os.path.dirname(f)
    demo = os.path.join(dir_aula, "demonstracao", "index.html")
    if not os.path.exists(demo):
        diz(False, "G14", f, "sem pasta demonstracao/"); continue
    bruto = open(demo, encoding="utf-8").read()
    limpo = re.sub(r"<[^>]+>", " ", bruto).lower()
    passos = len(re.findall(r'class="passo"', bruto))
    repare = len(re.findall(r'class="repare"', bruto))
    prompt = len(re.findall(r'class="pbox', bruto))
    # nenhum passo pode ser só instrução: todo passo tem que entregar alguma
    # coisa para o aluno levar (o que reparar, o que aquilo ensina, ou a lista)
    corpos = re.findall(r'<div class="passo-corpo">(.*?)\n    </div>', bruto, re.S)
    secos = [i + 1 for i, c in enumerate(corpos)
             if not re.search(r'class="(repare|ensina|lista)"', c)]
    ligado = 'href="./demonstracao/"' in open(f, encoding="utf-8").read()
    achados = sorted({t for t in PALCO if t in limpo})
    faltas = []
    if passos < 3:      faltas.append(f"só {passos} passos")
    if repare == 0:     faltas.append("nenhum bloco 'repare nisto'")
    if secos:           faltas.append(f"passo(s) só com instrução: {secos}")
    if prompt == 0:     faltas.append("nenhum prompt literal")
    if not ligado:      faltas.append("a aula não linka a demonstração")
    if achados:         faltas.append(f"DIREÇÃO DE CENA: {achados}")
    diz(not faltas, "G14", dir_aula,
        f"{passos} passos · {repare} repare · {prompt} prompts · 0 seco"
        if not faltas else str(faltas))

# ─────────── G14b · o G14 só olhava demonstracao/, e o defeito voltou pela porta
#             de fora: o card que aponta para ela continuava descrevendo roteiro.
#             gate que cobre parte da superfície deixa o erro voltar pelo resto.
titulo("G14b · NENHUMA PÁGINA DO ALUNO FALA COM O INSTRUTOR")
print("        (vale para TODO html do site, não só para a demonstração)")
# \b evita o falso positivo: "a sala" não pode casar dentro de "nesta sala"
CENA = [r"pergunte à (sala|turma)", r"pergunte a (sala|turma)", r"\bplano b\b",
        r"\ba sala\b (responde|dita|classific|precisa ver|conserta)",
        r"vire (para|pra) a sala", r"anote no quadro", r"espere o silêncio",
        r"não responda você", r"aponte (na tela|isto)", r"diga em voz alta",
        r"minutos de palco", r"se der errado", r"se a sala\b",
        # vocabulário do roteiro velho: a demonstração tem passos, não momentos
        r"\broteiro\b", r"momento \d+ d", r"os (três|quatro|cinco|seis) momentos",
        r"com o que apontar", r"executa ao vivo", r"travar na sala"]
CENA_RE = re.compile("|".join(CENA), re.I)
for f in HTML:
    limpo = re.sub(r"<[^>]+>", " ", open(f, encoding="utf-8").read())
    limpo = re.sub(r"\s+", " ", limpo)
    achados = sorted({m.group(0).strip() for m in CENA_RE.finditer(limpo)})
    diz(not achados, "G14b", f, f"FALA COM O INSTRUTOR: {achados}" if achados else "")

# ─────────── G15 · duração não vai para o material do aluno, em lugar nenhum
titulo("G15 · SEM DURAÇÃO EM NENHUMA PÁGINA DO ALUNO")
print("        (tempo é controle interno e vive fora do site · CLAUDE.md §9-ter)")
TEMPO = re.compile(r"\d+\s*(min\b|minutos?\b)", re.I)
SLOTS = [r'class="hero-kicker">([^<]*)<', r'class="destino-title">([^<]*)<',
         r'class="step-eyebrow">([^<]*)<', r'class="aula-dur">([^<]*)<',
         r'class="aula-title">([^<]*)<', r'class="kicker">([^<]*)<',
         r'class="passo-titulo">([^<]*)<']
for f in AULAS + ["m1/index.html"] + sorted(glob.glob("m1/a*/demonstracao/index.html")):
    s = open(f, encoding="utf-8").read()
    achados = [t for pat in SLOTS for t in re.findall(pat, s) if TEMPO.search(t)]
    diz(not achados, "G15", f, str(achados) if achados else "")
