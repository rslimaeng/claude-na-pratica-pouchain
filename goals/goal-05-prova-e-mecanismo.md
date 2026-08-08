# Goal 05 · Onda 28 · A prova do /context e o mecanismo da tranca

> **Base:** `35a53a9` na `main`, com a onda 27 já publicada.
> **Pedido do Rafael em 08/08/2026**, em duas mensagens seguidas, logo depois de
> aprovar a 1.4 e mandar publicar o M1.
> **Status:** ✅ publicada.

## Os dois pedidos, e o que cada um virou

### 1. A foto do `/context`

> *"Adicione essa foto para colocar aqui nessa parte que explica o consumo dos
> tokens, acredito que ajudará a entender. Pode ser depois da explicação, antes
> do 'prompt salvo não é skill'."*

Ele mandou um print do `/context` do Claude Code mostrando **43 skills ocupando
3,9 mil tokens, 0,4% da janela**. A seção da vitrine afirmava, em prosa, que
*"você pode ter quarenta skills e a mesa continua vazia"*. A foto é essa frase
com número medido em cima, e a coincidência do 43 com o "quarenta" virou parte da
legenda em vez de ser escondida.

**As quatro decisões que a foto exigiu:**

| Decisão | O que foi feito | Por quê |
|---|---|---|
| **Recorte** | Cortados os 420px de cima | Tiravam o cabeçalho, as dicas de TUI e o caminho `/Users/rafaellima`. O repositório é público |
| **Peso** | 337 KB → **50 KB** (85% menor), paleta de 64 cores | É terminal, tem pouca cor. Nenhuma perda de legibilidade |
| **Não redesenhar em HTML** | Ficou imagem, ao contrário da tela de Habilidades | Reproduzir em CSS **tiraria dela o que ela tem de valor**, que é ser medição e não afirmação nossa |
| **Celular** | Rola dentro da própria caixa, com piso de 700px | Em 341px o texto do terminal era ilegível. Mesmo tratamento das tabelas da página |

**A ressalva que a legenda carrega, e é a parte mais importante:** a tela é do
**Claude Code, no terminal**, e o M1 inteiro promete que ninguém precisa de
terminal. Sem isso escrito, uma sala que passou o módulo no Chat conclui que
falta instalar alguma coisa. O **G25** trava a página se a ressalva sumir.

> 🟡 **O que eu deliberadamente não escrevi:** a tela também mostra **112
> ferramentas de conector com 0 tokens**, com o rótulo `loaded on-demand`. Era
> tentador dizer *"a vitrine vale igual para o conector"*. Não disse: a tela
> prova isso **no terminal**, e não no claude.ai, onde a turma trabalha.
> Registrado como pendência no `FATOS-VERIFICADOS.md`.

### 2. A explicação da tranca vira aula

> *"Vi aqui sua explicação do conceito da tranca. Acho que vale a pena pegar
> parte dela e colocar na aula para deixar mais didática."*

**Parte**, e não tudo. O filtro foi o de sempre: na página só entra o que é para
o aluno.

| Da explicação | Foi para | Por quê |
|---|---|---|
| A tabela **lê a regra? · decide? · o que acontece quando falha** | ✅ a página | É o mecanismo, e mecanismo se mostra |
| **CAIXA ALTA não muda a regra de linha** | ✅ a página | É o erro que a sala comete, e ninguém tinha escrito |
| **"essa regra é importante?" não separa nada** | ✅ a página | É o pivô de importância para estrago |
| *"Um cuidado seu na hora de falar"* (o número é hipótese) | 🎙️ `ROTEIRO-DE-PALCO-M1.md` | Direção de cena |
| *"Como eu falaria isso na sala"* (os 4 movimentos) | 🎙️ `ROTEIRO-DE-PALCO-M1.md` | Direção de cena |

**A tabela é `<table>` de verdade**, e não um componente novo. Comecei escrevendo
um `.mec` com grid, rótulo lateral e colapso próprio no celular, e joguei fora ao
ver que a página já tinha `.table-wrap` + `<table>`, com scroll horizontal e tudo.
Trinta linhas de CSS a menos, semântica melhor, e o comportamento que o aluno já
encontrou nas outras aulas.

**Sem cor semântica nas linhas, de propósito.** Pintar a tranca de verde diria
que instrução é o caminho ruim, que é o oposto do que a aula ensina: instrução é
a primeira linha, sempre, e serve para a esmagadora maioria das regras.

## O gate novo

| Gate | O que trava |
|---|---|
| **G25** | A prova do `/context`: a imagem existe e é referenciada, declara `src`, tamanho, `loading` e `alt`, **todo número da legenda também está no `alt`**, e a legenda diz que a tela é do terminal e que o aluno não precisa dele |

**Por que o número vive no `alt`:** a imagem é binária, e não dá para ler o
número de dentro dela por gate. O `alt` vira a **cópia declarada**, e a legenda
tem que bater com ele. Assim a legenda não anda sozinha.

> ⚠️ **O que o G25 NÃO faz:** ele não confere a legenda **contra a imagem**. Se
> a foto for trocada por outra, o gate continua verde enquanto legenda e `alt`
> concordarem entre si. Para isso não existe checagem mecânica, é leitura. Os
> números estão no `FATOS-VERIFICADOS.md` para a conferência ser possível.

**Provado contra 5 defeitos injetados**, em cópia isolada, cada defeito em **uma
ocorrência** e com `assert` de premissa antes de injetar. 5 de 5 reprovados, e a
conferência foi a **linha nomeada** do gate, nunca o exit code sozinho.

Total do repo: **29 gates, 234 checagens, exit 0**.

## Um erro do caminho, e ele é conhecido

Ao inserir a foto, o `old_string` da edição era o `<h4>Prompt salvo não é skill</h4>`
e eu não o repus no `new_string`: **apaguei o título ao inserir o bloco antes
dele**. Peguei conferindo com `grep -c` logo depois.

E o `grep` inicial falhou com "no such file or directory", porque um `cd ..` de
três comandos antes **ainda estava valendo**. É a mesma armadilha da onda 27, no
mesmo dia. Caminho absoluto em tudo.

## Conferido no navegador

- Desktop 935px: imagem em 893px, sem rolagem interna, sem overflow de página
- Celular 375px: imagem em 700px rolando dentro da caixa, tabela rolando dentro
  da `.table-wrap`, **`scrollWidth` da página igual ao viewport**
- Console sem erro
- Ritmo da seção 02 conferido depois da edição: prosa e bloco alternando a cada
  2 a 4 linhas, dentro do §9-bis
