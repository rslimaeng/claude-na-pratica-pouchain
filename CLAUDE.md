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
| 1.1 Onde abrir, e por que ele piora no meio da conversa | 1.1 O ecossistema Claude em 2026 |
| 1.2 Pedir de um jeito que a primeira resposta já sirva | 1.4 Prompting como conversa vs como sistema |
| 1.3 A regra que fica | 1.2 CLAUDE.md, o manual do funcionário |
| 1.4 O mapa: skill, comando, MCP, plugin | 1.3 Skills, plugins, MCPs e comandos |

Sem esse De/Para visível, o cliente lê a reordenação como item faltando.

**Vale também para o nome do módulo.** O hub do M1 se chama *Escolher a ferramenta certa e onde guardar cada coisa*, e a ementa vendida chama *Módulo 1 · Fundamentos do Ecossistema Claude*. O chip `Ementa · Módulo 1` no hero e a nota de cobertura no rodapé fazem a ponte. **Trocar nome sem mostrar o De/Para é o que faz o cliente achar que sumiu conteúdo.**

## 3. A tese que unifica as 12 horas

> **Toda camada do Claude existe para resolver o mesmo problema: gestão de contexto.**

A pergunta que o aluno leva para casa: *"esta informação precisa estar no contexto sempre, às vezes, ou nunca?"*

## 4. A dor-mãe, o caso condutor

Os 6 setores fazem **literalmente a mesma coisa** com nomes diferentes:

> **Exporto relatório do sistema → colo numa planilha → monto na mão → decido.**

Toda aula ancora nessa dor. Nunca em "produtividade" genérica.

Frase de abertura do curso (citação neutra, não identificável, autorizada): *"o problema é que quando eu vou pedir de novo ele faz de outro jeito."*

## 5. 🔤 Os 6 níveis · o nome que vai para a tela

**Esta tabela é a fonte da verdade do texto.** Aprovada pelo Rafael em 07/08/2026. Nenhuma página inventa nome novo para nível; copia daqui.

A estrutura pedagógica (por que a ordem é essa, o que cada nível ensina) fica em `../TAXONOMIA-CURSO.md` §5. Aqui ficam **as palavras**.

| # | O que vai para a tela | No Claude é | A trava que ele resolve | Excel | Nome interno |
|---|---|---|---|---|---|
| 0 | **Por que ele piora na conversa longa** | Chat · Janela de contexto | *"por que ele fica burro na conversa longa?"* | a célula tem tipo | a física |
| 1 | **Pedir uma vez e receber pronto** | Chat | *"a resposta vem genérica e eu reescrevo tudo"* | fórmula | pedir |
| 2 | **Ele já começa sabendo as suas regras** | Project · Instruções · `CLAUDE.md` | *"reexplico quem eu sou e como a casa funciona toda vez"* | tabela nomeada | contextualizar |
| 3 | **Cada tarefa puxa o seu próprio procedimento** | Skill · Comando | *"cada tarefa tem um método, e pôr tudo junto piorou"* | tabela dinâmica | procedimentar |
| 4 | **Ele abre os arquivos onde você trabalha** | Cowork · Conector (MCP) | *"ele não enxerga meus arquivos, eu vivo copiando e colando"* | conectar na fonte | alcançar |
| 5 | **Você prova que está certo antes de mandar** | Checklist · rubrica · hook | *"tudo bem, mas como é que eu sei que está certo?"* | validação de dados | conferir |
| 6 | **Roda sem você apertar o play** | Rotina agendada · plugin | *"ainda sou eu que aperto o play toda manhã"* | macro | delegar |

**A última coluna existe só para nós.** Ela aparece no HTML como comentário, nunca como texto visível. Ver §7-bis · P1.

> ⚠️ **O nível 2 é que fecha o laço com a frase de abertura do curso.** *"Quando eu vou pedir de novo ele faz de outro jeito"* é respondida na aula 1.3, que é o nível 2, não no 3. O nível 3 é sobre a tarefa ter método próprio, que é outra coisa.

**Eixo duplo:** capacidade (vertical, é a progressão) × superfície (horizontal: Chat · Project · Cowork · Code). O aluno aprende **6 capacidades**, não 4 ferramentas vezes 6 capacidades.

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

## 7-bis. Como a promessa é escrita

**Pedido do Rafael em 07/08/2026**, depois de analisarmos como um curso concorrente comunica as mesmas funcionalidades.

O objetivo: um coordenador da Pouchain abre a página e reconhece **a própria rotina**, não uma lista de recursos.

> ⚠️ **A andragogia não muda.** O esqueleto continua sendo destino → origem → conceito → aplica → hook, a regra de 2 a 3 conceitos e o validador. O que estes 4 padrões mudam é a **superfície**: o nome das coisas e o jeito de prometer.

### P1 · Todo nome carrega duas coisas: a rotina e o recurso oficial

**Formato:** `[o que muda na sua rotina]` com o **nome oficial do Claude visível ao lado**.

