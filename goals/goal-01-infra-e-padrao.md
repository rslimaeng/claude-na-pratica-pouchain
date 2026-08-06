# Goal 01 · Infra + o padrão de aula

> **Onda 1 de 9.** Esta é a onda que define o padrão de todas as outras. Se a cara, a densidade e o tom estiverem errados aqui, as 17 aulas seguintes nascem erradas junto.

---

## 1. Escopo

### Entra

| # | Entregável | Caminho |
|---|---|---|
| 1 | Contexto do projeto para o terminal | `CLAUDE.md` |
| 2 | Este goal + índice das ondas | `goals/goal-01-infra-e-padrao.md` · `goals/README.md` |
| 3 | Infra de publicação | `.nojekyll` · `.gitignore` · `README.md` |
| 4 | Tokens de design | `_shared/design-tokens.md` |
| 5 | **Landing** com a trilha visual dos 6 níveis | `index.html` |
| 6 | **Hub do M1** | `m1/index.html` |
| 7 | **Aula 1.1** — O ecossistema e a física | `m1/a1-ecossistema-e-fisica/index.html` |
| 8 | **Aula 1.3** — A regra que fica (+ exercício + gabarito) | `m1/a3-regra-que-fica/` |
| 9 | Esqueleto do kit | `kit/LEIA-ME.md` |

### Não entra (explicitamente)

- Aulas 1.2 e 1.4 → Onda 2
- Qualquer coisa de M2 e M3 → Ondas 3 a 8
- `recursos/` e o `kit-participante.zip` montado → Onda 9
- Planilhas `.xlsx` da Gráfica Aurora — nesta onda os insumos são **`.csv` e `.md`**, porque o M1 roda em chat e o aluno cola texto. As planilhas entram na Onda 3, quando o Cowork aparece.

---

## 2. Por que a 1.3 vem fora de ordem

A **1.1** é a porta de entrada: define a primeira impressão, mas é conceitual e tem exercício leve.
A **1.3** é a aula mais rica do M1 — exercício forte, gabarito, e o **momento uau nº 1** (mesmo prompt com e sem regra fixa, lado a lado).

Fazendo as duas juntas, o Rafael valida **os dois extremos do padrão** de uma vez: a página conceitual e a página de construção com exercício. Se só a 1.1 entrasse, o padrão de exercício só seria testado na Onda 2 — tarde para corrigir.

---

## 3. Decisões tomadas nesta onda (o Rafael confirma ou derruba)

| # | Decisão | O que ficou | Por quê |
|---|---|---|---|
| **D1** | **Empresa fictícia** | **Gráfica Aurora** | Já estava proposta na `ARQUITETURA-PEDAGOGICA.md` §4.5. Resolve o público/privado sem sanitizar citação: a dor aparece como situação da Aurora, que é a rotina deles com outro nome |
| **D2** | **Accent color** | **Azul tinta `#1A5670`** sobre o creme Claude | Referência à tinta de impressão, legível sobre creme (contraste ~7:1), profissional e neutro. Sem identidade visual da Pouchain disponível nos insumos |
| **D3** | 🔴 **`/context` sai do exercício da 1.1 e vira demonstração** | O aluno **compara prompt vago × específico no chat**. O `/context` roda na tela do Rafael | `/context` é comando de terminal. Em M1 ninguém instalou Code ainda. **Exercício que exige o que o aluno não tem trava a sala.** Ver gate G8 |
| **D4** | 🔴 **O artefato da 1.3 é "as regras da minha função", não "um CLAUDE.md"** | O mesmo texto entra hoje nas **Instruções do Project** e vira o `CLAUDE.md` no M2 | É o eixo duplo em ação: mesmo conceito, superfícies diferentes. Chamar de "CLAUDE.md" em M1 força o aluno a criar um arquivo que ele ainda não tem onde colocar |
| **D5** | **De/Para com a ementa fica visível em toda aula** | Chip `Ementa 1.2` no hero + nota no rodapé da aula | A ordem pedagógica troca ementa 1.2↔1.4. Sem o De/Para, o cliente lê reordenação como item faltando |

**D3 e D4 são correções de projeto, não preferências.** Se derrubadas, a aula quebra ao vivo.

