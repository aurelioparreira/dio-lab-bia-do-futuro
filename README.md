# CORA — AI Financial Advisor

CORA é um agente de inteligência artificial projetado para atuar como **consultora financeira digital**, capaz de analisar dados de clientes e gerar recomendações personalizadas para tomada de decisão.

O projeto demonstra como integrar **LLMs, dados estruturados e engenharia de prompts** para criar um **AI Agent aplicado ao setor financeiro**.

Este repositório foi desenvolvido no contexto do laboratório **BIA do Futuro da Digital Innovation One (DIO)**.

---

# Visão Geral

A CORA combina **dados financeiros estruturados + inteligência artificial generativa** para produzir recomendações personalizadas.

Ela analisa:

- perfil do investidor
- histórico de transações
- objetivos financeiros
- produtos financeiros disponíveis

Com base nesse contexto, o agente gera **orientações financeiras inteligentes e contextualizadas**.

---

# Problema

A maioria das pessoas:

- não tem acesso a consultoria financeira
- não sabe organizar suas finanças
- não entende qual produto financeiro escolher

Consultores humanos são caros e pouco escaláveis.

---

# Solução

CORA atua como uma **consultora financeira digital baseada em IA**, capaz de:

- interpretar dados financeiros do usuário
- identificar padrões de gastos
- avaliar metas financeiras
- sugerir estratégias financeiras

Tudo isso de forma **automatizada e escalável**.

---

# Arquitetura da Solução

Fluxo de funcionamento do agente:

```

Dados do Cliente
↓
Construção do Contexto
↓
Prompt para LLM
↓
Processamento da IA
↓
Resposta Inteligente

```

A solução foi estruturada em quatro camadas principais.

---

# Camada 1 — Dados Financeiros

Dados simulados utilizados pelo agente para análise.

```

data/
│
├── perfil_investidor.json
├── produtos_financeiros.json
├── historico_atendimento.csv
└── transacoes.csv

```

Esses dados representam o **contexto financeiro do cliente**.

---

# Camada 2 — Context Builder

Os dados são consolidados em um **prompt estruturado** enviado ao modelo de linguagem.

Exemplo de contexto gerado:

```

Cliente: João
Idade: 35
Perfil: Moderado

Objetivos:

* Comprar carro em 3 anos
* Criar reserva de emergência

```

Esse contexto permite que a IA produza respostas **mais precisas e personalizadas**.

---

# Camada 3 — Motor de Inteligência Artificial

O projeto utiliza um **LLM (Large Language Model)** para interpretar o contexto e gerar recomendações financeiras.

Fluxo lógico:

```

Data → Context → Prompt → LLM → Insight Financeiro

```

---

# Camada 4 — Interface

A interface foi construída utilizando **Streamlit**, permitindo interação simples com o agente.

Funcionalidades:

- perguntas financeiras
- recomendações personalizadas
- interpretação do perfil financeiro

---

# Tecnologias Utilizadas

Python  
Streamlit  
Pandas  
JSON  
CSV  
API de LLM  
Prompt Engineering  

---

# Estrutura do Projeto

```

.
├── data
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   ├── historico_atendimento.csv
│   └── transacoes.csv
│
├── docs
│   ├── documentacao_agente.md
│   ├── base_conhecimento.md
│   ├── prompts.md
│   └── metricas.md
│
├── src
│   └── app.py
│
└── README.md

```

---

# Como Executar o Projeto

## 1 — Clonar repositório

```

git clone [https://github.com/aurelioparreira/dio-lab-bia-do-futuro](https://github.com/aurelioparreira/dio-lab-bia-do-futuro)

```

---

## 2 — Instalar dependências

```

pip install -r requirements.txt

```

---

## 3 — Executar aplicação

```

streamlit run src/app.py

```

---

# Exemplo de Uso

Pergunta do usuário:

```

Qual estratégia devo usar para comprar um carro em 3 anos?

```

Resposta da CORA:

- análise de renda
- análise de gastos
- sugestão de plano de economia
- indicação de produtos financeiros

---

# Roadmap

Próximas evoluções planejadas:

- integração com APIs bancárias
- memória de conversas
- recomendação automática de investimentos
- dashboard financeiro
- análise preditiva de gastos

---

# Aprendizados do Projeto

Durante o desenvolvimento foram explorados:

- AI Agents
- Engenharia de Prompts
- Integração de LLMs com dados estruturados
- Interfaces conversacionais
- IA aplicada a tomada de decisão financeira

---

# Possíveis Aplicações

- fintechs
- consultoria financeira automatizada
- educação financeira
- assistentes bancários
- plataformas de investimento

---

# Autor

Aurélio Parreira  

Explorador de IA aplicada à tomada de decisão.

GitHub  
https://github.com/aurelioparreira

---

# Licença

Este projeto é open-source e pode ser utilizado para fins educacionais.

---

## Interface

![Interface](assets/Streamlit.pdf)
