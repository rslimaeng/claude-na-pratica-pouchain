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
print("        (a aula 1.3 mostrava 'Offset 2 com 5' quando são 6, e 2434 como atrasada)")
try:
    from openpyxl import load_workbook
    from datetime import datetime
    ws = load_workbook("m1/a1-ecossistema-e-fisica/exercicio/pedidos-em-producao.xlsx",
                       data_only=True).active
    HOJE = datetime(2026, 7, 16)
    def data(v):
        if isinstance(v, datetime): return v
        for fmt in ("%d/%m/%Y", "%d-%b-%y"):
            try: return datetime.strptime(str(v).replace("jul", "Jul"), fmt)
            except ValueError: pass
        return None
    linhas = [r for r in ws.iter_rows(min_row=5, values_only=True) if r[0]]
    vivas  = [r for r in linhas if str(r[6]).strip().lower() != "entregue"]
    atrasadas = [r for r in vivas if (d := data(r[5])) and d < HOJE]
    carga = {}
    for r in vivas: carga[r[7]] = carga.get(r[7], 0) + 1
    fatos = {"OS no arquivo": len(linhas), "em produção": len(vivas),
             "atrasadas pela data": len(atrasadas),
             **{f"carga {k}": v for k, v in sorted(carga.items())}}
    for k, v in fatos.items(): print(f"        {k:26} {v}")
    # o que as páginas afirmam tem que bater
    ex = open("m1/a1-ecossistema-e-fisica/exemplo/index.html", encoding="utf-8").read()
    a3 = open("m1/a3-regra-que-fica/index.html", encoding="utf-8").read()
    checagens = [
        (f'>{len(vivas)}<' in ex,            "exemplo · OS em produção"),
        (f'alerta">{len(atrasadas)}<' in ex, "exemplo · atrasadas"),
        (f"{len(atrasadas)} atrasadas" in a3, "aula 1.3 · atrasadas"),
        (f"Offset 2 com {carga.get('Offset 2')}" in a3, "aula 1.3 · carga da Offset 2"),
    ]
    for ok, nome in checagens: diz(ok, "G13", nome)
except ImportError:
    print("        openpyxl ausente, gate pulado")

# ─────────────────────────────────────────────────── veredicto
print("\n" + "=" * 72)
if falhas:
    print(f"FALHOU · {len(falhas)} gate(s):")
    for x in falhas: print("   ", x)
    sys.exit(1)
print(f"TODOS OS GATES PASSARAM · {len(HTML)} páginas, {len(ins)} insumos")
