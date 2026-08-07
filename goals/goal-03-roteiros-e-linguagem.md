# Goal 03 · Roteiros de demonstração e linguagem de rotina

**Executada em 07/08/2026**, em rodadas curtas de validação: o Rafael validava um ponto, pedia o ajuste, eu executava, ele passava para o próximo.

**Ponto de retorno anterior:** tag `antes-da-linguagem-de-rotina` (commit `c9d297e`).

## 1. A correção que reorganizou tudo

Eu tinha escrito no processo: *"toda aula mostra a saída pronta antes do exercício"*, e construído uma página de artefato pronto para a 1.1. **O Rafael reprovou:**

> *"Eu quero o exemplo pronto para executar na frente deles, e não algo que eu vou clicar e aparece já feito. A ideia é eles verem acontecendo e fazer similar. Entender o motivo de isso ter acontecido. Lembre-se, o treinamento é prático e andragógico."*

**Por que ele estava certo:** mostrar o resultado pronto entrega o conceito já resolvido. O aluno assiste mágica, e mágica não se aprende. A ordem é **experiência → pergunta → conceito**, nunca conceito → ilustração.

A regra errada estava no `CLAUDE.md` e teria contaminado as 15 aulas seguintes.

## 2. O roteiro de demonstração

Uma página por aula, em `m1/aN-slug/demonstracao/`. Cada momento traz seis blocos:

| Bloco | O que é |
|---|---|
| O que você faz | A ação concreta |
| O prompt | Literal e copiável. Nunca "escreva algo como" |
| 🔴 Aponte isto na tela | O dedo no que importa |
| **Pergunte à sala** | A pergunta que eles respondem **antes** da explicação |
| Por que este momento existe | O conceito, depois de a sala ter vivido |
| Se der errado | O plano B, escrito antes de precisar |

**O bloco que não pode faltar é `pergunte à sala`.** É o que separa demonstração de aula.

### Os quatro momentos de ouro

O padrão é sempre o mesmo: **a sala produz a resposta antes de saber que produziu.**

| Aula | Momento | O que a sala faz |
|---|---|---|
| 1.1 | 3 | Dita as correções do pedido vago. No momento 5 reconhece as próprias palavras no pedido situado |
| 1.2 | 2 | Preenche os três campos da OS em branco. O pedido que roda no momento 3 é o deles |
| 1.3 | 2 | Dita as regras do Project linha por linha, e o instrutor só digita |
| 1.4 | 4 | Classifica três regras em voz alta e **discorda na terceira, de propósito** |

**Cada roteiro tem plano B em todo momento.** O da 1.4 momento 2 é exemplar: se a skill não disparar, o roteiro manda comemorar e consertar a descrição ao vivo, porque nada ensina melhor que "descrição vaga é skill que nunca roda".

## 3. Os 4 padrões de linguagem

Nasceram da análise de um curso concorrente, que o Rafael mandou olhar pela **comunicação**, não pelo conteúdo. Estão em `CLAUDE.md` §7-bis.

| | Padrão |
|---|---|
| **P1** | Todo nome carrega **a rotina e o nome oficial do recurso** |
| **P2** | Toda promessa tem **hora marcada** |
| **P3** | 🔴 Nomeia-se **a espera, nunca a pessoa** |
| **P4** | Diz-se **o que o curso não faz**, em bloco visível |

**O diagnóstico dele:** *física, pedir, contextualizar, procedimentar* é andaime de projeto. Um coordenador de PCP lê "Nível 2 · Contextualizar" e não sabe nem se é a rotina dele, nem qual recurso vai usar.

### O que foi renomeado

| | De | Para |
|---|---|---|
| Módulo 1 | Fundamentos do ecossistema | **Escolher a ferramenta certa e onde guardar cada coisa** |
| Aula 1.1 | O ecossistema e a física | **Onde abrir, e por que ele piora no meio da conversa** |
| Aula 1.2 | Pedir para entregar | **Pedir de um jeito que a primeira resposta já sirva** |
| Aulas 1.3 e 1.4 | | mantidas: já eram linguagem de rotina |

Os **7 níveis** ganharam nome público em `CLAUDE.md` §5, que passa a ser a fonte da verdade do texto.

> ⚠️ **O nome da ementa contratada é outro**, e trocar sem mostrar o De/Para faz o cliente achar que sumiu conteúdo. O hub ganhou chip de ementa e nota de cobertura, igual às aulas.

## 4. Duração saiu da tela

> *"Tire o tempo das aulas. Até pra não gerar uma pressão, vamos manter controle interno só."*

**Mesma convenção que já valia no Mallory.** Tempo no material do aluno não informa, cobra.

| Onde | Tempo |
|---|---|
| Hero, destino, eyebrow, card do hub | ❌ removido, e `.aula-dur` deletada |
| Roteiro de demonstração | ✅ é aqui que vive |
| Landing, no que foi vendido | ✅ contrato |

## 5. Defeitos que a auditoria pegou de graça

1. **A aula 1.3 mostrava números errados.** "Offset 2 com 5" quando são 6, e a OS 2434 como atrasada quando o prazo dela é dali a cinco dias. Virou o gate **G13**, que recalcula do `.xlsx`
2. **As figuras da Onda 2 nunca entraram no breakout.** `.mapa`, `.os`, `.rodadas` estavam presas em 780px desde que nasceram
3. **Duplicação no bloco P4.** "Não te deixa automático em 12 horas" já estava dito, e melhor, no callout de fechamento
4. **Um defeito de mobile anterior a esta onda:** o chip do módulo caía na coluna 1 porque a media query mirava o `<span>` e não o `<div>`

## 6. Gates novos

| Gate | O que pega |
|---|---|
| **G12** | Nome de nível fora da lista aprovada, ou linha da trilha sem o recurso oficial |
| **G13** | Número sobre a Gráfica Aurora que não bate com o `.xlsx` |
| **G14** | Aula sem `demonstracao/`, ou roteiro sem `.pergunta`, `.aponte` e `.planoB` em cada momento |
| **G15** | Duração na tela do aluno, **e roteiro sem duração** |

**G12 e G15 foram testados contra cópias quebradas de propósito** antes de entrar.

**Por que o G12 não é caça-palavra:** *alcançar* e *delegar* são verbos comuns do português e apareceriam em prosa legítima. Conferir a lista aprovada é preciso; caçar palavra proibida gera falso positivo, e gate com exceção deixa de ser gate.

## 7. 🔴 O problema de relógio, aberto e do Rafael

| Aula | Demo | Exercício | Sobra para o resto |
|---|---|---|---|
| 1.1 | 12 | 12 | **1 min** 🔴 |
| 1.2, 1.3, 1.4 | 6 | 12 | 7 min |

**A 1.1 não fecha nos 25 minutos.** Duas saídas:

