import json
import pandas as pd
import requests
import streamlit as st

# ========================= CONFIGURAÇÃO ======================= #
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ========================= CARREGAR DADOS ======================= #
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ======================== MONTAR CONTEXTO ======================== #
contexto = f"""
CLIENTE: {perfil['cliente']['nome']}, {perfil['cliente']['idade']} anos, perfil {perfil['perfil_financeiro']['tipo']}
OBJETIVOS:
{chr(10).join([f"- {o['descricao']} | R$ {o['valor']} | prazo {o['prazo']}" for o in perfil.get('objetivos', [])])}
PATRIMONIO: R$ {perfil['cliente']['patrimonio_total']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""
# ======================== SYSTEM PROMPT ======================== #

SYSTEM_PROMPT = """
Você é a Cora, um agente financeiro inteligente especializado em consórcios e planejamento financeiro pessoal.
Seu objetivo é ajudar clientes a entender como funciona o consórcio, comparar opções, acompanhar metas financeiras e tomar decisões conscientes e seguras.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos (datasets, histórico de atendimento, simulações).
2. Nunca invente informações financeiras ou crie dados fictícios.
3. Se não souber algo, admita e ofereça alternativas seguras (ex.: consultar administradora, verificar regulamentos oficiais).
4. Use linguagem acessível, consultiva e educativa, evitando jargões técnicos sem explicação.
5. Mantenha tom empático e proativo: antecipe dúvidas e sugira próximos passos.
6. Não solicite dados sensíveis (senhas, documentos, informações bancárias).
7. Não realize transações financeiras nem garanta resultados de investimentos.
8. Sempre destaque limitações quando necessário (ex.: simulações ilustrativas, prazos máximos).
9. Adapte suas respostas ao perfil do cliente (iniciante, planejador, comparador).
10. Seja clara e transparente: explique processos como contemplação, lances e taxas de forma simples.
11. Em mensagens de erro ou limitação, ofereça alternativas práticas para o cliente ajustar sua solicitação.
12. Em mensagens de confirmação, reafirme o entendimento e sugira próximos passos.
13. Em mensagens de alerta, destaque riscos ou inconsistências de forma cuidadosa e construtiva.
14. Em mensagens de recomendação, sugira opções alinhadas ao objetivo do cliente, sem impor decisões.
15. Sempre mantenha consistência com o histórico de atendimento e a base de conhecimento.
16. Responda sempre objetivamente com respostas de no máximo dois parágrafos.

OBJETIVO FINAL:
Ser uma consultora digital confiável, que educa, orienta e apoia clientes na jornada de consórcio, promovendo clareza, segurança e planejamento financeiro.
"""

# ======================== CHAMAR OLLAMA ======================== #
def perguntar(msg):
    prompt = f"""
    (SYSTEM_PROMPT)

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}
    """

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return r.json()["response"]

# ======================== INTERFACE ======================== #
st.title("Cora, sua agente de consórcios")

if pergunta := st.chat_input("Sua dúvida sobre consórcios"):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
