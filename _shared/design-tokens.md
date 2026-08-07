# Design tokens · Claude na Prática (Pouchain)

Referência humana dos tokens. **Cada página HTML replica esses tokens no `<style>` inline**, o que mantém cada arquivo single-file portável, que é o que permite abrir a página sem servidor, num pen drive ou offline na sala.

Base herdada do Workshop Maria Pitanga, com o accent trocado.

## Cores

```css
/* Fundo e superfícies */
--bg:            #F0EEE6;   /* creme Claude · fundo principal */
--bg-elev:       #FFFFFF;   /* elevação (cards) */
--bg-warm:       #E8E6DC;   /* creme mais escuro (chips, toolbars) */
--bg-code:       #F5F3EA;   /* fundo de bloco de código */

/* Texto */
--text:          #141413;
--text-muted:    #3D3D3A;
--text-dim:      #87867F;

/* Bordas */
--border:        rgba(20,20,19,.10);
--border-strong: rgba(20,20,19,.18);

/* Accent · AZUL TINTA (referência à tinta de impressão) */
--accent:        #1A5670;   /* accent principal · contraste ~7:1 sobre o creme */
--accent-dark:   #10394C;   /* hover */
--accent-soft:   #DDEAF0;   /* fundo tingido para chip e callout accent */
--accent-tinted: #F4F9FB;   /* card accent bem sutil */
--accent-line:   rgba(26,86,112,.22);

/* Semânticas */
--success:       #2E7D32;
--success-soft:  #F4F9F4;
--warning:       #B8860B;
--warning-soft:  #FCF7E8;
--danger:        #B85C5C;
--danger-soft:   #FBF5F5;
```

## Tipografia

```css
--font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', 'Menlo', monospace;
```

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

## Radius e sombras

```css
--radius-sm: 6px;
--radius:    10px;
--radius-lg: 14px;

--shadow-sm: 0 1px 2px rgba(20,20,19,.04), 0 1px 3px rgba(20,20,19,.06);
--shadow-md: 0 4px 12px rgba(20,20,19,.06), 0 2px 4px rgba(20,20,19,.04);
```

## Regras de estilo

- **Nunca** border-left grossa colorida em card ou callout. Preferir fundo tingido derivado da cor semântica + dot pequeno via `::before` no título
- Emoji só em callout curto pontual, **nunca** em card decorativo
- Header sticky com `backdrop-filter: blur(10px)` sobre `rgba(240,238,230,.92)`
- Sem gradiente, sem glassmorphism, sem dark mode
- `localStorage` sempre com prefixo `pcp-` (Pouchain Claude na Prática), evita colisão com outros sites do Rafael
- Grid responsivo: colapsa em `900px` e `720px`
- `@media (prefers-reduced-motion:reduce)` em toda página

## Componentes (Onda 1)

| Classe | Uso |
|---|---|
| `.site-header` + `.brand` + `.chip` | Header sticky, todas as páginas |
| `.crumbs` | Breadcrumb mono, páginas internas |
| `.chip` · `.chip-accent` · `.chip-ementa` | Pílulas de metadado. `.chip-ementa` marca o De/Para com a ementa vendida |
| `.trilha` + `.nivel-row` | **A trilha dos 6 níveis.** Só na landing, é o mapa que a pessoa consulta o curso inteiro |
| **`.fluxo` + `.fluxo-passo` + `.fluxo-seta`** | 📊 Etapas de um processo em sequência. `.final` destaca a etapa que continua sendo humana. Colapsa em coluna no `900px`, com a seta girando 90° |
| **`.ctx` + `.ctx-bar` + `.ctx-seg`** | 📊 Barra de ocupação segmentada. Usada para a janela de contexto enchendo ao longo da conversa. Serve para qualquer "quanto de X está ocupado por Y" |
| **`.pilha` + `.pilha-camada` + `.pilha-result`** | 📊 Camadas que somam num resultado único. Variante `.conflito` pinta as camadas que brigam. Usada para o empilhamento das instruções |
| **`.dilui` + `.pag`** | 📊 Grade de páginas com `.certa` (verde) e `.parecida` (âmbar). Mostra diluição de busca: 3 páginas × 40 páginas |
| `.pre-req` | Bloco de pré-requisitos da landing |
| `.aula-card` | Card de aula no hub do módulo |
| `.step` + `.step-num` + `.step-title` | Bloco numerado de seção de aula (01…08) |
| `.card` · `.card-accent` | Card base e card tingido |
| `.callout` + `.callout-info` / `.callout-warn` / `.callout-cerca` | Aviso, regra e a cerca de governança |
| `.compare` | 2 colunas lado a lado (antes × depois, vago × específico) |
| `.table-wrap` | Wrapper com `overflow-x` para tabela responsiva |
| `.prompt-box` + `.prompt-toolbar` + `.btn-copy` | Bloco de prompt copiável com toast |
| `.download-card` | Cartão de download de arquivo de partida |
| `.gabarito` (`<details>`) | Gabarito atrás de toggle. **Nunca com `open`** |
| `.checkpoint` | "Você sabe fazer X, Y, Z" no fim da aula |
| `.hook` | A trava que a aula não resolve → abre a próxima |
| `.nav-bottom` | ← anterior · próxima → |

