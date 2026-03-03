# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir consórcio conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual consórcio você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de consórcios
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quais os valores de parcelas para consórcio de máquinas agrícolas?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**

- A integração dos dados financeiros, perfil do investidor e histórico de atendimento foi consistente e clara.
- As recomendações respeitaram o momento financeiro do cliente (priorizar reserva antes do consórcio).
- A linguagem consultiva e acessível ajudou a explicar conceitos sem jargões técnicos.
- Houve alinhamento com o histórico de dúvidas já atendidas (ex.: contemplação, lances).
- O tom empático e educativo manteve a confiança e transparência.

**O que pode melhorar:**

- Tornar as simulações mais visuais e comparativas (ex.: tabelas de parcelas em diferentes prazos).
- Explorar cenários alternativos para acelerar a meta de reserva (ex.: ajustes de gastos mensais).
- Antecipar dúvidas sobre taxas administrativas e custos adicionais do consórcio.
- Reforçar alertas sobre riscos de iniciar o consórcio antes de concluir a reserva.
- Oferecer opções de acompanhamento contínuo das metas financeiras com checkpoints mensais.

---

