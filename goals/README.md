# Ondas de produção

1 onda = 1 goal. Nenhuma onda começa antes de o Rafael validar a anterior no navegador.
O plano completo está em [`../../PLANO-DE-PRODUCAO.md`](../../PLANO-DE-PRODUCAO.md).

| Onda | Goal | Entrega | Status |
|---|---|---|---|
| 1 | [`goal-01-infra-e-padrao.md`](goal-01-infra-e-padrao.md) | Infra · tokens · landing · hub M1 · **aulas 1.1 e 1.3** | ✅ validada, com 5 ajustes aplicados na onda 2 |
| **2** | [`goal-02-fechar-o-m1.md`](goal-02-fechar-o-m1.md) | **Aulas 1.2 e 1.4** · validador nas 4 aulas · conserto de layout · gates executáveis | 🟡 aguardando teste de mesa |
| **2-bis** | [`goal-02-bis-linguagem-de-rotina.md`](goal-02-bis-linguagem-de-rotina.md) | **Os 4 padrões de linguagem** aplicados em tudo que já existia. Nome de rotina + recurso oficial do Claude · dor-mãe ligada aos níveis · bloco "o que não fazemos" · gate G12 | ✅ no ar. Volta em `antes-da-linguagem-de-rotina` |
| **3** | [`goal-03-roteiros-e-linguagem.md`](goal-03-roteiros-e-linguagem.md) | **Roteiro de demonstração nas 4 aulas** · os 4 padrões de linguagem · renomeação do módulo e de 2 aulas · duração fora da tela · gates G12 a G15 | ✅ no ar |
| **3-bis** | [`goal-03-roteiros-e-linguagem.md`](goal-03-roteiros-e-linguagem.md) §7-ter | **A demonstração vira material do aluno** · direção de palco sai do site · planilhas de 18 e 56 para **120 e 104 linhas** · G14 inverte de sentido | ✅ aprovada e no ar |
| **3-ter** | [`goal-03-roteiros-e-linguagem.md`](goal-03-roteiros-e-linguagem.md) §7-quater | **Os cards que apontam para a demonstração** ainda descreviam o roteiro velho, em 5 trechos · o "2 para 7" da 1.3 era número da planilha antiga · nasce o **G14b**, que roda contra todo `.html` | ✅ no ar |
| **3-septies** | [`goal-03-roteiros-e-linguagem.md`](goal-03-roteiros-e-linguagem.md) §7-octies | **O exercício da 1.2 sai do `.docx` e entra na página**: quadro com as três perguntas, prévia ao vivo e botão de copiar · rascunho em `localStorage` · medida de linha aferida com sonda e ajustada para 62ch (~79 caracteres) | 🟡 aguardando validação |
| **3-octies** | [`goal-03-roteiros-e-linguagem.md`](goal-03-roteiros-e-linguagem.md) §7-nonies | **A 1.3 contra a documentação oficial de Projects**: a memória por projeto derrubou a "decepção nº 1" · três gavetas em vez de duas · um projeto, um trabalho · o empilhamento que já existe no Chat | ✅ validado no navegador · falta teste de mesa |
| **3-novies** | [`goal-03-roteiros-e-linguagem.md`](goal-03-roteiros-e-linguagem.md) §7-decies | **A didática do M3 do Maria Pitanga aplicada na 1.3**: cards É/Não é · anatomia em 3 cards · mockup da tela do Project · **página `exemplo/` com os 3 arquivos prontos** · nasce o **G13b** | ✅ validado no navegador · falta teste de mesa |
| **3-decies** | [`goal-03-roteiros-e-linguagem.md`](goal-03-roteiros-e-linguagem.md) §7-undecies | **A tela real como fonte da verdade**: o campo virou **Contexto**, não "Conhecimento do projeto" · seção 04 reenquadrada com tabela de verdade · a página `exemplo/` ganhou **um Project real por dentro** com Instruções, Memória e Contexto · **o exemplo real derrubou o critério de tamanho da aula** (o tamanho é consequência, não critério) · nascem **G13c**, **G16**, **G17** e **G18** | ✅ validado no navegador · falta teste de mesa |
| **3-undecies** | [`goal-03-roteiros-e-linguagem.md`](goal-03-roteiros-e-linguagem.md) §7-undecies | **O exercício da 1.3 sai do `.docx`** e vira quadro preenchível com contador e cópia · três blocos reenquadrados (momento-chave, card azul nas 4 aulas, tabela do gabarito) · nasce **G19** | ✅ validado no navegador · falta teste de mesa |
| 4 | a definir | Hub M2 + aulas 2.1 · 2.2 · 2.3 | ⏸️ |
| 5 | a definir | M2: aulas 2.4 · 2.5 · 2.6 | ⏸️ |
| 6 | a definir | M2: aulas 2.7 · 2.8 | ⏸️ |
| 7 | a definir | Hub M3 + aulas 3.1 · 3.2 · 3.3 | ⏸️ |
| 8 | a definir | M3: aulas 3.4 · 3.5 · 3.6 | ⏸️ |
| 9 | a definir | Aula 3.7 + entregável final + plano de 30 dias | ⏸️ |
| 10 | a definir | `recursos/` + `kit-participante.zip` montado | ⏸️ |

## O protocolo de 3 passos

Toda aula passa pelos três antes de ser considerada pronta:

1. **Produção**, o terminal produz segundo a anatomia e o goal da onda
2. **Auditoria**, `python3 goals/gates.py` rodado da raiz. São 23 gates e 198 checagens, e o script sai com código 1 se alguma falhar
3. **Teste de mesa (Rafael)** 🔴, ele roda o exercício de verdade e confere se a saída bate com o gabarito

O passo 3 é o único que pega *"o exercício não funciona"*. Nenhuma auditoria de código detecta isso.

> **Regra dos gates:** gate com exceção permanente deixa de ser gate. Se o script acusa, o conserto é no código. E gate que procura uma palavra não pode rodar contra o arquivo que enuncia a regra sobre ela, senão se auto-reprova.

## Duas regras que valem para toda aula nova

**1. A página publicada é do aluno.** Direção de cena (*pergunte à sala, espere, plano B, preparo, minutagem*) vive em `../../ROTEIRO-DE-PALCO-M1.md`, fora deste repositório. Os seis blocos permitidos estão em `../CLAUDE.md` §9, e o gate **G14** reprova 19 frases de palco por busca literal.

**1-bis. E vale para o site inteiro, não só para `demonstracao/`.** O **G14b** roda a mesma lista contra todo `.html`. Ele nasceu porque as quatro demonstrações estavam limpas e **os cards que apontavam para elas continuavam descrevendo o roteiro velho**. Ao corrigir uma página, pergunte sempre **o que aponta para ela**.

**2. Insumo tem piso de 100 linhas.** Em arquivo pequeno o aluno pensa *"isso eu fazia na mão"* e a tese da aula cai. Ver `../CLAUDE.md` §8-ter. Conferido pelo **G13**, que também recalcula todo número que as páginas afirmam.

**Ao escrever aula nova, copiar da 1.1.** É a única que passou pelas três correções do Rafael.