- **A** · enxugar para 7 min, juntando os momentos 1 e 2
- **B** · aceitar 35 min, porque é a aula de abertura e o momento 3 é o que compra as outras 11 horas

**Recomendação: B.** Mas isso muda a distribuição das 2h do M1, e a conta é do Rafael.

## 7-bis. 🔴 A segunda reprovação: o roteiro rodava no terminal

**07/08/2026, mesmo dia.** O Rafael abriu o roteiro da 1.1 publicado e reprovou de novo:

> *"Já começa dizendo que vai rodar no Claude Code e roda o context. Isso aqui para mim não está nada didático. Eu queria um exemplo similar: o que eles vão fazer. Eu mostrar a diferença, rodando com sequência de prompts, que eu posso simular uma conversa normal e um ali que já vai estar pronto. Esse aqui que você criou, eu achei até anti-andragógico. Tem um monte de cor."*

**Ele estava certo em três frentes de uma vez:**

| | O defeito | Por que é grave |
|---|---|---|
| **Superfície** | Momentos 1, 2 e 4 rodavam no **Claude Code**, com `/context` | Minuto 3 de 12 horas, e a sala olha um terminal que só chega no M3. Três dos cinco momentos estavam marcados *"a sala assiste"*, então não dava para dizer *"agora façam igual"* |
| **Conceito** | `/context` mostra **um número** | A conversa degradando ao vivo mostra a mesma coisa e o aluno **repete sozinho na segunda-feira**. Escolhi a prova mais bonita em vez da que ensina |
| **Superfície visual** | **Seis fundos coloridos por momento**, um por tipo de bloco | Fura o `CLAUDE.md` §8-bis, que já dizia *"cor sempre semântica, nunca decorativa"*. Tipo de bloco não é semântica |

**Eu tinha respeitado a letra do §10** (*conceito que precisa de terminal vai para a demonstração*) **e quebrado o espírito inteiro.** A regra virou R1: primeiro se procura como mostrar o conceito **na superfície do aluno**; terminal é último recurso, não atalho.

### O que a 1.1 é agora

Duas conversas no Claude Chat, 10 minutos de palco:

| # | min | O que acontece |
|---|---|---|
| 1 | 1 | Anexa o mapa de cotação e faz o pedido vago. Ele responde com toda a segurança |
| **2** | **3** | 🔴 *"O que falta nesta resposta para você fechar essa compra hoje?"* A sala dita, vai para o quadro |
| 3 | 2 | Três correções na mesma conversa. Melhora, não fecha, e na terceira ele larga o prazo |
| 4 | 2 | Conversa nova, pedido pronto. *"É o que vocês me disseram há três minutos, só que escrito antes"* |
| 5 | 2 | Sai o documento com dois achados que ninguém tinha visto |

**Insumo novo:** `demonstracao/cotacoes-fornecedores.xlsx`, de **Compras**. O exercício continua com a planilha de PCP. Ver R2.

### 📏 O piso de 50 linhas

A planilha saiu com 15 linhas e o Rafael mandou refazer na hora: *"de cara, já crie uma planilha mais robusta. Algo pelo menos de 50 linhas ou mais."*

**Ele está certo e é conteúdo, não capricho.** Em 15 linhas alguém pensa *"isso eu fazia na mão"*, e a pergunta do momento 1 (*"quanto tempo vocês levariam na mão?"*) perde o efeito. Virou regra no `CLAUDE.md` §8-ter.

**Ficou com 56 linhas:** 14 insumos × 4 fornecedores. E o tamanho comprou uma quarta armadilha, que é a melhor de todas.

| | A armadilha | Quem cai |
|---|---|---|
| 1 | **Prazo.** Insumos Delta é o mais barato por unidade e chega **6 dias depois** de a máquina rodar | o pedido vago, sempre |
| 2 | **Frete.** Delta e Cearapel cotam FOB: mais R$ 890 e R$ 1.240 fora do valor unitário | quase sempre |
| 3 | **Incompleto.** Suprimentos deixou **3 itens** sem cotar e Cearapel deixou 2. O total do "mais barato" nunca existiu | quase sempre |
| 4 | 🔴 **Unidade.** Cearapel cotou a chapa CTP em `cx c/ 10`, e não por unidade. Ler direto multiplica o item por dez | **ninguém acha na mão** |

**O desfecho:** sobra **um único fornecedor** que cotou os 14 itens e entrega a tempo, a Papelaria Norte, e é justamente o mais caro na conta ingênua. É o melhor fecho possível para a aula: o pedido vago escolhe o mais barato **porque ele é incompleto**.

**O G13 recalcula tudo isso** e confere as três frases do momento 5, nas duas páginas. Testado contra cópias quebradas: **5 das 7 checagens reprovam** quando o número muda.

### Efeito colateral bom: o relógio da 1.1 fechou

A demonstração caiu de **12 para 10 minutos**. Com os 12 do exercício, dá 22 nos 25 da aula. **O problema do §7 se resolveu sozinho**, e a distribuição de 2h do M1 não precisa mudar.

### Dívida

**Só a 1.1 está no padrão novo.** Os roteiros da 1.2, 1.3 e 1.4 continuam com as seis cores, o `.papeis`, o `.preparo` em âmbar e o prompt aberto no meio da página. Esperam o Rafael validar a 1.1. Registrado também no `_shared/design-tokens.md`, com o aviso de **copiar da 1.1, nunca das outras três**.

## 7-ter. 🔴 A terceira reprovação: público errado

**07/08/2026, fim do dia.** O Rafael abriu a página publicada e reprovou o **gênero** do texto, não o conteúdo:

> *"É como se você tivesse ensinando pra mim o que eu tenho que fazer. Eu não vou ficar lendo isso para eles. Esse material é o material que eu vou dar aula no curso: o que aparecer de texto e o que eu for ler tem que ser para o usuário final. Eu quero um passo a passo."*

**O erro:** eu escrevi um **roteiro de palco** e publiquei no site do aluno. *Pergunte à sala · espere o silêncio passar · zoom do navegador em 150% · antes de a turma entrar · plano B por momento.* Tudo isso é anotação de bastidor. Na tela do aluno não ensina nada, e ainda faz o instrutor parecer que está lendo instrução de como dar a própria aula.

**O padrão do meu erro, e é o terceiro da série:** eu otimizei para a mecânica pedagógica e esqueci **quem lê**. A andragogia estava certa; o destinatário estava errado.

### O que existe agora

| O que é | Onde |
|---|---|
| Passo a passo, prompts, o que aparece na tela, o que reparar, o que aquilo ensina | `site/m1/aN/demonstracao/` · **público** |
| Pergunta para a sala, quando esperar, quadro, plano B, preparo, minutagem | `../ROTEIRO-DE-PALCO-M1.md` · **interno** |

Os seis blocos permitidos na página pública estão no `CLAUDE.md` §9. **Nenhum passo pode ser só instrução:** todo passo entrega `repare`, `ensina` ou `lista`.

