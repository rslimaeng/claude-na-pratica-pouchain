# Claude na Prática · site do curso

Material de apoio do treinamento in-company **Claude na Prática**: 12 horas, 3 módulos, 19 aulas curtas. Conduzido por Rafael Lima.

O site é o material que fica **depois** do curso: cada aula é uma página navegável, com o exercício, o arquivo de partida e o gabarito.

## 👉 https://rslimaeng.github.io/claude-na-pratica-pouchain/

## Como abrir

Online, no link acima. Ou localmente: cada página é um HTML autossuficiente, basta abrir `index.html` no navegador, sem servidor e sem instalar nada. Também funciona offline, num pen drive.

## Estrutura

```
site/
├── CLAUDE.md            ← contexto do projeto (voz, regras de conteúdo, anatomia de aula)
├── _shared/             ← tokens de design
├── goals/               ← 1 arquivo por onda de produção
├── index.html           ← landing com a trilha dos 6 degraus
├── m1/                  ← Módulo 1 · Fundamentos
│   ├── index.html       ← hub do módulo
│   └── <aula>/          ← index.html + exercicio/ + gabarito/
└── kit/                 ← Kit do participante (montado na Onda 9)
```

## Estado

| Onda | Entrega | Status |
|---|---|---|
| 1 | Infra · landing · hub M1 · aulas 1.1 e 1.3 | 🟡 aguardando validação |
| 2 a 9 | a definir | ⏸️ |

Índice completo em [`goals/README.md`](goals/README.md).

## Antes de publicar

- [ ] `.nojekyll` na raiz (impede o Jekyll de renderizar os `.md`)
- [ ] Os 10 gates de qualidade de [`goals/goal-01-infra-e-padrao.md`](goals/goal-01-infra-e-padrao.md) §5 passaram
- [ ] Nenhum nome de pessoa real, nenhum dado do cliente dentro de exemplo ou insumo

---

Todos os exemplos e planilhas pertencem à **Gráfica Aurora**, uma indústria gráfica fictícia criada para o treinamento. Nomes, números e clientes são inventados.
