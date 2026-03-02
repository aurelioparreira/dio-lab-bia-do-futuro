# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os arquivos `historico_atendimento.csv`, `perfil_investidor.json` e `produtos_financeiros.json` foram modificado para se encaixarem melhor no contexto do projeto Cora (consórcio e finanças pessoais). O arquivo `transacoes.csv` foi mantido sem modificações.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

A base de conhecimento pode ser injetada diretamente no prompt (ctrl + c, ctrl + v) ou carregada via código como no exemplo abaixo:

```
import pandas as pd
import json

#CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

#jsons
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```
text
DADOS E PERFIL DO CLIENTE (perfil_investidor.json)
{
  "cliente": {
    "nome": "João",
    "idade": 32,
    "profissao": "Analista de Sistemas",
    "renda_mensal": 5000.00,
    "patrimonio_total": 15000.00
  },
  "perfil_financeiro": {
    "tipo": "moderado",
    "aceita_risco": false,
    "momento": "organização financeira"
  },
  "objetivos": [
    {
      "tipo": "seguranca",
      "descricao": "Completar reserva financeira",
      "valor": 15000.00,
      "prazo": "2026-06"
    },
    {
      "tipo": "patrimonio",
      "descricao": "Entrada de imóvel",
      "valor": 50000.00,
      "prazo": "2027-12"
    }
  ],
  "indicacoes_consorcio": {
    "prioridade": "baixa",
    "momento_ideal": "apos_reserva",
    "tipo_recomendado": "consorcio_imovel_planejado",
    "estrategia": "entrada_programada"
  }
}

TRANSAÇÕES DO CLIENTE (transacoes.csv)
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saidam

HISTÓRICO ATENDIMENTO DO CLIENTE (historico_atendimento.csv)
data,canal,tema,resumo,resolvido
2025-09-15,chat,Parcelas do consórcio,Cliente perguntou sobre valores e prazos das parcelas,sim
2025-09-22,telefone,App do consórcio,Erro ao visualizar simulação foi corrigido,sim
2025-10-01,chat,Carta de crédito,Cliente pediu explicação sobre como funciona a contemplação,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência vinculada ao consórcio,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone para receber notificações da Cora,sim
---

PRODUTOS FINANCEIROS(produtos_financeiros.json)
[
  {
    "nome": "Consórcio Imobiliário",
    "categoria": "imovel",
    "risco": "baixo",
    "caracteristica": "Sem juros, prazo longo",
    "aporte_minimo": 300.00,
    "indicado_para": "Quem quer adquirir ou investir em imóvel"
  },
  {
    "nome": "Consórcio de Veículos",
    "categoria": "veiculo",
    "risco": "baixo",
    "caracteristica": "Parcelas acessíveis",
    "aporte_minimo": 250.00,
    "indicado_para": "Compra planejada de carro ou moto"
  },
  {
    "nome": "Consórcio com Lance Estratégico",
    "categoria": "estrategico",
    "risco": "medio",
    "caracteristica": "Possibilidade de contemplação rápida",
    "aporte_minimo": 500.00,
    "indicado_para": "Quem quer acelerar a contemplação"
  },
  {
    "nome": "Consórcio como Investimento",
    "categoria": "investimento",
    "risco": "medio",
    "caracteristica": "Formação de patrimônio",
    "aporte_minimo": 400.00,
    "indicado_para": "Quem busca construir renda no longo prazo"
  }
]
```

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