### As planilhas subiram para o piso de 100

> *"Algo sempre mais robusto de 100 ou mais linhas, pois lembre-se da sensação do ganho de produtividade."*

| Planilha | De | Para | O que o volume comprou |
|---|---|---|---|
| `pedidos-em-producao` (exercício, PCP) | 18 | **120 OS** | OS duplicada, cliente com dois nomes, máquina em branco |
| `cotacoes-fornecedores` (demonstração, Compras) | 56 | **104 linhas** | 26 insumos × 4 fornecedores |

**O número que carrega a aula 1.3:** o campo Status marca **4 atrasadas**, a data de prazo diz **30**. E a OS 2442 e a OS 2490 estão as duas com 13 dias de atraso, com o sistema marcando só a primeira.

A página `exemplo/` foi **regerada inteira** dos dados novos, por script: big numbers, tabela das atrasadas, carga das seis máquinas, vence em 3 dias e as três decisões.

### Os gates mudaram de lado

| Gate | Antes | Agora |
|---|---|---|
| **G14** | **exigia** `.pergunta`, `.aponte` e `.planoB` | **reprova 19 frases de direção de cena**, e exige que nenhum passo seja só instrução |
| **G15** | exigia que o roteiro **tivesse** duração | reprova duração em **todas** as páginas do aluno |
| **G13** | 11 checagens | **24**, mais o piso de 100 linhas nas duas planilhas |

**124 checagens no total.**

## 7-quater. Onda 3-ter · o card que apontava para a demonstração

A onda 3-bis limpou as quatro demonstrações e parou ali. Uma varredura de `.html` depois mostrou que **a página de aula estava limpa no corpo e suja no card de saída**, que é o link para a demonstração. Cinco trechos, em cinco arquivos:

| Onde | O que dizia | O que diz agora |
|---|---|---|
| aula 1.1, card | *"a pergunta que a sala responde antes da explicação, e o plano B se travar"* | *"o que reparar em cada passo"* |
| aula 1.2, card | *"Os quatro momentos, com o que apontar em cada um"* · *"O momento 2 é onde vocês preenchem"* | *"Os quatro passos, do pedido de uma frase ao arquivo preenchido"* · *"O passo 3 é a OS com os três campos preenchidos"* |
| aula 1.3, card | *"a sala ditando o que entra no arquivo"* · **"o número muda de 2 para 7"** | *"o arquivo escrito uma vez só"* · **"30 OS atrasadas e o campo Status marca 4"** |
| aula 1.4, card | *"O momento 4 é a sala classificando em voz alta"* | *"três regras reais de uma gráfica e onde cada uma mora"* |
| `exemplo/` | *"resultado do **momento 5 do roteiro**, que o Rafael executa ao vivo"* · *"ser o plano B se a geração travar na sala"* | *"resultado do **passo 5 da demonstração**"* · o plano B saiu (já vive no `ROTEIRO-DE-PALCO-M1.md`, linhas 22 e 84) |

**O 2 para 7 da aula 1.3 era erro de fato, não só de linguagem.** A planilha foi para 120 linhas na onda 3-bis e o corpo da página já dizia 30, mas o card ficou com o número da planilha velha. Foi a mesma varredura que pegou os dois.

### G14b

O **G14** só lê `demonstracao/index.html`. Foi por isso que passou. O **G14b** roda a lista de palco, com `\b`, contra **todo `.html` do site**, mais o vocabulário do roteiro: `roteiro`, `momento N da`, `os quatro momentos`, `com o que apontar`, `executa ao vivo`, `travar na sala`.

Testado contra uma cópia com os cinco textos reprovados de volta: **acusa os cinco**, e não dá falso positivo em *"ninguém nesta sala"* nem em *"o mural na parede da sala"*, que são texto legítimo do aluno.

**16 gates, 136 checagens.**

> A lição, que vale para toda onda futura: **gate que cobre parte da superfície não protege a regra, só o pedaço que ele olha.** Ao corrigir uma página, pergunte o que aponta para ela.

## 7-quinquies. Onda 3-quater · a seção 04, e o exercício da 1.2 que não rodava

Auditoria da aula 1.2 antes de o Rafael abrir. Dois achados, e o segundo é mais grave que todos os anteriores.

### A seção 04 das quatro aulas falava na primeira pessoa do instrutor

O mesmo defeito das três reprovações, no **corpo da aula** em vez da demonstração:

| Aula | O que estava publicado |
|---|---|
| 1.1 | *"**Eu uso** uma planilha de Compras"* · *"**Paro e pergunto para vocês**... o que **vocês responderem vai para o quadro**"* |
| 1.2 | *"**Abro** uma conversa... **leio em voz alta**"* · *"**Vamos contando juntos**"* · *"**Comparo** o relógio"* |
| 1.3 | *"**Mostro** onde ficam as Instruções"* · *"**Jogo** um manual longo... acontecendo **na frente de vocês**"* |
| 1.4 | *"**Faço** um pedido... **Vocês veem**"* · *"**O que eu quero** que fique do passo 3"* |

O eyebrow `Demonstração · na tela do Rafael` virou `Demonstração`, porque o site é o material que fica **depois** do curso e a referência à tela da frente não se sustenta três meses depois. Cada lista virou *"O que acontece na tela"*, e agora dá ao aluno **o que fazer enquanto assiste** (*"conte as mensagens"*, *"pare aqui e responda para você mesmo"*) em vez de descrever quem opera o teclado.

**Dois números velhos vieram junto**, os dois na 1.1: *"nas 56 linhas"* e *"deixou de cotar três itens"*. Conferido na planilha: são **104 linhas** e o mais barato não cotou **5**.

**O G14b ganhou checagem de pessoa gramatical.** Lista de palavra não pegava isto: `leia em voz alta` reprovava e `leio em voz alta` passava. Dentro do bloco `.demo`, verbo em primeira pessoa do singular reprova.

E o próprio gate foi corrigido: **`vocês` sozinho não é defeito.** *"O dia a dia de vocês"* e *"Vocês já resolveram isso, em outro lugar"* tratam a turma como profissionais da gráfica, e são dos melhores trechos do material. O defeito é a turma como **plateia**: `pergunto para vocês`, `na frente de vocês`, `vocês veem`.

### 🔴 O exercício da 1.2 não tinha arquivo para rodar

O passo 3 mandava *"cole o pedido reescrito, conte quantas mensagens até a resposta servir, esse número é a sua nota"*. Os três pedidos-modelo começam com **"Anexei..."**. E não existia arquivo nenhum. O aluno colaria numa conversa vazia e o Claude responderia que não recebeu anexo: **a nota da aula era impossível de medir**.

Pior: a 1.1 entrega PCP, e a 1.2 é a aula que deveria alcançar Compras, Financeiro, DP e RH. Do jeito que estava, **quatro dos seis setores não encostavam em dado real no módulo inteiro**.

