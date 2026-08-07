# -*- coding: utf-8 -*-
"""
Gera as 4 paginas de DEMONSTRACAO do M1, agora escritas PARA O ALUNO.

O que mudou e por que: a versao anterior era roteiro de palco publicado no site
do aluno. Tinha "pergunte a sala", "espere o silencio passar", "zoom em 150%",
"antes de a turma entrar" e plano B. Isso nao ensina ninguem e obriga o
instrutor a ler em voz alta instrucao de como dar a propria aula.

Regra que sai daqui: na pagina publica so entra o que e para o aluno.
Direcao de cena sai do site e vira arquivo interno.

Blocos permitidos: fazer · prompt · tela · repare · ensina · lista
Blocos proibidos: pergunte a sala · plano B · preparo de palco · minutos
"""
import html
import os
import re

RAIZ = ("/Users/rafaellima/developer/4-cursos-treinamentos/treinamentos-in-company/"
        "pouchain-claude-na-pratica/site/m1")

CSS = """
:root{
  --bg:#F0EEE6; --bg-elev:#FFFFFF; --bg-code:#F5F3EA;
  --text:#141413; --text-muted:#3D3D3A; --text-dim:#87867F;
  --border:rgba(20,20,19,.10); --border-strong:rgba(20,20,19,.18);
  --accent:#1A5670; --accent-dark:#10394C; --accent-soft:#DDEAF0;
  --accent-line:rgba(26,86,112,.22);
  --col:860px;
  --radius-sm:6px; --radius:10px; --radius-lg:14px;
  --font-body:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  --font-mono:'JetBrains Mono',ui-monospace,'SF Mono','Menlo',monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font-body);background:var(--bg);color:var(--text);
  font-size:16px;line-height:1.62;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
.wrap{max-width:var(--col);margin:0 auto;padding:0 24px}

.topo{padding:26px 0 0}
.volta{font-family:var(--font-mono);font-size:12px;color:var(--text-dim);margin-bottom:18px}
.kicker{font-family:var(--font-mono);font-size:11.5px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--accent);margin-bottom:14px}
h1{font-size:clamp(28px,4vw,38px);font-weight:700;line-height:1.12;
  letter-spacing:-.02em;margin-bottom:16px}
.lead{font-size:18px;line-height:1.6;color:var(--text-muted)}
.lead strong{color:var(--text)}
.lead + .lead{margin-top:12px}

/* o arquivo usado na demonstracao */
.arq{display:flex;align-items:center;justify-content:space-between;gap:16px;
  flex-wrap:wrap;margin-top:24px;background:var(--bg-elev);
  border:1px solid var(--border);border-radius:var(--radius);padding:16px 18px}
.arq-info{min-width:0}
.arq-nome{display:block;font-family:var(--font-mono);font-size:14px;
  color:var(--text);font-weight:500}
.arq-meta{display:block;font-size:13.5px;color:var(--text-dim);margin-top:4px}
.arq-btn{font-size:14px;font-weight:500;background:var(--accent);color:#fff;
  border-radius:var(--radius-sm);padding:9px 16px;text-decoration:none;white-space:nowrap}
.arq-btn:hover{background:var(--accent-dark)}

/* os passos */
.passo{display:grid;grid-template-columns:74px 1fr;gap:20px;margin-top:44px;
  align-items:start}
.passo-n{font-family:var(--font-mono);font-size:26px;font-weight:600;
  color:var(--accent);line-height:1;letter-spacing:-.02em;position:sticky;top:20px}
.passo-corpo{min-width:0;border-left:1px solid var(--border);padding-left:22px;
  padding-bottom:4px}
.passo-titulo{font-size:22px;font-weight:600;letter-spacing:-.015em;
  line-height:1.26;margin-bottom:18px}

.bloco{margin-bottom:18px}
.bloco:last-child{margin-bottom:0}
.b-rot{display:block;font-family:var(--font-mono);font-size:10px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--text-dim);margin-bottom:6px}
.b-tx{display:block;font-size:16.5px;line-height:1.55;color:var(--text-muted)}
.b-tx b{color:var(--text);font-weight:600}
.b-tx code{font-family:var(--font-mono);font-size:14px;background:var(--bg-code);
  padding:2px 6px;border-radius:4px;color:var(--accent-dark)}

/* a unica caixa colorida: o que o aluno precisa notar na tela */
.repare{background:var(--accent-soft);border-radius:var(--radius);
  padding:17px 19px;margin-bottom:18px}
.repare .b-rot{color:var(--accent-dark)}
.repare .b-tx{color:var(--accent-dark);font-size:17px}
.repare .b-tx b{color:var(--accent-dark);font-weight:700}

/* lista de itens dentro de um passo */
.lista{margin-bottom:18px}
.lista ul{list-style:none;margin-top:2px}
.lista li{font-size:16.5px;line-height:1.5;color:var(--text-muted);
  padding-left:22px;position:relative;margin-bottom:10px}
.lista li:last-child{margin-bottom:0}
.lista li::before{content:"";position:absolute;left:2px;top:11px;width:6px;
  height:6px;border-radius:50%;background:var(--accent-line)}
.lista li b{color:var(--text);font-weight:600}

.ensina{margin-bottom:18px;padding-top:15px;border-top:1px solid var(--border)}
.ensina .b-tx{font-size:16px}

/* prompt: fechado, para nao cortar a leitura */
.pbox{border:1px solid var(--border);border-radius:var(--radius);margin-bottom:18px;
  background:var(--bg-elev);overflow:hidden}
.pbox > summary{list-style:none;cursor:pointer;display:flex;align-items:center;
  justify-content:space-between;gap:12px;padding:12px 15px}
.pbox > summary::-webkit-details-marker{display:none}
.pbox > summary:hover{background:var(--bg-code)}
.p-nome{font-family:var(--font-mono);font-size:11.5px;letter-spacing:.05em;
  color:var(--text-muted)}
.p-abre{font-family:var(--font-mono);font-size:11px;color:var(--accent)}
.pbox[open] .p-abre::after{content:" \\25B4"}
.pbox:not([open]) .p-abre::after{content:" \\25BE"}
.pconteudo{font-family:var(--font-mono);font-size:13.5px;line-height:1.62;
  white-space:pre-wrap;padding:14px 15px 15px;color:var(--text-muted);
  border-top:1px solid var(--border)}
.p-rodape{display:flex;justify-content:flex-end;padding:0 15px 13px}
.pbtn{font-family:var(--font-mono);font-size:11px;font-weight:500;cursor:pointer;
  background:var(--accent);color:#fff;border:none;padding:7px 15px;
  border-radius:var(--radius-sm)}
.pbtn:hover{background:var(--accent-dark)}
.pbox.curto .pconteudo{font-size:16px;color:var(--text)}

.fecho{margin:48px 0 0;background:var(--accent-soft);border-radius:var(--radius-lg);
  padding:24px 26px}
.fecho-rot{display:block;font-family:var(--font-mono);font-size:11px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--accent-dark);margin-bottom:11px}
.fecho-frase{display:block;font-size:21px;font-weight:600;line-height:1.34;
  letter-spacing:-.015em;color:var(--accent-dark);margin-bottom:13px}
.fecho p{font-size:16px;line-height:1.6;color:var(--accent-dark);opacity:.92}
.fecho strong{opacity:1;font-weight:600}

.rodape{margin:44px 0 60px;padding-top:20px;border-top:1px solid var(--border);
  font-size:14.5px;color:var(--text-dim);line-height:1.6}

.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(80px);
  background:var(--text);color:#fff;padding:11px 20px;border-radius:999px;
  font-size:14px;transition:transform .22s;z-index:99}
.toast.on{transform:translateX(-50%) translateY(0)}

@media (max-width:720px){
  .passo{grid-template-columns:1fr;gap:8px}
  .passo-n{position:static}
  .passo-corpo{border-left:none;padding-left:0}
  .arq{flex-direction:column;align-items:stretch}
  .arq-btn{text-align:center}
}
"""

