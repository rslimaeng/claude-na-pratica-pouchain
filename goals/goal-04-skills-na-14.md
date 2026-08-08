# Goal 04 · Onda 27 · A 1.4 vira a aula de fazer skill

> **Branch:** `onda-27-skills-a14` · **base:** `7bfa515` na `main`
> **Pedido do Rafael em 07/08/2026, à noite**, depois de ler a 1.4 inteira pela primeira vez.
> **Status:** 🟡 na branch. Só vai para a `main` se ele aprovar no navegador.

## Por que esta onda existe

A 1.4 era a menor aula do M1 (3.913 palavras) e a única que nunca tinha passado por uma
rodada de revisão do Rafael. Ela também mudou na onda anterior **sem ninguém olhar o
conteúdo**, porque três correções de layout entraram nas quatro aulas de uma vez.

O pedido dele, em uma frase: *"o grande entregável aqui dessa aula é a pessoa aprender a
fazer as skills."*

## Os cinco achados, e o que cada um virou

### 1. 🔴 A abertura contradizia a 1.3, e a contradição era minha

A seção 01 abria com *"Meu texto de regras já tem duas páginas"* e o destino prometia
agir *"na primeira vez que o seu texto passar de duas páginas"*. Quer dizer: **o gatilho
da aula era tamanho**.

Só que na onda 3-decies a 1.3 passou a dizer o contrário, com um exemplo real de 128
linhas funcionando: *o tamanho é consequência do critério, não é o critério*. Eu corrigi
a 1.3 e não olhei a aula seguinte, que herdava a régua antiga.

**Virou:** o gatilho passa a ser **mistura**, não tamanho. A aula agora abre com as
regras funcionando e o método faltando, mostra os dois caminhos que a pessoa tenta
(colar o método nas instruções × explicar na hora) e fecha com um callout que **nomeia a
contradição de frente**, citando as 128 linhas da 1.3 para dizer que tamanho nunca foi
o critério.

> A lição, que já estava na memória e voltou: **corrigir uma aula sem varrer o que ela
> alimenta deixa a contradição viva a um clique de distância.**

### 2. A ponte 1.3 → 1.4 não estava clara

*"Eu não sei se está bem claro aqui essa situação, de um pro outro."*

**Virou:** a seção 01 diz explicitamente o que a 1.3 resolveu (as regras que ficam) e o
que ela não resolve (o método de uma tarefa), e o caminho B fecha com a frase de abertura
do curso: *"o problema é que quando eu vou pedir de novo ele faz de outro jeito"*. Ela foi
resolvida para as regras, na 1.3, e voltou para o método.

### 3. O conceito 2 precisava ficar mais didático

O conceito estava certo e o Rafael gostou dele. Faltava o **mecanismo** e um **número
que a sala sinta**.

**Virou:** a diferença entre instrução e cerca deixa de ser de força e passa a ser de
mecanismo (*ele lê e decide · a tranca não lê e não decide*), e o "uma vez em cem" ganha
tamanho: 40 propostas por mês são uma proposta errada a cada dois meses e meio.

### 4. A seção 03 precisava ficar mais clara

**Virou:** a tabela de ganha/paga foi encurtada célula a célula, a última coluna passou a
ser *"é o lugar certo quando"* e ganhou legenda dizendo o que reparar. E a seção abre
declarando o recorte: **dos cinco lugares, quatro você reconhece e um você constrói.**

### 5. 🔴 A parte de skill era o entregável e ocupava um parágrafo

**Virou o corpo da aula.** Nove blocos novos, nesta ordem:

| Bloco | O que faz |
|---|---|
| `.anat` | A skill `fechar-cotacao` inteira, campo a campo, com a coluna **quando carrega** |
| `.hab` | A tela **Habilidades** reproduzida, com uma skill real e o rótulo "por Você" |
| `.vitrine` | Os três níveis de leitura: sempre · quando escolhe · quando precisa |
| `.versus` | Prompt salvo × skill, linha a linha |
| `.norma` | **A sua empresa já escreveu a skill**: limites · quem aprova · o anexo que ninguém lê |
| `.demo` + `.prompt-box` | O caminho dos 3 passos, com o pedido de empacotar literal e copiável |
| `.vsp` | Skill × Project: **verbo × substantivo**, e por que os dois juntos |
| `.adv` | Até onde vai: uma skill de 292 linhas, e o formato é o mesmo |

## As decisões que precisam do seu aval

### A · O exemplo grande é o `advisor-jeff-bezos`, e não o arquivo inteiro

Das 11 skills do board, escolhi essa por dois motivos:

1. **Passa no teste AP11.** Hormozi, Roberge, Verna e Chen não são nomes que um gestor de
   indústria em Fortaleza reconhece sem buscar. Bezos, Jobs e Musk são.