---

## 4. Arquivos a criar

```
site/
├── CLAUDE.md
├── README.md · .nojekyll · .gitignore
├── _shared/design-tokens.md
├── goals/
│   ├── README.md
│   └── goal-01-infra-e-padrao.md
├── index.html
├── m1/
│   ├── index.html
│   ├── a1-ecossistema-e-fisica/
│   │   ├── index.html
│   │   └── exercicio/pedidos-em-producao.csv
│   └── a3-regra-que-fica/
│       ├── index.html
│       ├── exercicio/minhas-regras-PARTIDA.md
│       └── gabarito/minhas-regras-GABARITO.md
└── kit/LEIA-ME.md
```

---

## 5. 🚦 Os 8 gates de qualidade

**Nenhuma onda fecha com gate reprovado.** Cada gate tem verificação mecânica — auditoria de conteúdo não substitui `grep` de componente. Esta lição é do Mallory, onde o `.md` estava limpo e o HTML estava pela metade.

### G1 · Estrutura — a anatomia está inteira?

Toda página de aula tem os 8 blocos + destino + checkpoint + hook + nav.

```bash
for f in m1/*/index.html; do
  echo "== $f"
  for m in "O que você vai saber fazer" "A situação" "O conceito" "Como funciona" \
           "Demonstração" "Sua vez" "Confira" "Pegadinhas" "A cerca" \
           "checkpoint" "hook-frase" "nav-bottom" "chip-ementa"; do
    printf "  %-32s %s\n" "$m" "$(grep -ci "$m" "$f")"
  done
done
```
**Reprova se:** qualquer contagem = 0.

> ⚠️ **Usar `grep -ci`, com o `-i`.** O caixa-alta dos títulos vem do CSS (`text-transform:uppercase`), não da fonte. Um gate case-sensitive reprova página correta — foi o que aconteceu na primeira rodada da Onda 1.

### G2 · Gabarito escondido — dá para tentar antes de ver?

```bash
grep -c "<details" m1/a3-regra-que-fica/index.html      # ≥ 1
grep -c "open>" m1/a3-regra-que-fica/index.html         # deve ser 0
```
**Reprova se:** não há `<details>`, ou há `<details open>`. Gabarito aberto não é exercício, é demonstração.

### G3 · Higiene de dados — nada real vaza

```bash
grep -rniE "pouchain" --include="*.html" --include="*.csv" --include="*.md" m1/ kit/ index.html
grep -rniE "(zenith|GE )" --include="*.html" --include="*.csv" m1/
```
**Reprova se:** o nome do cliente aparece **dentro de insumo, exemplo ou dado**. Aparecer no `CLAUDE.md` e no rodapé como "quem contratou" é esperado e correto.
**Reprova também se:** houver qualquer nome de pessoa real, número vindo do material interno de consultoria, ou nome de sistema real da casa.

> 🔒 **Este repositório é público.** Nada de material interno de consultoria entra aqui — nem em `.md` de governança. A regra vale para o repo inteiro, não só para as páginas.

### G4 · Fatos técnicos — tudo rastreável

Toda afirmação técnica cruza com `../FATOS-VERIFICADOS.md`. Todo número de produto carrega data.

```bash
grep -oE "(200 mil|1M|[0-9]+ (mil )?tokens|[0-9]+%|R\$ ?[0-9]|US\$ ?[0-9])" m1/*/index.html index.html
```
**Reprova se:** algum número de produto aparece sem "verificado em DD/MM/AAAA" por perto.

### G5 · Didática — cabe na cabeça de quem está na sala?

Verificação humana, com critério fechado:

| Critério | Reprova se |
|---|---|
| **Máx. 2-3 conceitos por aula** | A seção `02 · O CONCEITO` introduz 4 ou mais ideias novas |
| **Analogia passa no teste AP11** | Precisa de Google para entender. Testar: gestor de indústria em Fortaleza pega de primeira? |
| **Hook aponta para a aula seguinte** | O hook é retórica genérica ("e tem muito mais!") em vez da trava concreta que a próxima aula resolve |
| **A dor é situação, não citação atribuída** | Alguém identificável aparece |
| **Jargão traduzido** | "token", "contexto", "retrieval" aparecem sem uma frase de tradução ao lado |