JS = """
document.querySelectorAll(".pbtn").forEach(function(b){
  b.addEventListener("click", function(e){
    e.preventDefault();
    var el = document.getElementById(b.dataset.alvo);
    navigator.clipboard.writeText(el.innerText).then(function(){
      var t = document.getElementById("toast");
      t.classList.add("on");
      setTimeout(function(){ t.classList.remove("on"); }, 1500);
    });
  });
});
"""

ROTULO = {"fazer": "O que fazer", "tela": "O que aparece na tela",
          "repare": "Repare nisto", "ensina": "O que isso ensina"}


def bloco(tipo, conteudo, pid=None, extra=None):
    if tipo == "prompt":
        nome, texto, curto = conteudo
        cls = "pbox curto" if curto else "pbox"
        aberto = " open" if curto else ""
        rot = "fechar" if curto else "abrir"
        return (f'      <details class="{cls}"{aberto}>\n'
                f'        <summary>\n'
                f'          <span class="p-nome">{nome}</span>\n'
                f'          <span class="p-abre">{rot}</span>\n'
                f'        </summary>\n'
                f'        <div class="pconteudo" id="{pid}">{texto}</div>\n'
                f'        <div class="p-rodape">'
                f'<button class="pbtn" data-alvo="{pid}">Copiar</button></div>\n'
                f'      </details>\n')
    if tipo == "lista":
        rot, itens = conteudo
        lis = "\n".join(f"          <li>{i}</li>" for i in itens)
        return (f'      <div class="lista">\n        <span class="b-rot">{rot}</span>\n'
                f'        <ul>\n{lis}\n        </ul>\n      </div>\n')
    cls = {"repare": "repare", "ensina": "ensina"}.get(tipo, "bloco")
    rot = extra or ROTULO[tipo]
    return (f'      <div class="{cls}">\n        <span class="b-rot">{rot}</span>\n'
            f'        <span class="b-tx">{conteudo}</span>\n      </div>\n')