**Fonte da verdade:** `m1/a3-regra-que-fica/index.html`, é a página mais completa. Copiar e adaptar.

## Componentes da Onda 2

| Classe | 📊 | O que mostra | Nasceu em |
|---|---|---|---|
| `.checagem` | | O validador de fim de aula. Item objetivo + como conferir + para onde voltar | todas as 4 aulas |
| `.rodadas` | 📊 | Quantas idas e vindas cada versão do pedido custou, em caixinhas | 1.2 |
| `.os` | 📊 | A ordem de serviço da gráfica ao lado da OS de um pedido, campo a campo | 1.2 |
| `.exemplos` | | O mesmo conceito no setor de cada um, em accordion. Abre e roda | 1.2 e 1.4 |
| `.mapa` | 📊 | Onde cada tipo de regra mora, em cinco faixas. Artefato impresso do M1 | 1.4 |
| `.rot` | | Rótulo que precisa ser bloco. **Use esta classe**, nunca `display:block` num seletor de tag inline | todas |

## Componentes da Onda 3 · linguagem de rotina

Nasceram ao aplicar os 4 padrões de `CLAUDE.md` §7-bis.

| Classe | 📊 | O que mostra | Onde |
|---|---|---|---|
| `.rec` | | **Chip do recurso oficial do Claude.** Variante `.livre` (cinza) para o que não exige instalar nada, ou seja níveis 0 e 1 | trilha · hub · hero das aulas |
| `.nivel-rec` | | A célula da trilha que empilha os chips `.rec` | landing |
| `.fluxo-mata` | 📊 | Dentro de cada etapa da dor-mãe, qual nível a elimina. Usa `margin-top:auto` para colar na base e alinhar as caixas | landing |
| `.fluxo-base` | 📊 | A faixa que diz que os níveis 0 a 2 não removem etapa nenhuma, e por que vêm antes assim mesmo | landing |
| `.nao-faz` + `.nao-item` + `.nao-mas` | | O bloco "o que estas 12 horas não fazem". Rótulo com `.rot`, nunca `strong` puro | landing |
| `.destino-quando` | | A promessa com hora marcada, embaixo da lista do destino. Rótulo com `.rot` | 4 aulas |

## Componentes da Onda 3-bis · o aluno não começa em branco

| Classe | 📊 | O que mostra | Nasceu em |
|---|---|---|---|
| `.caminhos` + `.cam` | 📊 | **Colunas paralelas com cabeçalho.** Dois ou três caminhos comparados campo a campo. A estrutura de referência que o Rafael mandou | 1.1 §04 |
| `.cam-mesa` | 📊 | Barra da janela de contexto miniaturizada, dentro de uma coluna de comparação | 1.1 |
| `.bif` + `.bif-fora` | 📊 | **A bifurcação.** Uma pergunta, três respostas, três lugares. `.bif-fora` é o caso que a pergunta não cobre | 1.4 §02 |
| `.ver-pronto` | | Cartão que leva ao artefato pronto. Fica **antes** do exercício, não depois | 1.1 §04 |
| `.fig-leg` | | A frase de leitura embaixo da figura. Era regra do `CLAUDE.md` §8-bis e não tinha classe | 1.4 |

**Página de exemplo pronto:** `m1/a1-ecossistema-e-fisica/exemplo/`. Tem identidade visual própria (Fraunces serif, off-white quente, azul-noite e terracota) **de propósito**: ela mostra o que o pedido situado manda gerar, não o que o site é. Moldura do site em cima, documento embaixo, CSS de impressão A4 embutido.

### Layout

- `--col: 780px` é a coluna de leitura. Prosa enche ela inteira, sem `max-width` próprio
- `--col-wide: 1140px` é o breakout. Figura, tabela e grade saem da coluna
- A regra `BREAKOUT` fica no **fim** do `<style>`, porque precisa ganhar o `margin-left` do componente
