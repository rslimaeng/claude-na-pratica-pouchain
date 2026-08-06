# CLAUDE.md · Site do curso "Claude na Prática" (Pouchain)

## 1. Contexto

Material de apoio de um **treinamento in-company presencial de 12 horas** na **Pouchain Indústria Gráfica**, conduzido pelo Rafael Lima.

- **Formato:** 12h · 3 módulos · presencial
- **Turma:** ~20 participantes de **6 setores**: Comercial, Compras, PCP, Financeiro, DP, RH
- **Perfil:** gestores, coordenadores e analistas que **já usam o Claude Chat**. Não são técnicos. Vocabulário operacional-tático, zero jargão de programação sem tradução
- **O site é o material que fica depois do curso**, o "PPT deles", só que navegável e vivo

**Repo público:** https://github.com/rslimaeng/claude-na-pratica-pouchain
**Site publicado:** https://rslimaeng.github.io/claude-na-pratica-pouchain/

> 🔒 **O repositório é público, e isso vale para os `.md` de governança também.** Nada de material interno de consultoria entra aqui: nem número, nem nome de pessoa, nem achado de diagnóstico. Se precisar registrar algo assim, vai em `../`, fora deste repo.

**Documentos que mandam neste projeto** (ficam um nível acima, em `../`):

| Arquivo | O que decide |
|---|---|
| `PLANO-DE-PRODUCAO.md` | As 9 ondas, o protocolo de 3 passos, anatomia de página e de exercício |
| `TAXONOMIA-CURSO.md` | A progressão de 6 níveis e a grade das 19 aulas (§8) |
| `DIDATICA-E-HARNESS.md` | Método GPS, os 7 elementos de aula, o validador em 3 camadas |
| `FATOS-VERIFICADOS.md` | **Fonte da verdade técnica.** Nenhuma afirmação técnica entra sem passar aqui |
| `ARQUITETURA-PEDAGOGICA.md` | Ementa (é contrato), universo fictício |

## 2. A ementa é contrato, a ordem das aulas não é

A ementa vendida define os **módulos e os subtemas**. O número de aulas dentro deles e a **ordem** são decisão pedagógica nossa.

**De/Para obrigatório**, toda página de aula exibe qual item da ementa ela cobre:

| Aula do site | Cobre na ementa |
|---|---|
| 1.1 O ecossistema e a física | 1.1 O ecossistema Claude em 2026 |
| 1.2 Pedir para entregar | 1.4 Prompting como conversa vs como sistema |
| 1.3 A regra que fica | 1.2 CLAUDE.md, o manual do funcionário |
| 1.4 O mapa: skill, comando, MCP, plugin | 1.3 Skills, plugins, MCPs e comandos |

Sem esse De/Para visível, o cliente lê a reordenação como item faltando.

## 3. A tese que unifica as 12 horas

> **Toda camada do Claude existe para resolver o mesmo problema: gestão de contexto.**

A pergunta que o aluno leva para casa: *"esta informação precisa estar no contexto sempre, às vezes, ou nunca?"*

## 4. A dor-mãe, o caso condutor

Os 6 setores fazem **literalmente a mesma coisa** com nomes diferentes:

> **Exporto relatório do sistema → colo numa planilha → monto na mão → decido.**

Toda aula ancora nessa dor. Nunca em "produtividade" genérica.

Frase de abertura do curso (citação neutra, não identificável, autorizada): *"o problema é que quando eu vou pedir de novo ele faz de outro jeito."*

## 5. Os 6 níveis (a espinha)

| # | Nível | A trava que resolve | Excel |
|---|---|---|---|
| 0 | A física | *"por que ele fica burro na conversa longa?"* | a célula tem tipo |
| 1 | Pedir | *"a resposta vem genérica e eu reescrevo tudo"* | fórmula |
| 2 | Contextualizar | *"reexplico quem sou toda vez"* | tabela nomeada |
| 3 | Procedimentar | *"cada tarefa tem um método"* | tabela dinâmica |
| 4 | Alcançar | *"ele não enxerga meus arquivos"* | conectar à fonte |
| 5 | Conferir | *"como sei que está certo?"* | validação de dados |
| 6 | Delegar | *"ainda sou eu que aperto o play"* | **macro** |

**Eixo duplo:** capacidade (vertical, é a progressão) × superfície (horizontal: Chat · Project · Cowork · Code). O aluno aprende **5 conceitos**, não 4 ferramentas × 5 conceitos.

## 6. Regras duras de conteúdo