Rafael escolheu criar as duas planilhas que faltavam. Cada caso agora tem arquivo:

| Setor | Arquivo | Tamanho | As armadilhas, todas dependentes do volume |
|---|---|---|---|
| Compras | `cotacoes-fornecedores.xlsx` | 104 linhas | as quatro que já existiam. **A pergunta mudou** para *"monta o pedido de compra"*, porque *"qual é a melhor"* era literalmente a demonstração da 1.1 e quem é de Compras já tinha visto a resposta |
| Financeiro | `fechamento-dois-meses.xlsx` | 118 linhas, 2 abas | **3 contas renomeadas** entre os meses · **rateios que variam mais que qualquer causa real** · 28 linhas sem centro de custo |
| RH e DP | `inscricoes-vaga-auxiliar-offset.xlsx` | 124 inscrições, 2 abas | **1 requisito ambíguo** · desejáveis que viram obrigatórios · tempo de casa que induz senioridade falsa |

**Os números que provam que as armadilhas mordem:**

- Financeiro: junho fecha em **+200.500** e julho em **−151.300**. Incluindo os rateios, as três maiores causas são *receita diversos, rateio administrativo, rateio de estrutura*. Excluindo, como o pedido manda, são *receita diversos, papel couché, horas extras*. **Duas das três mudam.**
- RH: a frase *"disponibilidade para trabalhar em turnos"* aprova **53 ou 19** pessoas, conforme a leitura. Diferença de **34 pessoas**, e nenhuma das duas leituras é errada. Exigindo também os três desejáveis, sobra **1 de 53**.

**Zero nome de pessoa**, em lugar nenhum: a triagem é por código `INSC-NNN`, do jeito que triagem cega é feita de verdade. O G13 confere isso.

Tudo saiu de gerador versionado, com `random.seed(2481)`. O `gera_cotacoes.py` passou a gravar em **dois caminhos**, para as duas cópias não divergirem. O docx virou `gera_docx_pedidos.py`, em vez de arquivo escrito à mão.

**16 gates, 144 checagens.**

## 7-sexies. Onda 3-quinquies · o gabarito da 1.3 dizia 4 máquinas

Auditoria da aula 1.3 antes de o Rafael abrir. **Quatro números da planilha antiga sobreviveram**, e o pior estava no gabarito.

O exercício da 1.3 manda escrever as regras da própria função, colar nas Instruções de um Project e rodar **o mesmo pedido vago da 1.1 na mesma planilha**. O gabarito de referência dizia:

> *"Temos 4 máquinas: Offset 1, Offset 2, Flexo 1 e Flexo 2."*

A planilha tem **seis**, e as mesmas seis aparecem no prompt situado da 1.1 e na saída da demonstração da 1.3, **na mesma página**. Quem usasse o gabarito de referência ensinaria ao Claude que Digital 1 e Offset 3 não existem, e **a aula que promete melhorar a resposta entregaria uma pior.**

| Onde | Dizia | Diz |
|---|---|---|
| gabarito 1.3 | "Temos **4** máquinas: Offset 1, Offset 2, Flexo 1 e Flexo 2" | "Temos **seis** máquinas: Offset 1, Offset 2, Offset 3, Flexo 1, Flexo 2 e Digital 1" |
| gabarito 1.1 | "há **18 pedidos**... distribuídos entre **duas** máquinas" | "há **120 pedidos**... distribuídos entre **seis** máquinas" |
| corpo 1.3 | "duas máquinas offset e duas flexográficas" | "três offset, duas flexográficas e uma digital" |
| corpo 1.4 | "uma gráfica com **quatro** máquinas" | "uma gráfica com **seis** máquinas" |

**Ajuste de coerência junto:** o trecho 2 do gabarito citado na página dizia que o relatório sai *"em CSV com ponto e vírgula"*, e o insumo que o aluno baixa é `.xlsx`. Agora descreve a sujeira que o arquivo tem de verdade, **conferida uma a uma**: 2 cabeçalhos mesclados (`A1:I1`, `A2:I2`), coluna `" Tiragem "` com espaço, linha em branco na 63, 3 formatos de data com 80 ocorrências cada, status em três caixas, valor 80 número e 40 texto.

### O G13 cresceu, e a varredura passou a ser do site inteiro

Quatro checagens novas, e **a varredura roda em todo `.html`** em vez de numa lista escrita à mão. Foi exatamente assim que o *"quatro máquinas"* da 1.4 escapou da primeira versão do gate, que só olhava 1.1 e 1.3:

- as seis máquinas citadas em cada página que fala delas
- nenhum texto afirma outro **total**
- **contagem por família**: *"duas offset"* reprova, porque são três. O teste do total sozinho deixava passar
- nenhum texto afirma um total de OS diferente de 120

Testado contra os quatro trechos publicados: **acusa os quatro**, e nomeia o arquivo e a afirmação errada.

O conserto do gabarito virou `corrige_maquinas_gabarito.py`, que **lê a lista de máquinas da planilha**. Rodar de novo não estraga: se o texto já estiver certo, avisa e não grava.

**16 gates, 151 checagens.**

> **A lição, terceira variação do mesmo tema:** o insumo é a fonte da verdade e o texto obedece. Toda vez que uma planilha muda de tamanho, **tudo que a descreve mente até prova em contrário**, inclusive gabarito, exemplo de resposta genérica e prompt de outra aula.

## 7-septies. Onda 3-sexies · enquadramento e a pincelada de loop e grafo

Dois pedidos do Rafael sobre a aula 1.2.

### 1. O bloco largo saía do eixo, e a culpa era da ordem da regra

Print de tela larga: a tabela da OS e o diagrama das rodadas apareciam deslocados para a esquerda. **Medido em 2000px: a prosa centra em 993 e a tabela centrava em 627, desvio de 373px.**

A regra de sangramento alarga o bloco e o recentra com `margin-left:50%` + `transform:translateX(-50%)`. **Qualquer regra posterior com o atalho `margin:` zera o `margin-left`**, e sobra só o transform, que empurra o bloco meia largura para a esquerda. Era o caso de `.rodadas`, `.os` e `.mapa`, nas aulas 1.2 e 1.4. O `.compare` escapava **por sorte**: a regra dele vem antes do sangramento no arquivo.

Conserto: `margin-top` e `margin-bottom`, que não tocam no `margin-left`. Nasce o **G11c**, que reprova classe da lista de sangramento com atalho `margin:` declarado depois dela.

> **Detalhe que quase me enganou:** a primeira versão do detector não achava nada, porque **comentário de bloco `/* */` antes da regra entra no seletor capturado**. Sem remover comentário, o parser lê `.rodadas` como `/* RODADAS */ .rodadas` e não casa. Remover comentário antes de parsear CSS é obrigatório.

