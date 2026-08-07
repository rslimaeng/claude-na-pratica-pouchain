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

## 8. Aberto

- 🔴 **Teste de mesa das 4 aulas**, que nenhuma onda substitui
- **M2 e M3 ainda com nome antigo.** "Cowork na prática" carrega o recurso oficial mas não promete nada. Resolver quando o M2 for validado
- A onda 4 (Módulo 2) continua bloqueada pelas duas descobertas da onda 2: skill do claude.ai é individual, e só o proprietário adiciona conector em Team/Enterprise