1. **Zero nome de pessoa real.** Em lugar nenhum, nem em exemplo, nem em planilha, nem em citação.
2. **Zero dado da Pouchain nos insumos.** Todo insumo pertence à **Gráfica Aurora**, indústria gráfica fictícia.
3. **Nada que venha do material interno de consultoria entra no site.** Esse material fica fora deste repositório. O que chega aqui é sempre reescrito como situação genérica da Gráfica Aurora.
4. **Fonte Anthropic ganha de creator, sempre.** Contradições registradas em `FATOS-VERIFICADOS.md`.
5. **Nenhum número de produto sem data.** Escrever "verificado em DD/MM/AAAA".
6. **Nomenclatura de creator vai rotulada** (ex.: "as 4 primitivas" é vocabulário de creator, não da Anthropic).
7. **ROI em horas de pessoa, nunca em dólares de token.** O público não decide orçamento.
8. **A dor não se inventa**, mas entra sempre como *situação* da Gráfica Aurora, nunca como citação atribuída a alguém.

## 7. Voz e tom

- Português-BR direto. Frase curta.
- Explicar como se explica para um profissional inteligente que **não é técnico**, não como se explica para um júnior de TI.
- Analogias do mundo deles: **Excel, gráfica, OS, tiragem, papel, prazo de máquina, turno**. E o Excel sempre que couber, porque é o sistema-de-trabalho de 6/6 setores.
- **Teste obrigatório da analogia (AP11):** funciona para gestor de indústria em Fortaleza sem buscar no Google? Se não, troca.
- Tom parceiro, não professor. Sem "vale destacar", sem "cabe mencionar".
- Emoji só em callout curto pontual. **Nunca** em card decorativo.

### 🔴 Proibido: travessão

**Nenhum travessão (o traço longo, `U+2014`) em lugar nenhum.** Nem em prosa, nem em título, nem em `<title>`, nem em comentário de CSS. Hífen normal em palavra composta continua valendo.

Use pontuação portuguesa normal:

| Onde você ia pôr travessão | Escreva assim |
|---|---|
| ligando duas ideias da mesma frase | vírgula: `Traga a sua planilha, e é nela que vamos trabalhar` |
| anunciando o que vem depois | dois-pontos: `A conversa longa piora: vendo a mesa encher` |
| corrigindo ou contrapondo | ponto e frase nova, ou `não é X, é Y` |
| separando aposto no meio da frase | parênteses, ou duas vírgulas |
| entre título e subtítulo | ponto médio: `Aula 1.1 · O ecossistema` |

**Por quê:** pedido direto do Rafael. O travessão dá um tom de texto traduzido e aparecia em excesso. Verificado pelo gate **G9**.

## 8. Base visual

- **Paleta:** creme Claude `#F0EEE6` (fundo) + **azul tinta `#1A5670`** (accent, referência à tinta de impressão) + Inter + JetBrains Mono
- **Tokens em `_shared/design-tokens.md`.** Cada página replica os tokens no `<style>` inline, o que mantém single-file portável
- **Estética:** minimalista. Sem gradiente, sem glassmorphism, sem dark mode. Cards com borda sutil e fundo levemente tingido derivado da cor semântica. **Nunca** border-left grossa colorida

## 8-bis. 📊 Sempre que der para explicar com desenho, desenhe

**Regra permanente, pedido do Rafael.** Conceito abstrato explicado em texto corrido é o que o aluno esquece primeiro. Antes de escrever três parágrafos explicando um mecanismo, pergunte: **dá para mostrar isso?**

| Conceito | Virou |
|---|---|
| A conversa longa enche a janela | Três barras horizontais (mensagem 3 · 20 · 40) com as faixas mudando de tamanho |
| A dor-mãe dos 6 setores | Fluxo de 4 caixas, com a última destacada como "isto continua seu" |
| As instruções se empilham e não brigam | Pilha de 4 camadas somando numa faixa só, mais a variante do conflito |
| Encher dilui | Grade de páginas: 3 páginas com 1 acerto × 40 páginas com 8 parecidos |

**Como construir:**

- **HTML e CSS puro.** Sem biblioteca de gráfico, sem imagem, sem SVG externo. Cada página continua single-file
- **Reaproveite os componentes que já existem** antes de inventar um novo. `.ctx` (barras), `.fluxo` (etapas), `.pilha` (camadas), `.dilui` (grade) já estão prontos e documentados em `_shared/design-tokens.md`
- **Cor sempre semântica**, nunca decorativa. Verde é o certo, âmbar é o parecido, vermelho é o problema, azul tinta é o accent
- **Toda figura tem uma frase de leitura embaixo**, dizendo o que a pessoa deveria ter reparado. Figura sem legenda vira enfeite
- `aria-hidden="true"` em seta e elemento puramente decorativo
- Colapsa no `720px` sem virar papa

