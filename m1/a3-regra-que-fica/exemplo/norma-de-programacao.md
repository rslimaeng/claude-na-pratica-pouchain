# Norma interna de programação de produção · Gráfica Aurora

> Este arquivo vai no campo **Contexto**, não nas Instruções.
> Repare na diferença: as regras do coordenador são lidas em toda conversa.
> Esta norma só é consultada quando a pergunta tem a ver com ela.
> Documento fictício, criado para o treinamento.

## NP-01 · Ordem de prioridade quando duas OS disputam a mesma máquina

Quando duas ou mais OS competem pelo mesmo equipamento na mesma janela,
a fila obedece esta ordem, e só se passa para o critério seguinte em caso
de empate:

1. OS com prazo já vencido, da mais atrasada para a menos atrasada
2. OS de cliente em contrato anual, listados no anexo A
3. OS com maior valor faturado
4. OS que entrou primeiro no sistema

A ordem só pode ser quebrada com autorização do gerente industrial,
registrada na própria OS.

## NP-02 · Tempo de preparação por família de máquina

O tempo de preparação entra na programação como tempo de máquina ocupada,
mesmo sem produzir peça:

| Família | Preparação | Troca de cor adicional |
|---|---|---|
| Offset | 90 min | 25 min por cor |
| Flexo | 45 min | 15 min por cor |
| Digital | 10 min | não se aplica |

Trocar de substrato dentro da mesma OS soma mais 20 minutos em qualquer família.

## NP-03 · Capacidade nominal por turno

Turno A das 6h às 14h, turno B das 14h às 22h. O turno C das 22h às 6h
só roda com autorização prévia.

| Máquina | Peças por hora | Observação |
|---|---|---|
| Offset 1 | 9.000 | a mais rápida, tiragem acima de 20 mil |
| Offset 2 | 7.500 | aceita papel cartão |
| Offset 3 | 6.000 | a mais antiga, para tiragem média |
| Flexo 1 | 4.200 | rótulo autoadesivo |
| Flexo 2 | 3.800 | filme flexível |
| Digital 1 | 900 | tiragem até 2 mil, dado variável |

A capacidade nominal considera 85% de eficiência. Programar acima disso
exige justificativa escrita.

## NP-04 · O que atrasa uma OS sem que ela apareça atrasada no sistema

O campo Status do sistema é preenchido à mão pelo líder de turno, e por isso
atrasa em relação à realidade. Estas quatro situações não mudam o campo Status:

- OS parada aguardando aprovação de prova pelo cliente
- OS parada aguardando entrada de papel do fornecedor
- OS com arte reprovada e reenviada para o cliente
- OS em máquina parada por manutenção não programada

**A regra que vale:** para saber se uma OS está atrasada, compare a data de
prazo com a data de hoje. Não use o campo Status.

## NP-05 · Quando uma OS pode mudar de máquina

Só quando as três condições valem ao mesmo tempo:

1. A máquina de destino aceita o substrato da OS
2. A tiragem cabe na faixa de capacidade da máquina de destino
3. A troca não empurra outra OS já programada para depois do prazo dela

Mudança de máquina sempre gera nova preparação, que entra no cálculo.

## NP-06 · Papel e insumo

O papel é reservado no momento em que a OS entra na programação, não no
momento em que ela sobe na máquina. Reserva sem consumo por mais de 15 dias
volta para o estoque livre, e a OS precisa ser reprogramada.

Sobra de papel acima de 8% da tiragem é registrada como perda e entra no
relatório mensal de eficiência.

## Anexo A · Clientes em contrato anual

Supermercados Praia Nova · Cosméticos Flor de Lis · Laticínios Serra Verde ·
Distribuidora Norte Nordeste · Farmacêutica Cariri

Contrato anual garante prioridade na fila, não garante prazo menor.
O prazo continua sendo o que está na OS.