def render(cfg):
    p = []
    p.append('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="UTF-8">\n'
             '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
             f'<title>{cfg["title"]}</title>\n'
             f'<meta name="description" content="{cfg["desc"]}">\n'
             '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
             '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700'
             '&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">\n'
             f'<style>{CSS}</style>\n</head>\n<body>\n<div class="wrap">\n\n')
    p.append('  <div class="topo">\n'
             f'    <div class="volta"><a href="../">&larr; voltar para a aula {cfg["aula"]}</a></div>\n'
             f'    <div class="kicker">Demonstração · aula {cfg["aula"]}</div>\n'
             f'    <h1>{cfg["h1"]}</h1>\n')
    for l in cfg["lead"]:
        p.append(f'    <p class="lead">{l}</p>\n')
    if cfg.get("arquivo"):
        nome, meta, href = cfg["arquivo"]
        p.append('\n    <div class="arq">\n      <div class="arq-info">\n'
                 f'        <span class="arq-nome">{nome}</span>\n'
                 f'        <span class="arq-meta">{meta}</span>\n      </div>\n'
                 f'      <a class="arq-btn" href="{href}" download>Baixar &darr;</a>\n'
                 '    </div>\n')
    p.append('  </div>\n')

    n_prompt = 0
    for i, passo in enumerate(cfg["passos"], start=1):
        p.append(f'\n  <div class="passo">\n    <div class="passo-n">{i:02d}</div>\n'
                 f'    <div class="passo-corpo">\n'
                 f'      <div class="passo-titulo">{passo["titulo"]}</div>\n\n')
        for b in passo["blocos"]:
            tipo, conteudo = b[0], b[1]
            extra = b[2] if len(b) > 2 else None
            if tipo == "prompt":
                n_prompt += 1
                p.append(bloco(tipo, conteudo, pid=f"p{n_prompt}"))
            else:
                p.append(bloco(tipo, conteudo, extra=extra))
        p.append('    </div>\n  </div>\n')

    f = cfg["fecho"]
    p.append(f'\n  <div class="fecho">\n    <span class="fecho-rot">{f[0]}</span>\n'
             f'    <span class="fecho-frase">{f[1]}</span>\n    <p>{f[2]}</p>\n  </div>\n')
    p.append(f'\n  <p class="rodape">{cfg["rodape"]}</p>\n\n</div>\n\n'
             '<div class="toast" id="toast">copiado</div>\n'
             f'<script>{JS}</script>\n</body>\n</html>\n')
    return "".join(p)


# ══════════════════════════════════════════════════════════════════════════
from demos_conteudo import AULAS  # noqa                                    # noqa: E402

for slug, cfg in AULAS.items():
    destino = os.path.join(RAIZ, slug, "demonstracao", "index.html")
    saida = render(cfg)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, "w", encoding="utf-8").write(saida)
    proibidas = [t for t in ["pergunte à sala", "Pergunte à sala", "plano B",
                             "Plano B", "Se der errado", "a sala", "A sala",
                             "turma", "palco", "min</span>", "quadro"]
                 if t in saida]
    print(f"{slug:26} {len(saida):>6} bytes · {len(cfg['passos'])} passos"
          + (f"  ⚠️ RESIDUO DE PALCO: {proibidas}" if proibidas else "  ✓ limpo"))