### G6 · Navegação — nenhum link morto

```bash
grep -ohE 'href="[^"#h][^"]*"' index.html m1/index.html m1/*/index.html \
  | sed 's/href="//;s/"//' | sort -u
```
Conferir um a um se o caminho existe.
**Reprova se:** qualquer link relativo aponta para arquivo inexistente. **Aula com botão de download quebrado quebra na sala.**

### G7 · Render — a página abre e se comporta

```bash
python3 -c "import html.parser,sys
class P(html.parser.HTMLParser):
  def __init__(s):super().__init__();s.st=[]
  def handle_starttag(s,t,a):
    if t not in ('meta','link','br','img','hr','input'):s.st.append(t)
  def handle_endtag(s,t):
    if s.st and s.st[-1]==t:s.st.pop()
    else:print('DESALINHADO',t)
p=P();p.feed(open(sys.argv[1]).read());print('abertas ao fim:',p.st)" ARQUIVO.html
```
Mais, em cada página: `viewport` presente · `lang="pt-BR"` · `<title>` único · media query de `720px` presente · `prefers-reduced-motion` presente.
**Reprova se:** tag desalinhada, ou falta responsividade. Metade da sala abre no celular no intervalo.

### G7-ter · 🔴 Classe usada sem CSS — a lição do Mallory, generalizada

**O gate que pegou o defeito real desta onda.** Como cada página é single-file, uma classe pode ser usada no HTML e não existir no `<style>` daquela página — o componente aparece **cru**, sem borda, sem fundo, sem nada. Conteúdo perfeito, componente pela metade. Nenhuma leitura de texto pega isso.

```bash
for f in index.html m1/index.html m1/*/index.html; do
python3 - "$f" <<'PY'
import re,sys
src=open(sys.argv[1],encoding='utf-8').read()
style="\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))
body=re.sub(r"<style>.*?</style>","",src,flags=re.S)
used=set()
for m in re.findall(r'class="([^"]+)"', body): used.update(m.split())
missing=sorted(used-set(re.findall(r"\.([A-Za-z][\w-]*)", style)))
print(f"{'FALHA' if missing else 'OK   '}  {sys.argv[1]}", missing or "")
PY
done
```
**Reprova se:** qualquer classe aparece na lista. **Sem exceção conhecida** — se uma classe é só marcador semântico, dê a ela uma regra CSS de uma linha. Gate com exceção permanente para de ser gate.

### G8 · 🔴 Exercício executável — o aluno consegue fazer AGORA?

O gate mais importante, e o que nenhuma ferramenta pega sozinha.

| Pergunta | Reprova se |
|---|---|
| O exercício exige só o que o aluno tem **naquele ponto do curso**? | Aula de M1 pede terminal, instalação, Cowork ou Code |
| O arquivo de partida **existe** e baixa? | O `href` aponta para arquivo que não está no repo |
| O insumo funciona **sem upload de arquivo**? | Em M1 o dado não pode depender de anexo — tem que dar para colar no chat |
| O gabarito é alcançável a partir da partida? | O gabarito tem seções que a partida não pede |
| Cabe no tempo declarado? | Exercício de 12 min que leva 30 |
| Tem callout "o seu vai ser diferente"? | Falta — e aí gestor não-técnico trava achando que errou |

---

## 6. Matriz de auditoria desta onda

**Rodada em 05/08/2026.** Contagem, não impressão. As contagens de classe incluem a definição no CSS — por isso "7 linhas de nível" aparece como 13.

