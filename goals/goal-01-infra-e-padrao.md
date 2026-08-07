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
| 7 | **Aula 1.1** · O ecossistema e a física | `m1/a1-ecossistema-e-fisica/index.html` |
| 8 | **Aula 1.3** · A regra que fica (+ exercício + gabarito) | `m1/a3-regra-que-fica/` |
| 9 | Esqueleto do kit | `kit/LEIA-ME.md` |

### Não entra (explicitamente)

- Aulas 1.2 e 1.4 → Onda 2
- Qualquer coisa de M2 e M3 → Ondas 3 a 8
- `recursos/` e o `kit-participante.zip` montado → Onda 9
- Planilhas dos outros setores da Gráfica Aurora (compras, ponto, currículos). Nesta onda existe só a de produção; as demais entram junto com as aulas que as usam.

---

## 2. Por que a 1.3 vem fora de ordem

A **1.1** é a porta de entrada: define a primeira impressão, mas é conceitual e tem exercício leve.
A **1.3** é a aula mais rica do M1: exercício forte, gabarito, e o **momento uau nº 1** (mesmo prompt com e sem regra fixa, lado a lado).

Fazendo as duas juntas, o Rafael valida **os dois extremos do padrão** de uma vez: a página conceitual e a página de construção com exercício. Se só a 1.1 entrasse, o padrão de exercício só seria testado na Onda 2, e aí é tarde para corrigir.

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
│   │   └── exercicio/pedidos-em-producao.xlsx
│   └── a3-regra-que-fica/
│       ├── index.html
│       ├── exercicio/minhas-regras-PARTIDA.md
│       └── gabarito/minhas-regras-GABARITO.md
└── kit/LEIA-ME.md
```

---

## 5. 🚦 Os gates de qualidade

> ⚠️ **Esta seção foi substituída.** Ela trazia 10 gates como comandos `bash` para rodar na mão. Eles viraram **[`gates.py`](gates.py)**: 12 gates, uma execução só, saída com código 1 se algum falhar.
>
> ```bash
> python3 goals/gates.py
> ```
>
> A versão antiga continua no histórico do git. **Não copie de lá:** o G1 daquela lista não inclui o validador de fim de aula, e o número de gates mudou.

**O que sobreviveu desta seção e virou regra permanente do projeto:**

- **Nenhuma onda fecha com gate reprovado.** Auditoria de leitura não substitui verificação mecânica. A lição vem do Mallory, onde o `.md` estava limpo e o HTML estava pela metade
- **Gate com exceção permanente deixa de ser gate.** Se o script acusa, o conserto é no código, não no gate
- **Gate que procura uma palavra não pode rodar contra o arquivo que enuncia a regra sobre ela**, senão se auto-reprova
- **Gate case-sensitive reprova página correta.** O caixa-alta dos títulos vem do CSS (`text-transform`), não da fonte

## 6. Matriz de auditoria desta onda

**Rodada em 05/08/2026.** Contagem, não impressão. As contagens de classe incluem a definição no CSS, por isso "7 linhas de nível" aparece como 13.

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

**`m1/a3-regra-que-fica/index.html` usava `.prompt-box`, `.prompt-toolbar`, `.prompt-btn` e `.prompt-content` sem ter o CSS delas.** O bloco de prompt copiável teria aparecido **cru**: texto solto, sem caixa, sem botão estilizado, sem fonte mono.

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

**Por que é inegociável:** um exercício que promete uma saída e entrega outra quebra na frente de 20 pessoas, ao vivo, sem chance de recuperar. Nenhuma auditoria de código detecta isso, só rodar detecta.

---

## 8. Critérios de aceite da onda

- [ ] Os 8 gates passam
- [ ] Matriz de auditoria preenchida com contagem
- [ ] Rafael abriu no navegador e aprovou densidade, tom e cara da página
- [ ] Rafael rodou os 2 exercícios (teste de mesa registrado)
- [ ] D1 a D5 confirmadas ou derrubadas por escrito