2. **O segundo framework dele é o conceito 2 desta aula.** Separar decisão reversível de
   irreversível e gastar tempo só na segunda é, palavra por palavra, o *"se ele esquecer
   isso uma vez em cem, qual o tamanho do estrago?"*. O exemplo não só impressiona, ele
   **reforça o que a aula acabou de ensinar**.

**O que eu não fiz, e por quê:** as 11 skills são amarradas a uma pessoa real e a uma
empresa que não são suas, com o nome delas em todo parágrafo. Publicar o arquivo num
repo público não é nosso para fazer. **A página mostra a anatomia** (nome, descrição,
as cinco seções, o tamanho), nunca o conteúdo.

### B · O módulo passa a ter três artefatos, e não dois

Se a pessoa sai sabendo fazer skill mas não faz uma, o entregável não aconteceu. O
exercício foi de 4 para **7 passos**, o validador ganhou a **checagem de que a skill
entra sozinha**, e o item final passou de "os dois artefatos" para "os três". Mexeu em
4 lugares: a 1.4, o card do hub, o hero e o checkpoint.

> **Correção do Rafael na primeira olhada:** *"o tópico 5 não tá no mesmo padrão."*
> Ele estava certo. Os passos 1 a 4 são título mais uma frase; o 5 tinha virado três
> parágrafos com três ações empilhadas (escolher, empacotar, testar). Virou **três
> passos curtos**, no mesmo ritmo dos outros. As alturas agora são 83 · 83 · 108 ·
> 108 · 83 · 83 · 83 pixels, contra os ~250 do passo 5 anterior.

### C · Os prints viraram HTML, e não imagem

Você pediu print da tela e de uma skill sua. Reproduzi as duas **em HTML e CSS**, que é o
padrão que a 1.3 já usa (`.tela`, `.painel`) e o que mantém a página single-file, sem
imagem binária, responsiva e legível no celular. A tela **Habilidades** e a skill
`pesquisa-mercado-oportunidades` estão campo a campo, fiéis ao seu print.

## Os gates novos

| Gate | O que trava |
|---|---|
| **G20** | A skill `fechar-cotacao` é **a mesma** na aula e na demonstração: nome, tamanho recalculado do arquivo, número de passos e as duas palavras-gatilho |
| **G21** | Todo tamanho grande citado na 1.4 sai de um arquivo real: as 292 linhas do `.skill` e as 128 do `00-System_Instruction.md` da 1.3. Pula alto se o insumo não existir na máquina |
| **G22** | A tela é nomeada como a tela nomeia (**Habilidades**, **por Você**) e a anatomia mostra as três partes na ordem |
| **G23** | Toda referência a `passo N` aponta para passo que existe naquela aula. Nasceu ao quebrar o passo 5 em três: o validador continuou mandando voltar ao 5, que virou outro |

**Os quatro foram provados contra defeito injetado**, em cópia isolada do repo, com o
defeito entrando em **uma ocorrência só** (trocar todas faria um gate furado passar).
11 defeitos, 11 reprovados. Total do repo: **27 gates, 216 checagens, exit 0**.

> ⚠️ **O que o G23 não faz, e está escrito no código:** ele confere a **faixa**, não o
> alvo. Se a lista cresce e a referência antiga continua dentro da faixa, ele passa.
> Para o alvo certo não existe checagem mecânica, é leitura.
>
> A primeira tentativa de prova dele foi **mal desenhada por mim**: o defeito que eu
> injetei criava uma classe órfã, e o **G7-ter pegou antes**, o que me daria um falso
> "reprovou". Defeito injetado tem que testar **só** a regra em questão.

## Dois consertos que apareceram no caminho

1. **O botão de copiar da 1.4 e o da demonstração não tinham fallback.** Usavam só
   `navigator.clipboard`, sem `catch`. Quando a permissão é negada, o botão ficava mudo.
   Ganharam os três caminhos que a 1.3 já tinha, e o terceiro **avisa a pessoa** em vez de
   falhar em silêncio. Verificado no navegador: a permissão foi negada, caiu no fallback,
   e o aviso apareceu.
2. **Dois números que eu inventei**: escrevi "27 linhas" para uma skill de 19 e "293" para
   um arquivo de 292. Os dois agora são recalculados por gate.

## O que continua faltando

- 🔴 **Teste de mesa**, e ele é seu: fazer uma skill de verdade pelo caminho dos 3 passos
  e ver se o passo 2 devolve mesmo uma skill utilizável.
- 🟡 Confirmar que a tela se chama **Habilidades** numa conta que não é a de instrutor.
  Mesma dúvida aberta do campo "Contexto" na 1.3.
- 🟡 O exercício da 1.4 ainda baixa um `.docx`, diferente da 1.2 e da 1.3, que já têm
  quadro preenchível na página. Aqui a impressão é o ponto, então o `.docx` se defende.
  Se você quiser o quadro preenchível também, é uma onda curta.