### 2. A pincelada de loop e grafo, para quem já foi aluno dele

Parte da turma já fez curso de prompt com o Rafael. Sem diferenciação, a 1.2 soa como **mais do mesmo** para essas pessoas.

Fonte: `insumos/graph-and-loops.md`, 242 linhas, três origens (Greg Eisenberg sobre engenharia de grafos · um vídeo em português sobre loops e grafos · **a conversa do Boris Cherny, criador do Claude Code, no dia seguinte ao lançamento do Opus 5**).

**O achado não é um tópico novo, é uma confirmação.** As três perguntas da aula **são** a formulação nova, dita por quem construiu a ferramenta:

| A pergunta da aula | O nome dele |
|---|---|
| O que é "pronto"? | critério de pronto (*exit criteria*) |
| Quais são as restrições? | limites (*guardrails*) |
| O que fazer na dúvida? | como ele **confere o próprio trabalho** |

E o que **envelheceu** é exatamente o que o veterano aprendeu: **especificar os passos**. Boris chama isso de erro comum, e conta que apagaram **80% das instruções internas do Claude Code** quando o Opus 5 saiu, porque existiam para corrigir coisa que o modelo já faz sozinho.

O bloco entra depois do Conceito 2, com quatro peças: o que mudou · a fala citada e atribuída · a tabela De/Para · onde isso vai dar (loop no M2, grafo no M3). Fecha dizendo explicitamente que **nada disso é necessário para o exercício da seção 05**.

**As duas analogias são da casa, não de software:**

- **Loop:** a tiragem é conferida **contra a prova aprovada**, não contra a lembrança de quem acertou a máquina. Quem fez carrega o motivo de cada decisão, e o motivo atrapalha na hora de julgar.
- **Grafo:** a diferença entre **uma máquina imprimindo dez OS em fila e as seis rodando em paralelo**. O trabalho é o mesmo, o relógio não.

O bloco `.fala` é **sem cor de propósito**: a única caixa colorida da página continua sendo a que o aluno precisa notar (§8-bis).

### A tensão que isso criou, resolvida nas duas aulas

O **"pedido situado"** da aula 1.1 tem **60 linhas**, com `## PAPEL`, `## CONTEXTO`, `## ESTILO DE SAÍDA (CRÍTICO)`, `## TAREFA`, `## ANTES DE GERAR` e `## LINGUAGEM`. O veterano que ler a pincelada da 1.2 e lembrar daquele prompt tem uma pergunta legítima: *"mas vocês acabaram de me mostrar um prompt de sessenta linhas".*

**Rafael pediu para escrever nas duas.** A resposta é a mesma, com peso diferente:

| Onde | O que entrou |
|---|---|
| **1.1**, callout logo depois do prompt | Ele é longo **dizendo o que "pronto" significa**, e em nenhuma linha diz *como* fazer. Cria o gancho para a 1.2, que é onde o conceito tem nome |
| **1.2**, bloco próprio | Tabela De/Para de quatro linhas, fechando em **"descreve o destino"** contra **"dita o trajeto"**. E aponta que o `## ANTES DE GERAR` do prompt da 1.1 **já era a conferência** que a fala chama de mais importante |

A tabela usa exemplos que são a memória muscular do veterano no lado errado: *"primeiro leia o arquivo, depois monte a tabela, depois some a coluna"* · *"use a função SOMASE"* · *"pense passo a passo antes de responder"*.

### O card da fonte, e a primeira imagem do site

Capa do vídeo mais link para o YouTube, ao lado da citação. **A imagem foi recortada do print** por dois motivos: os selos *"289 VPH"* e *"31.8x"* são de uma extensão do Rafael e não são conteúdo, e *"há 11 dias"* é **data relativa**, que apodrece num site que fica depois do curso.

Ficou só a capa, 840×473, JPEG de 56 KB em `_shared/`. Título, fonte, duração e idioma **viraram HTML**: selecionável, responsivo, traduzível e sem data que envelhece. Original em `insumos/assets-fotos/`.

**Dois gates cresceram, porque era a primeira imagem do site:**

- **G6** passa a conferir `src` junto com `href`. Ele olhava só `href`, e caminho de imagem errado passaria em silêncio
- **G6b** exige `alt`, `width` e `height` em toda `<img>`. Sem `width`/`height` o layout pula quando a imagem carrega

> **O G6b nasceu errado duas vezes, e as duas só apareceram testando contra defeito injetado, não lendo o código:**
> 1. `'alt="' in tag` casa dentro de `data-alt="`
> 2. `\balt="` também casa, porque **o hífen já é fronteira de palavra**
>
> Ficou `\salt="`, que exige espaço antes do atributo. É a mesma lição da Regra 5 em outra roupa: **gate não testado é gate que você acha que tem.**

**17 gates, 163 checagens.** (O G6b imprime dentro do título do G6, então não conta como gate separado na contagem de cabeçalhos.)

## 7-octies. Onda 3-septies · o quadro do pedido dentro da página

**Pedido do Rafael em 07/08/2026**, com referência: o canvas do
`workshop-ia-maria-pitanga/m5/`. Na seção 05 da 1.2 o exercício saía do site
(baixar o `.docx`, preencher fora, voltar). Agora ele acontece na página.

### O que o quadro tem

| Bloco | Por que existe |
|---|---|
| Seletor de caso | Ao escolher, aparece **o pedido original como ele foi feito**. É contra ele que a pessoa escreve |
| Três caixas de diagnóstico | O passo *"marque antes de escrever"* virou ação de verdade, não instrução |
| Os três campos | O que é "pronto", as restrições, o que fazer na dúvida |
| Contador de idas e vindas | A nota da aula. **Não entra no texto copiado**, e o quadro diz isso |
| Prévia ao vivo | O pedido se montando enquanto ela escreve. É a tese da aula em movimento |
| Copiar e limpar | Rascunho salvo em `localStorage` |

### A decisão que mudou o exercício

O `.docx` tinha uma caixa livre: *"reescreva aqui"*. O quadro **monta o pedido a
partir das três respostas**. A diferença não é de interface, é de exercício: numa
caixa livre a pessoa conserta o que já tinha percebido, e era exatamente contra
isso que o passo de marcar antes existia.

O texto sai como **pedido escrito**, nunca como formulário colado. Rótulo que
força repetição foi trocado: `Se algo ficar ambíguo:` seguido de uma resposta que
começava com *"Se um valor estiver ambíguo"* virou `Na dúvida:`.

O `.docx` continua na página, agora como botão secundário, para quem prefere
papel. Ele ainda é o único suporte da parte 5.

### 📏 A medida de linha, medida e não estimada

