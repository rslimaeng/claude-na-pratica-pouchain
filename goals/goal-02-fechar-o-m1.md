# Goal 02 · Fechar o Módulo 1

**Status:** executada em 06/08/2026. Aguarda teste de mesa do Rafael.

## 1. O que entrou nesta onda

Pedido do Rafael, em três frentes:

1. **Consertar o layout.** Duas queixas: a frase que quebrava no meio e o texto que "não aproveitava o espaço"
2. **Fechar o M1 inteiro**, as aulas 1.2 e 1.4, para ele validar o módulo de uma vez em vez de em pedaços
3. **Validador no fim de cada aula**, e uma revisão de como Project, skill e MCP estavam sendo apresentados, com mais de um exemplo por conceito

## 2. As duas correções de layout

### 2a. A frase quebrando no meio

Dois mecanismos diferentes, o mesmo sintoma. Viraram os gates **G11** e **G11b**:

| Causa | Onde estava | Efeito |
|---|---|---|
| `display:block` em seletor de **tag inline** | `.pre-req-item strong`, `.mod-entrega strong` | Todo `<strong>` do bloco virava bloco, inclusive dentro de `<p>`. "Traga a sua" ia para uma linha só, e a frase continuava embaixo começando com vírgula |
| `display:flex` no **pai**, com texto solto irmão de tag inline | `.mapa-oque`, `.mapa-carga`, `.download-filename` | Cada pedaço virava item de flex e a frase se espalhava pela caixa |

**Conserto que vale como regra:** rótulo que precisa ser bloco ganha a classe `.rot`. Container flex tem um elemento por item, nunca texto solto ao lado de tag.

### 2b. O texto que "não aproveitava o espaço"

A queixa estava certa, o diagnóstico não. Medido no navegador antes de mexer:

- `.wrap` era `1100px`, e a prosa tinha **nove** `max-width` diferentes entre `680px` e `860px`
- Resultado: **102 caracteres por linha**, contados um a um com `Range.getClientRects()`

102 caracteres é **longe demais**, não perto. A faixa confortável é 45 a 80. Alargar a linha teria piorado a leitura de verdade.

O que estava errado era a **relação**: prosa em nove larguras dentro de uma página larga, com tabela e grade indo até a borda. O texto parecia órfão, e é isso que o olho registra como "quebrou cedo".

**Conserto:** duas larguras, e só duas.

| Token | Valor | Quem usa |
|---|---|---|
| `--col` | `780px` | a coluna de leitura. Prosa enche ela **inteira**, sem `max-width` próprio |
| `--col-wide` | `1140px` | header, breadcrumb e as figuras, que estouram a coluna |

Corpo do texto subiu de 16px para 18,5px. Resultado medido: **81 caracteres por linha**, e a prosa encostando nas duas bordas da coluna.

> ⚠️ **Não estime largura de linha, meça.** `1ch` no Inter vale ~1,34 caractere. A conta de cabeça erra em 30%, e foi o que me fez escolher `76ch` na primeira tentativa, que deu 102 caracteres.

## 3. As duas aulas novas

| | |
|---|---|
| **1.2 · Pedir para entregar** | Ementa 1.4. Conceitos: pedir o resultado e não a tarefa · as três perguntas. Analogia: a **OS de impressão**, que a casa já usa há vinte anos e nunca deixa campo em branco. Exercício em `.docx` com 3 pedidos ruins, um por setor |
| **1.4 · O mapa: onde cada regra mora** | Ementa 1.3. Conceitos: uma pergunta escolhe entre os 5 lugares · regra que precisa valer 100% não mora em texto. Entrega o **2º artefato do M1**, a tabela de decisão impressa |

**Componentes visuais novos:** `.rodadas` (idas e vindas por versão do pedido), `.os` (a OS de impressão ao lado da OS de pedido, campo a campo), `.mapa` (as 5 faixas), `.exemplos` (accordion por setor), `.checagem` (o validador).

## 4. O validador de fim de aula

Camada 1 do harness traduzida para uma sala de 20 pessoas: **critério objetivo que o aluno confere sozinho**.

Cada item tem três partes: o que conferir · **como** conferir (contável ou sim/não) · para onde voltar se falhar.

Nenhum item pergunta "ficou bom?", porque ninguém responde isso sobre o próprio trabalho, e porque numa sala de 20 o instrutor não escala. Está nas 4 aulas.

## 5. Fatos de produto verificados

A aula 1.4 afirma onde cada coisa funciona, e isso **não estava verificado**. Foi checado na doc oficial em 06/08/2026 e registrado em `../FATOS-VERIFICADOS.md`. Duas descobertas mudam planejamento:

1. **Skill do claude.ai é individual de cada usuário.** Não é compartilhada com a organização e o admin não distribui de forma central. Não existe "o TI sobe e os 20 recebem" por essa via
2. **Em conta Team ou Enterprise, só o proprietário adiciona conector.** Conectar sistema não é decisão que se toma no meio da aula

Também: **comando e skill convergiram** na documentação atual. A aula ensina os dois como a mesma peça com gatilho diferente, e a ementa 1.3 segue coberta.

## 6. Gates

Deixaram de ser lista em markdown e viraram **`goals/gates.py`**, executável, com saída 1 em caso de falha.

```bash
python3 goals/gates.py
```

| Gate | O que pega |
|---|---|
| G1 | Os blocos da anatomia, incluindo o validador. Aceita o hook de fim de módulo |
| G2 | Gabarito atrás de `<details>`, nunca `open` |
| G3a / G3b | Nome do cliente em página de conteúdo · achado de consultoria em qualquer lugar |
| G4 | Afirmação sobre produto sem data de verificação |
| G6 | Link interno morto |
| G7 | Balanço de tags |
| G7-ter | Classe usada sem nenhum CSS que a pegue |
| G9 | Travessão |
| G10 | Insumo em formato proibido |
| **G11** | `display:block` em seletor de tag inline |
| **G11b** | Container flex/grid com texto solto irmão de tag inline |

**Duas regras para escrever gate novo**, as duas aprendidas errando:

1. **Gate com exceção permanente deixa de ser gate.** Quando G11b acusou `.download-filename` e `.mapa-carga`, o conserto foi no HTML, não no gate
2. **Gate que procura uma palavra não pode rodar contra o arquivo que enuncia a regra sobre ela.** A primeira versão do G3 reprovou o `CLAUDE.md` por conter a palavra que o próprio `CLAUDE.md` proíbe. Ver `EXCLUI_REGRA` no script

## 7. Teste de mesa · 🔴 pendente, só o Rafael faz

| Aula | O que conferir | O que muda se não bater |
|---|---|---|
| 1.1 | O prompt situado gera mesmo o documento A4, e ele confirma 3 coisas antes | Os números do gabarito e o item 4 do validador |
| **1.2** | O pedido do gabarito de Compras resolve mesmo **em uma rodada** | O item 2 do validador promete "duas mensagens ou menos" |
| 1.3 | O texto de regras muda mesmo a resposta em conversa nova | O item 3 do validador |
| **1.4** | Não tem passo executável: é classificação no papel. Confira se as 8 regras dão discussão boa em 12 minutos | O tempo do exercício |

## 8. Aberto

- `m1/a3-regra-que-fica/exercicio/minhas-regras-PARTIDA.md` continua em `.md`. É texto para copiar e colar nas Instruções do Project, então cabe na regra. Vale perguntar ao Rafael se prefere `.docx` mesmo assim, porque quem abre é gente que não abre `.md`
- Onda 3 é o Módulo 2. Antes dela, o pré-check de TI ganhou **dois itens bloqueantes** vindos do §5