| Escreva | Não escreva |
|---|---|
| Ele faz do mesmo jeito toda vez · **Skill** | Nível 3 · Procedimentar |
| Ele abre os seus arquivos · **Cowork** | Módulo Cowork |
| Ele já começa sabendo o seu contexto · **Project** | Nível 2 · Contextualizar |

**Por que os dois juntos:**

- Só a rotina, e a pessoa não sabe o que aprendeu nem consegue pesquisar depois
- Só o nome oficial, e ela não sabe para que serve
- O nome oficial é também o que faz a empresa sentir que comprou **Claude**, e não "um curso de IA"

🔴 **O vocabulário dos níveis é andaime nosso.** *Física, pedir, contextualizar, procedimentar, alcançar, conferir, delegar* serve para **nós** decidirmos a ordem das aulas. **Não vai sozinho para a tela do aluno.** Se aparecer, aparece com a tradução e o recurso ao lado.

**Onde o nome oficial é obrigatório:** trilha da landing · card do hub · chip do hero da aula. Dentro da aula, com o aluno já em contexto, a metáfora pode liderar.

### P2 · Toda promessa tem hora marcada

Capacidade abstrata não gruda. Batida de calendário gruda.

| Escreva | Não escreva |
|---|---|
| Toda segunda o painel reabre atualizado | Você aprende a criar painéis |
| Antes da reunião de PCP o relatório já está pronto | Automatize seus relatórios |
| No fechamento do mês, a conferência já vem feita | Ganhe produtividade no fechamento |

Use a rotina real dos 6 setores: fechamento do mês · reunião de segunda · apontamento de turno · triagem de currículo · cotação de fornecedor · acompanhamento de OS.

### P3 · 🔴 Nomeie a espera, nunca a pessoa

**Isto é regra de segurança de posicionamento, não de estilo.**

O que dói no gestor não é falta de habilidade, é **depender de alguém que tem fila**. Nomear a fila é o que faz a sala se reconhecer. Só que este curso é in-company, e **as pessoas dessa fila estão na sala**.

| Escreva | ❌ Nunca escreva |
|---|---|
| Você deixa de esperar o relatório de terça | Você não precisa mais do analista |
| A montagem manual sai do seu caminho | Substitui o trabalho do assistente |
| O dado chega pronto para a sua decisão | Corta a etapa do time de apoio |

**Mesmo mecanismo, sujeito diferente: a espera é o vilão, a pessoa nunca é.** Curso vendido para indivíduo pode ser cru aqui. O nosso não pode. Ver `../TAXONOMIA-CURSO.md` §11.

### P4 · Diga o que estas 12 horas não fazem

Bloco **visível**, na landing e na abertura, não rodapé.

Faz dois trabalhos de uma vez:

1. Evita que 20 pessoas cheguem ao M3 achando que vão aprender a programar
2. Diz ao gestor que ele é o protagonista do material, não o convidado que veio assistir a um curso de TI

O conteúdo já existe: é a **Cerca 0** da abertura. Falta estar na tela.

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

## 8-quater. Coluna de leitura e breakout

A página tem **duas larguras, e só duas**:

| Token | Valor | Quem usa |
|---|---|---|
| `--col` | `780px` | `.wrap`, a coluna de leitura. **Toda prosa enche ela inteira** |
| `--col-wide` | `1140px` | header, breadcrumb, e as figuras que estouram a coluna |

**Prosa não tem `max-width` próprio.** A coluna já é a medida. Nove larguras diferentes dentro de um `.wrap` largo é o que faz o texto parecer órfão, e foi o defeito que o Rafael reportou na Onda 1.

**Figura, tabela e grade estouram para `--col-wide`**, com a regra `BREAKOUT` no fim do `<style>`. Diagrama mais largo que o texto é intencional e lê como editorial; texto mais estreito que o diagrama, sem motivo, lê como quebrado.

**O número que manda:** ~80 caracteres por linha. Acima de 90 a leitura cai de verdade. Confira medindo, não estimando: `ch` no Inter vale ~1,34 caractere, então a conta de cabeça erra em 30%.

## 8-quinquies. 🔴 A frase não pode quebrar no meio

Dois jeitos de quebrar uma frase sem perceber, os dois já aconteceram aqui:

1. **`display:block` num seletor de tag inline.** `.pre-req-item strong{display:block}` pega *todo* `<strong>` do bloco, inclusive o que está dentro de um `<p>`. A frase parte em duas e a segunda metade começa com vírgula. Gate **G11**.
2. **`display:flex` ou `display:grid` no pai**, com texto solto e tag inline como irmãos. Cada pedaço vira um item de flex e a frase se espalha. Gate **G11b**.

