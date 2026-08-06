# Design tokens · Claude na Prática (Pouchain)

Referência humana dos tokens. **Cada página HTML replica esses tokens no `<style>` inline** — mantém cada arquivo single-file portável, que é o que permite abrir a página sem servidor, num pen drive ou offline na sala.

Base herdada do Workshop Maria Pitanga, com o accent trocado.

## Cores

```css
/* Fundo e superfícies */
--bg:            #F0EEE6;   /* creme Claude — fundo principal */
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

/* Accent — AZUL TINTA (referência à tinta de impressão) */
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
- `localStorage` sempre com prefixo `pcp-` (Pouchain Claude na Prática) — evita colisão com outros sites do Rafael
- Grid responsivo: colapsa em `900px` e `720px`
- `@media (prefers-reduced-motion:reduce)` em toda página

## Componentes (Onda 1)

| Classe | Uso |
|---|---|
| `.site-header` + `.brand` + `.chip` | Header sticky, todas as páginas |
| `.crumbs` | Breadcrumb mono, páginas internas |
| `.chip` · `.chip-accent` · `.chip-ementa` | Pílulas de metadado. `.chip-ementa` marca o De/Para com a ementa vendida |
| `.trilha` + `.nivel-row` | **A trilha dos 6 níveis.** Só na landing — é o mapa que a pessoa consulta o curso inteiro |
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

**Fonte da verdade:** `m1/a3-regra-que-fica/index.html` — é a página mais completa. Copiar e adaptar.