Medido com sonda, no elemento e no tamanho reais: a **14px** o `1ch` vale
8,83px e o caractere médio do português vale 6,87px, ou seja **1ch = 1,28
caractere**. A regra de bolso do projeto (`1,34`) se sustenta. O que estourava
era o texto: `58ch` entrega **74 caracteres** e as duas dicas que quebravam
tinham **77 e 96**. Ficou **62ch**, que dá **79**, o alvo de ~80 do
`CLAUDE.md` §8-quater, e as frases foram encurtadas junto.

Quatro dicas sobravam uma palavra sozinha na segunda linha. Depois de encurtadas,
o maior texto auxiliar do quadro tem 74 caracteres e **os seis cabem em uma linha**.

> A lição, e ela quase me pegou de novo: a primeira medição desta onda deu
> "66 caracteres" porque **o viewport estava em 375px** e eu li a largura de uma
> linha real em vez de sondar o limite. Número medido no estado errado é chute
> com casa decimal. **Sonde o limite, não a linha que calhou de estar ali.**

### O copiar tem dois caminhos

`navigator.clipboard` exige contexto seguro, e o participante pode abrir a página
de um pendrive na sala. A função tenta a API, cai para `execCommand` e, se as duas
falharem, o toast manda selecionar e usar Ctrl+C. A prévia fica visível e
selecionável de propósito, para esse caso.

**Gates:** 17 gates, 163 checagens, exit 0. Quem protegeu esta onda foi o
**G7-ter**: toda classe nova do quadro nasceu com regra de CSS.

## 7-nonies. Onda 3-octies · a 1.3 contra a documentação oficial

**Pedido do Rafael em 07/08/2026:** cruzar a aula 1.3 com `insumos/claude-project.md`,
três vídeos sobre Projects, sendo o primeiro do canal oficial da Anthropic.
*"Não acho que ela esteja ruim, é mais para ver se tem o que melhorar."*

A leitura confirmou que a aula já cobria 9 dos ~14 pontos do insumo, e em vários
casos explica melhor que a fonte. Mas achou **um erro de fato publicado**.

### 🔴 A "decepção nº 1" estava desatualizada

A seção 07 dizia que num Project *"o que fica guardado são as instruções e os
documentos, não o que você conversou ontem"*. **Existe memória por projeto**, e a
segunda metade da frase é falsa. Fonte e detalhes em `../../FATOS-VERIFICADOS.md`.

Por que era P0 e não detalhe: alguém da sala levanta a mão. A memória apareceu no
Claude deles, e a aula perderia autoridade justamente onde pede para escrever um
arquivo de regras.

**A resposta certa reforça a tese.** Virou um bloco novo no Conceito 1, com tabela
memória × instrução e a frase que resolve: **memória é o que ele lembrou,
instrução é o que você mandou.** A pegadinha da seção 07 passou a dizer só o que
continua verdade, mais um callout que remete ao bloco.

### Os três enriquecimentos, e todos viraram figura

O Rafael foi explícito: *"mantenha os elementos didáticos que não são só texto."*
Nenhum acréscimo entrou como parágrafo solto.

| Enriquecimento | Virou | Componente |
|---|---|---|
| A terceira gaveta: o anexo da conversa | Terceira coluna da tabela de gavetas + callout com a pergunta prática *"onde eu ponho a planilha de hoje?"* | `table-wrap` |
| Um projeto, um trabalho | Duas colunas: `"Gráfica Aurora"` contra `"Coordenação de PCP"` | `.compare` |
| O empilhamento já existe no Chat | Pilha de 3 camadas: preferências do perfil, estilo, instruções do projeto | `.pilha` |

Os três **reaproveitaram componente existente**, nenhuma classe nova, nenhum CSS
novo. É o §8-bis do `CLAUDE.md` funcionando: reaproveite antes de inventar.

### A tensão que eu quase criei, e como ficou resolvida

O insumo diz *"one project for one task"*. A aula manda **dar ao projeto o nome da
função**. Escrito sem cuidado, o acréscimo contradiria o exercício da própria aula.

A formulação que resolve não é nenhuma das duas: **o critério é coerência, não
tamanho.** Um projeto cabe quantos pedidos você quiser, desde que o mesmo texto de
regras sirva para todos. O teste que ficou na página: *"as minhas instruções valem
para tudo que eu vou pedir aqui dentro?"* Se a resposta é "para metade", virou dois.

### O que ficou de fora, de propósito

| Ponto | Por quê |
|---|---|
| O nome "RAG" | A figura do "encher dilui" explica melhor que a sigla |
| Salvar planilha como `.csv` | Contradiz o `CLAUDE.md` §8-ter |
| Projeto do Cowork ≠ projeto do claude.ai | É do M2. Na 1.3 seria antecipar assunto |
| *"Projects are the room, skills are the playbook"* | É da **1.4**, que é exatamente sobre isso |

Da distinção projeto × skill, a 1.3 ficou só com o critério de corte, no validador:
**se a regra serve também fora deste projeto, ela não é do projeto.** Uma linha, e
prepara a 1.4 sem invadir.

### Um erro de método que quase se repetiu

A primeira medição da página saiu com `viewport: 0`, porque a aba tinha sido
recriada. Número medido em viewport inválido é número inventado. Refeita a 1280px:
a tabela de 4 colunas cabe em 1138px sem rolar, nenhum bloco fora do eixo, e a
aula fica com **3 pilhas, 1 grade, 5 comparativos e 5 tabelas**, muito acima do
piso de 3 figuras.

**Gates:** 17 gates, 163 checagens, exit 0.

## 7-decies. Onda 3-novies · a didática do M3 do Maria Pitanga na 1.3

**Pedido do Rafael em 07/08/2026**, com quatro prints do
`workshop-ia-maria-pitanga/m3/` e da página de caso dele. O pedido foi preciso:

> *"Os blocos e o visual de como ele se apresenta, eu acho que isso é uma didática
> que a gente pode aproveitar."* E depois, delimitando: *"não o termo de agente,
> mas aí tem toda a parte de como funciona o Project que pode somar."*

**A restrição que ele mesmo colocou é a mais importante.** O M3 do MP fala em
**agente**; o nosso nível 2 fala em **instrução persistente**. Trazer a palavra
puxaria vocabulário do nível 3 (skill) para cá e quebraria a progressão do
`CLAUDE.md` §5. A didática veio, a palavra não. Conferido: `agente` não aparece
em nenhuma das duas páginas.

### O que foi replicado

| Do M3 do MP | Virou na 1.3 | Componente |
|---|---|---|
| §01 Conceito, cards É/Não é | **O que a instrução persistente é, e o que não é.** 6 cards. O primeiro "não é" aponta para a tabela da memória logo abaixo | `.eh` |
| §03 Anatomia, 3 partes fixas | **As três partes e onde cada uma mora**, com exemplo de PCP em cada card e o nome do campo no rodapé | `.anat` |
| §04 Ferramenta, mockup da tela | **A tela do Project** com os dois campos lado a lado e o chat de uso | `.tela` |
| §05 Caso-âncora com arquivos | **Página `exemplo/`** com 3 `.md` para baixar mais a planilha da 1.1 | página nova |