**Como escrever sem cair:** rótulo que precisa ser bloco ganha **classe** (`.rot`), nunca seletor de tag. Container flex tem **um elemento por item**, nunca texto solto ao lado de tag.

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
[✅ CONFIRA VOCÊ MESMO]           ← o validador. Critério objetivo, o aluno confere sozinho
[✅ checkpoint] [➜ HOOK] [nav-bottom]
```

**Dois detalhes de UX inegociáveis:**

1. **O gabarito fica atrás de `<details>`.** Aberto, ninguém tenta. É a diferença entre exercício e demonstração.
2. **O hook fecha toda página.** Não é retórica, é o que faz 19 aulas serem uma corrente, não uma lista. Na última aula do módulo ele fecha o **módulo**, e não a aula.
3. **O validador não pergunta "ficou bom?".** Ele é a camada 1 do harness traduzida: cada item é contável ou é sim/não, e diz para onde voltar se falhar. Critério que depende do instrutor não entra, porque numa sala de 20 o instrutor não escala.

### 🔴 A seção 04 é roteiro para executar, nunca resultado para olhar

**Correção do Rafael em 07/08/2026**, e ela derruba a versão anterior desta seção. Eu tinha escrito "toda aula mostra a saída pronta antes do exercício", e ele reprovou:

> *"Eu quero o exemplo pronto para executar na frente deles, e não algo que eu vou clicar e aparece já feito. A ideia é eles verem acontecendo e fazer similar. Entender o motivo de isso ter acontecido."*

**O que estava errado:** mostrar o resultado pronto entrega o conceito já resolvido. O aluno vê mágica, e mágica não se aprende, se assiste. **A ordem andragógica é experiência → pergunta → conceito**, nunca conceito → ilustração.

**Toda aula tem um roteiro de demonstração**, em página própria, ligado da seção 04. Cada momento traz, nesta ordem:

| Bloco | O que é |
|---|---|
| **O que você faz** | A ação concreta: abrir, anexar, colar |
| **O prompt** | Literal e copiável. Nunca "escreva algo como" |
| **🔴 Aponte isto na tela** | O dedo no que importa, senão passa batido |
| **Pergunte à sala** | A pergunta que eles respondem **antes** de você explicar |
| **Por que este momento existe** | O conceito, só depois de a sala ter vivido ele |
| **Se der errado** | O plano B, escrito antes de precisar |

**O bloco que não pode faltar é "pergunte à sala".** É o que separa demonstração de aula. Referência: `m1/a1-ecossistema-e-fisica/demonstracao/`.

> ⭐ **O padrão de ouro é o momento 3 da 1.1:** a sala dita as correções do pedido vago, o instrutor anota no quadro, e no momento 5 o pedido situado **é reconhecido como delas**. Sempre que der para a sala escrever a resposta sem saber que escreveu, faça isso.

**E o resultado pronto?** Continua existindo, com **dois papéis, os dois depois**: comparar com o que o aluno fez, e ser o plano B se a geração travar ao vivo. Nunca "olhe antes de tentar". Exemplo: `m1/a1-ecossistema-e-fisica/exemplo/`.

**Regra de ouro que sobreviveu:** todo resultado mostrado é gerado **dos dados reais do insumo daquela aula**, nunca inventado. Um exemplo que não bate com a planilha ensina o aluno a perseguir o que ele não vai conseguir. Conferido pelo gate **G13**.

## 9-bis. 📊 Texto corrido longo é defeito, não estilo

**Complemento do §8-bis, com o critério que faltava.** O Rafael mandou dois desenhos de referência e a regra que sai deles:

> **Nenhuma seção de aula passa de dois parágrafos seguidos sem uma figura, uma tabela ou um bloco estruturado.** Lista numerada de cinco itens em prosa é texto corrido disfarçado.

**Três estruturas que resolvem quase tudo**, e vieram das referências dele:

| Estrutura | Quando usar | Onde já existe |
|---|---|---|
| **Colunas paralelas com cabeçalho** | Comparar dois ou três caminhos, campo a campo | `.caminhos` da 1.1 · `.os` da 1.2 |
| **Faixas empilhadas com rótulo lateral** | Uma coisa que tem camadas ou lugares | `.mapa` da 1.4 · `.pilha` da 1.3 |
| **Barra segmentada com legenda** | Quanto de X está ocupado por Y | `.ctx` da 1.1 · `.cam-mesa` |

**Piso por aula: 3 figuras.** Ao fechar uma aula, contar. Se tiver menos, a aula está explicando com palavra o que dava para mostrar.

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
- Toda onda fecha com **`python3 goals/gates.py`**, rodado da raiz do repo. Sai com código 1 se algo falhar. Auditoria de leitura não substitui gate mecânico
- **Gate com exceção permanente deixa de ser gate.** Se um gate acusa, conserta o código. E gate que procura uma palavra não pode rodar contra o arquivo que enuncia a regra sobre ela, senão se auto-reprova
- Nenhuma onda começa antes de o Rafael validar a anterior no navegador
- `.nojekyll` obrigatório na raiz (impede o Jekyll de renderizar `.md`)

## 12. Modelo mental do Rafael

Rafael é PM não-técnico. **Ele decide, o terminal executa.** Ele valida no navegador e roda o exercício de verdade (teste de mesa).

- **Verdade > conforto.** Se o goal está estranho, dizer antes de executar.
- **Comunicação enxuta.** Bullets > parágrafos.
- **Nunca perguntar decisão de produto ao terminal**. Perguntar ao Rafael.