## 8-ter. Formato dos arquivos de insumo

| Para | Use | Nunca |
|---|---|---|
| Planilha, relatório exportado, base de dados | **`.xlsx`** | `.csv` |
| Documento, norma, procedimento, contrato | **`.docx`** | `.txt` |
| Prompt para copiar e colar | **`.md`** | outro |

**Por quê:** `.csv`, `.txt` e `.md` não são os formatos que a sala usa no trabalho. Abrir um `.xlsx` de verdade, com cabeçalho mesclado e coluna torta, é o exercício. Um `.csv` limpinho ensina o caso que não existe.

**A sujeira é de propósito e precisa estar lá:** cabeçalho mesclado antes da tabela, data em formatos diferentes, coluna com espaço no nome, status em duas caixas, valor ora número ora texto, linha em branco no meio.

## 9. Anatomia fixa de página de aula

```
[header sticky · breadcrumb · chip "Módulo 1 · Aula 3 de 4"]
HERO  kicker + H1 + subtítulo + chips [Nível] [artefato] [pré-requisito] [ementa]
🎯 O QUE VOCÊ VAI SABER FAZER     ← o DESTINO
01 · A SITUAÇÃO                   ← a ORIGEM. A sala se reconhece
02 · O CONCEITO                   ← 1, no máximo 2 + 💡 Analogia
03 · COMO FUNCIONA
04 · DEMONSTRAÇÃO                 ← o que o Rafael mostra ao vivo
05 · SUA VEZ · N MIN              ← download da partida + passos numerados
06 · CONFIRA · GABARITO           ← ATRÁS DE <details>
07 · PEGADINHAS
08 · 🔒 A CERCA                   ← "neste nível, o que nunca pode acontecer"
[✅ checkpoint] [➜ HOOK] [nav-bottom]
```

**Dois detalhes de UX inegociáveis:**

1. **O gabarito fica atrás de `<details>`.** Aberto, ninguém tenta. É a diferença entre exercício e demonstração.
2. **O hook fecha toda página.** Não é retórica, é o que faz 19 aulas serem uma corrente, não uma lista.

## 10. Regra dura de exercício

**O exercício só pode exigir o que o aluno tem naquele ponto do curso.**

M1 roda em **Claude Chat e Project**, o aluno ainda não instalou Cowork nem Code. Comando de terminal em exercício de M1 é bug, não escolha. Se o conceito precisa de terminal para ser visto, ele vai para a **demonstração na tela do Rafael**, não para o exercício.

Gabarito **não é resposta certa única**, é versão de referência. Vem sempre com o callout: *"O seu vai ser diferente do meu, e tudo bem. Compare a estrutura, não o conteúdo."* Sem isso, gestor não-técnico trava achando que errou.

**Planilha de exercício é suja de propósito**: coluna com espaço no nome, data em formato misto, linha em branco no meio. Planilha real é suja. Uma planilha limpa demais ensina o caso que não existe.

## 11. Disciplina de execução

- **Autor de todos os commits:** `Rafael Lima <rslima.eng@gmail.com>`. O trabalho é dele; os commits não mencionam o Claude Code
- **Nunca** `--amend` em commit já pushado · **nunca** `push --force` · **nunca** `--no-verify`
- 1 onda = 1 goal em `goals/goal-NN-slug.md`, escrito **antes** de a onda começar
- `goals/README.md` mantém a tabela das 9 ondas
- Toda onda fecha com os **10 gates de qualidade** do `goal-01` §5, verificados por `grep`. Auditoria de conteúdo não substitui `grep` de componente
- Nenhuma onda começa antes de o Rafael validar a anterior no navegador
- `.nojekyll` obrigatório na raiz (impede o Jekyll de renderizar `.md`)

## 12. Modelo mental do Rafael

Rafael é PM não-técnico. **Ele decide, o terminal executa.** Ele valida no navegador e roda o exercício de verdade (teste de mesa).

- **Verdade > conforto.** Se o goal está estranho, dizer antes de executar.
- **Comunicação enxuta.** Bullets > parágrafos.
- **Nunca perguntar decisão de produto ao terminal**. Perguntar ao Rafael.