### Por que o mockup era o maior buraco

A aula falava de "Instruções do projeto" e de "documentos" o tempo todo e **nunca
mostrava a tela**. Para quem nunca criou um Project, a diferença entre os dois
campos só fica óbvia vendo os dois lado a lado. Foi o acréscimo de maior retorno.

### Os três arquivos do `exemplo/`

| Arquivo | Onde entra | Por que existe |
|---|---|---|
| `regras-do-coordenador.md` | Campo Instruções | O gabarito em formato de **colar**, não de escrever. O `.docx` continua para quem prefere papel |
| `norma-de-programacao.md` | Campo Conhecimento | **Conteúdo novo**, e o ponto é esse: é material de consulta, não regra. Ordem de prioridade da fila, tempo de preparação, capacidade por turno |
| `pedido-da-vez.md` | Nenhum campo, é o chat | Uma frase, mais 4 variações que mudam o recorte sem mexer no formato |

A `norma-de-programacao.md` foi escrita de propósito como material que **não pode**
estar nas instruções: ninguém precisa da capacidade da Offset 3 em toda conversa.
É a distinção da aula demonstrada em arquivo, não em texto.

### 🔴 O número que eu quase publiquei errado

Escrevi na página que o arquivo de regras tem "32 linhas". Contei: são **27**.
A aula promete *"entre 20 e 40 linhas"*, e um exemplo que não cabe na própria
faixa destrói o critério.

Virou o gate **G13b**, que recalcula três coisas: o arquivo cabe na faixa, tem as
cinco seções, e **nenhuma página afirma um número diferente do real**. Testado
contra dois defeitos injetados numa cópia com caminho absoluto:

1. página dizendo 32 quando são 27 → acusou
2. arquivo estourando a faixa (47 linhas) → acusou as duas checagens

É a Regra 6 outra vez: **insumo é a fonte da verdade, e número que a página afirma
sobre ele precisa ser recalculado, nunca digitado.**

### O custo, declarado

A 1.3 foi de 4.917 para **5.512 palavras**, e continua sendo a maior do módulo.
A justificativa é que ela é a aula do **nível 2**, o que fecha a frase de abertura
do curso. Se na revisão pré-turma ela pesar, o candidato natural a sair é o
comparativo do "encher de escopo", que é o mais recente e o menos ancorado numa
dor da sala.

**Gates:** 18 gates, 177 checagens, exit 0.

## §7-undecies · Onda 3-decies · a tela real como fonte da verdade

**Pedido do Rafael em 07/08/2026**, com quatro prints da conta dele e a pasta
`insumos/exemplos/m1-aula-3/`. Duas frentes: consertar o enquadramento da seção
04 e refazer a página de exemplo no padrão do caso-âncora do Maria Pitanga.

### 🔴 O achado que mais importa: o campo mudou de nome

O painel de um Project em pt-BR mostra **Instruções · Memória · Contexto**. O
site escrevia **"Conhecimento do projeto"** em 6 lugares, que é a tradução do
`project knowledge` do help center em inglês.

**Por que isso não é implicância:** o material existe para 20 pessoas abrirem a
própria tela e acharem o campo. Nome que não está na tela é aula que trava ao
vivo, e trava no pior momento, que é o do exercício.

Trocado nas 6 ocorrências. Virou o gate **G16**, que varre HTML e os `.md`
publicados dentro de `m1/`, e confere também que a tela da 1.3 nomeia os três
blocos. Os `goals/*.md` ficam de fora de propósito: são eles que enunciam a
regra e precisam poder citar o nome velho.

⚠️ **Fica aberto** se "Contexto" é o rótulo de todo mundo ou de um lote de
rollout. Conferir na semana da turma **numa conta que não seja a do instrutor**.

### O que os prints resolveram de graça

| Print | O que ele provou |
|---|---|
| Diálogo *Criar instruções* | *"funcionará junto com suas instruções do perfil e o estilo selecionado"*. A pendência 🟡 do bloco `.pilha` virou ✅, **por texto do produto** e não do help center |
| Diálogo *Gerenciar memória* | *"regenera a memória do projeto todas as noites"* e *"apenas você pode ver"*. Duas precisões que a aula não tinha |
| Painel do projeto | **2.030 linhas ocupam 2%** da capacidade. Virou o fecho da página de exemplo |

**A lição de método:** eu procurei a confirmação da pilha no help center por dois
turnos e não achei. Ela estava escrita **dentro do produto**, num diálogo que o
usuário lê toda vez que cria um projeto. Documentação de produto também é a tela
do produto.

### A seção 04 estava "desenquadrada", e era literal

Três defeitos somados, nenhum deles overflow:

1. A tabela era desenhada com barra vertical em **fonte proporcional**. Os pipes
   não alinhavam, e é isso que o olho lê como quebrado
2. `.uau-prompt` tinha `margin:0 22px 0`, ou seja **zero em cima e zero embaixo**,
   espremida entre o cabeçalho e as colunas
3. O bloco corria a `--col-wide` cheia, 1.140px contra 732px de prosa. Razão 1,56

Corrigido com três variantes renderizadas e comparadas no navegador, e o Rafael
escolheu a C: a saída virou **tabela HTML de verdade**, como o Claude renderiza,
e o bloco caiu para **960px** (razão 1,31). O momento-chave é metade figura e
metade prosa, e por isso ele não merece a largura das figuras puras.

**Duas regras globais da própria página mordiam o bloco novo**, e só apareceram
medindo: `table{min-width:580px}` empurrava a tabela para fora de meia coluna, e
`.step-body ol{font-size:18px}` inflava as listas da resposta. As duas anuladas
com `min-width:0` e prefixo `.step-body`.

### A página de exemplo ganhou um Project de verdade

A crítica do Rafael: *"o Claude project tem toda a parte de instruções, a parte
de contexto e não tem nada disso"*. Estava certo. Os arquivos mapeavam nos campos
certos, mas a página nunca **mostrava o Project**.

Entrou uma seção com o painel do `brand-squad` reproduzido campo a campo, com o
tamanho real de cada arquivo e a barra de capacidade. **Só prévia, sem download**,
decisão dele: o arquivo é ativo de trabalho e o repositório é público.

Três escolhas que valem registrar:

- **O texto da Memória foi trocado por um genérico**, e o motivo virou conteúdo:
  a tela diz *"apenas você pode ver esta memória"*, então publicar a original
  seria mostrar justamente o que o produto separa
- **A palavra "agente" não entrou**, mesmo o arquivo de origem sendo cheio dela.
  Na página são "especialistas". O termo é do nível 3 e chega na 1.4
- **Nenhum dos 15 nomes de autor real aparece.** A regra do §6.1 vale mesmo para
  gente pública