| Componente esperado | Onde | Verificação | Contagem | Veredicto |
|---|---|---|---|---|
| Trilha dos 7 degraus (níveis 0-6) | `index.html` | `grep -c 'nivel-row'` | 13 = 6 CSS + **7 linhas** | ✅ |
| 4 pré-requisitos antes de rolar | `index.html` | `grep -c 'pre-req-item'` | 7 = 3 CSS + **4 itens** | ✅ |
| 6 setores na dor-mãe | `index.html` | `grep -c 'setor-nome'` | 7 = 1 CSS + **6 setores** | ✅ |
| 4 cards de aula no hub | `m1/index.html` | `grep -c 'aula-card'` | 8 = 4 CSS + **4 cards** | ✅ |
| Chip de ementa nas duas aulas | `m1/*/index.html` | `grep -c 'chip-ementa'` | 2 e 2 (CSS + uso) | ✅ |
| Anatomia completa (13 marcadores) | `m1/*/index.html` | G1 com `-i` | todos ≥ 1 | ✅ |
| `<details>` presente e **fechado** | ambas as aulas | G2 | details=1 · `open`=0 | ✅ |
| Callout "o seu vai ser diferente" | ambas as aulas | `grep -c` | 1 e 1 | ✅ |
| Cerca 🔒 nas duas aulas | `m1/*/index.html` | `grep -c 'callout-cerca'` | 4 e 4 (CSS + uso) | ✅ |
| Botão copiar funcional | `m1/*/index.html` | `grep -c 'data-copy'` | a1: 2 botões · a3: 1 botão | ✅ |
| Arquivos de exercício existem | `a1/` `a3/` | `ls` | 3 arquivos, 1.8–5.2 KB | ✅ |
| Tags HTML balanceadas | 4 páginas | G7 parser | 4/4 OK | ✅ |
| `lang` · `viewport` · `title` · mq720 · reduced-motion | 4 páginas | G7-bis | 4/4 completos | ✅ |
| **Classe sem CSS** | 4 páginas | **G7-ter** | 🔴 **1 falha → corrigida** | ✅ após fix |
| Links relativos vivos | 4 páginas | G6 | 15/15 resolvem | ✅ |
| Zero "Pouchain" em insumo/exemplo | tudo publicado | G3 | 0 | ✅ |
| Zero número de produto sem data | tudo | G4 | 0 (só larguras de CSS) | ✅ |
| Máx. 2-3 conceitos por aula | `m1/*/index.html` | G5 | 2 e 2 | ✅ |
| CSV suja como prometido | `a1/exercicio/` | contagem | 18 linhas · 3 formatos de data · 1 linha em branco · 1 coluna com espaço · status em 2 caixas · 1 valor sem separador | ✅ |
| Exercício de M1 sem terminal | `m1/*/index.html` | G8 | 0 ocorrências | ✅ |

### 🔴 O defeito que a auditoria pegou

**`m1/a3-regra-que-fica/index.html` usava `.prompt-box`, `.prompt-toolbar`, `.prompt-btn` e `.prompt-content` sem ter o CSS delas.** O bloco de prompt copiável teria aparecido **cru** — texto solto, sem caixa, sem botão estilizado, sem fonte mono.

Nenhuma leitura do conteúdo pegaria isso: o texto estava certo, a estrutura estava certa, o botão existia. **Só a contagem de classe × CSS pega.** É exatamente o padrão do Mallory, e é por isso que o `G7-ter` virou gate permanente.

Corrigido: CSS adicionado. Reverificado: 4/4 OK.

**Segundo achado, menor:** a classe `.back` do `nav-bottom` era marcador semântico sem CSS nas 3 páginas internas. Recebeu uma regra de uma linha, em vez de virar exceção do gate.

---

## 7. Registro de teste de mesa (Rafael) 🔴

O passo que só ele pode fazer: **rodar o exercício de verdade e conferir se a saída bate com o que o gabarito promete.**

| Aula | Rodado em | Saiu como esperado? | O que divergiu |
|---|---|---|---|
| 1.1 · prompt vago × específico | | | |
| 1.3 · regras da minha função | | | |

**Por que é inegociável:** um exercício que promete uma saída e entrega outra quebra na frente de 20 pessoas, ao vivo, sem chance de recuperar. Nenhuma auditoria de código detecta isso — só rodar detecta.

---

## 8. Critérios de aceite da onda

- [ ] Os 8 gates passam
- [ ] Matriz de auditoria preenchida com contagem
- [ ] Rafael abriu no navegador e aprovou densidade, tom e cara da página
- [ ] Rafael rodou os 2 exercícios (teste de mesa registrado)
- [ ] D1 a D5 confirmadas ou derrubadas por escrito