### O gate que eu achei que tinha e não tinha

O **G13c** confere os números do Project real contra os dois arquivos de origem.
A primeira versão conferia **presença**: *"a página precisa dizer 2.030 linhas"*.

Injetei o defeito numa cópia e **ele passou**. Motivo: o número aparece em dois
lugares da página, e trocar um deles deixava o outro satisfazendo o teste.

Reescrito para conferir **cada citação dentro dos rótulos do painel**, e não a
presença em qualquer lugar do arquivo. Reprovado contra **9 defeitos injetados**,
9 pegos, incluindo o caso de o arquivo de origem crescer e a página ficar velha.

> **Presença não é conferência.** Um gate que pergunta "existe?" passa enquanto
> sobrar uma cópia certa em qualquer canto do arquivo. O que protege é conferir
> **cada ocorrência no lugar onde ela é afirmada**.

### 🔴 E o exemplo real derrubou o critério de tamanho da aula

**Rafael achou na hora**, olhando a tabela de gavetas: ela dizia *"Tamanho certo ·
Curto. 20 a 40 linhas"*, e a página de exemplo, a um clique dali, mostrava um
campo de Instruções com **128 linhas funcionando bem**.

**A tabela estava dando um número como critério, e o número estava errado.** O
critério de verdade é outro, e a própria aula já o tinha em outro lugar:

> **O tamanho é consequência do critério, não é o critério.** Se toda linha vale
> em toda conversa, o texto pode crescer sem estragar nada. Se tem linha que só
> vale às vezes, ele já está errado com 10 linhas.

O que mudou:

| Antes | Depois |
|---|---|
| Linha "Tamanho certo": *20 a 40 linhas* | Linha **"Como saber se cabe ali"**: *toda linha vale em toda conversa* |
| "O que dá errado: virar manual de 200 linhas" | "O que dá errado: **pôr como regra o que era consulta**" |
| "Documentos: pode ser longo, mas **poucos** arquivos" | "Muitos arquivos **parecidos entre si**: ele acha o trecho vizinho" |
| Validador item 1: *"o seu texto cabe em uma página"* | *"toda linha vale em qualquer conversa deste projeto"* |
| Passo do exercício: *"Fique entre 20 e 40 linhas"* | *"**Nesta primeira**, fique entre 20 e 40 linhas"* |

**A faixa de 20 a 40 não sumiu, mudou de estatuto.** Ela é andaime do primeiro
exercício, e agora diz isso: abaixo de 20 quase sempre é texto escrito de
memória, acima de 40 na primeira tentativa quase sempre é consulta disfarçada de
regra. **A licença para crescer é o teste da linha, não um número.**

Nasce o **G17**, que exige que toda faixa de linhas venha qualificada e que a
tabela e o validador não voltem a medir por tamanho.

> ⚠️ **A primeira versão do G17 usava janela de 320 caracteres** para achar a
> qualificação "por perto". Furou no teste: a janela atravessa `<p>` e `<li>`
> vizinhos, e o parágrafo de cima qualificava outra coisa. Reescrito para exigir
> a qualificação **no mesmo bloco**. Provado contra 8 defeitos injetados.

### E o validador prometia quatro conferências e tinha cinco

Achado ao mexer no item 1. A onda 3-octies acrescentou um item e ninguém
reescreveu o `checagem-lead`. **Ninguém conta ao acrescentar item**, então virou
o **G18**: o número por extenso no lead tem que bater com a contagem de
`.checagem-o`. Lead que não abre com número não promete nada, e passa.

### Onda 3-undecies · o exercício da 1.3 sai do `.docx` e três blocos reenquadrados

**Quatro pedidos do Rafael no mesmo turno**, testando no navegador dele.

#### O exercício acontece na página, como na 1.2

O `.docx` de partida virou um **quadro com as cinco seções**, prévia ao vivo,
contador de linhas e botão de copiar. O `.docx` continua ali, como linha
secundária, para quem prefere papel ou impresso.

Duas escolhas que valem registrar:

- **A saída sai no formato do gabarito** (`# título` mais cinco `## N. seção`),
  não como formulário preenchido. É o texto que vai ser colado do outro lado
- **O contador conta o que é regra**, ignorando título e cabeçalho de seção, e
  fica verde na faixa que a aula pede para a primeira. É o mesmo número que o
  **G13b** confere no gabarito, agora visível para quem está escrevendo

#### Três blocos desenquadrados, e o padrão é o mesmo nos três

| Onde | O que estava errado | Medida |
|---|---|---|
| Coluna esquerda do momento-chave | caixa vazia embaixo do conteúdo | **268px** de sobra |
| Card azul de navegação | sangrava para 1140px com o texto travado em 58ch | **563px** de vazio à direita |
| Tabela do gabarito | sangrava **dentro** de um card de 730px e saía pelos dois lados | escapava **408px** |

**O padrão:** os três são a regra de sangramento aplicada onde ela não serve.
Ela existe para **figura na coluna de leitura**. Card de navegação é prosa, e
prosa vive na coluna. Dentro de um card não existe coluna de leitura para
sangrar, então o `margin-left:50%` mede contra a caixa errada.

Correções: a leitura que vale para as duas colunas virou uma faixa `.uau-fecho`
embaixo das duas (268px caíram para 78px) · `.saidas` saiu da regra de
sangramento **nas quatro aulas** e o `.s-desc` passou a encher o card (sobra de
563px para 80px, 70 caracteres por linha) · `.gabarito-body .table-wrap` anula o
sangramento dentro do card.

Nasce o **G19**. A primeira versão dele procurava a lista de seletores a partir
do comentário `/* BREAKOUT`, e **parou no primeiro `{` depois dele**, que na 1.3
era o `.uau{--col-wide:960px}` da onda anterior. A segunda versão usava
`([^{}]+)\{...` e **travou o gate**, backtracking quadrático em arquivo de
90 KB. A terceira fatia o CSS por `}` e procura a regra **pelo que ela faz**,
`margin-left:50%`, não por onde ela está. Provado contra 5 defeitos injetados.

> **Ache a regra pelo efeito, não pela vizinhança.** Comentário se move, ordem
> muda, e um seletor novo entra no meio. `margin-left:50%` é o que define a
> regra, e é por ele que o gate tem que procurar.

**Gates:** 23 gates, 198 checagens, exit 0.

## 8. Aberto

- 🔴 **Teste de mesa das 4 aulas**, que nenhuma onda substitui
- 🟡 **Confirmar "Contexto" numa conta que não seja a do instrutor**, antes da turma
- **M2 e M3 ainda com nome antigo.** "Cowork na prática" carrega o recurso oficial mas não promete nada. Resolver quando o M2 for validado
- A onda 4 (Módulo 2) continua bloqueada pelas duas descobertas da onda 2: skill do claude.ai é individual, e só o proprietário adiciona conector em Team/Enterprise
