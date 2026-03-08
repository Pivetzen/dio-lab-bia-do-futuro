import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gemma3:1b" # Certifique-se que o modelo está rodando no Ollama

# ============ CARREGAR DADOS (BEBETO) ============
# Carregando a nova estrutura de arquivos que definimos
perfil = json.load(open('./data/jovem_perfil.json', encoding='utf-8'))
dicionario = json.load(open('./data/dicionario_kids.json', encoding='utf-8'))
extrato = pd.read_csv('./data/extrato_mesada.csv')
missoes = pd.read_csv('./data/missões_concluidas.csv')

# ============ MONTAR CONTEXTO PEDAGÓGICO ============
contexto = f"""
JOVEM INVESTIDOR: {perfil['nome']}, {perfil['idade']} anos ({perfil['escolaridade']})
META PRINCIPAL: {perfil['objetivo_principal']} (Faltam R$ {perfil['metas'][0]['valor_necessario'] - perfil['cofrinho_total']})
RESPONSÁVEL: {perfil['responsavel_legal']['nome']} ({perfil['responsavel_legal']['parentesco']})

ÚLTIMAS MOVIMENTAÇÕES (MESADA):
{extrato.tail(5).to_string(index=False)}

MISSÕES JÁ CONCLUÍDAS (XP):
{missoes.to_string(index=False)}

DICIONÁRIO DE ANALOGIAS (OBRIGATÓRIO USAR):
{json.dumps(dicionario['termos'], indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT (PERSONA BEBETO) ============
SYSTEM_PROMPT = """Você é o Bebeto, um mentor financeiro descolado para crianças e adolescentes.

OBJETIVO:
Ensinar finanças de forma gamificada e simples, usando os dados do jovem para dar exemplos.

REGRAS DE OURO:
1. TRADUÇÃO OBRIGATÓRIA: Use SEMPRE as analogias do dicionário (ex: em vez de 'CDB', use 'Empréstimo de Brinquedo').
2. VALIDAÇÃO: Qualquer sugestão de investimento deve vir acompanhada de: "Mas primeiro, precisamos do OK da [Nome do Responsável]".
3. LINGUAGEM: Use um tom de 'parceiro', gírias leves e emojis. Seja motivador!
4. FOCO NA META: Relacione gastos e economias com o tempo que falta para atingir o objetivo (ex: PS5).
5. LIMITAÇÃO: Se perguntarem algo fora de finanças ou perigoso, diga que seu superpoder é só sobre moedas e sonhos.
6. Responda em no máximo 3 parágrafos curtos.
"""

# ============ CHAMAR OLLAMA ============
def perguntar_bebeto(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO JOVEM:
    {contexto}

    Pergunta do Jovem: {msg}"""

    try:
        r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False}, timeout=120)
        return r.json()['response']
    except Exception as e:
        return f"Ops! Meu sistema deu um tique... (Erro: {e}). Tenta de novo, Lucas!"

# ============ INTERFACE STREAMLIT (VISUAL GAMIFICADO) ============
st.set_page_config(page_title="Bebeto - Seu Mentor Financeiro", page_icon="🎮")

st.title("🎮 Bebeto: O Mestre das Moedas")
st.subheader(f"E aí, {perfil['nome']}! Rumo ao seu {perfil['objetivo_principal']}! 🎮")

# Barra de progresso da meta
progresso = (perfil['cofrinho_total'] / perfil['metas'][0]['valor_necessario'])
st.progress(progresso)
st.caption(f"Seu baú está com {progresso*100:.1f}% da meta concluída!")

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if pergunta := st.chat_input("Diz aí, qual a dúvida de hoje?"):
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Consultando o baú de sabedoria..."):
            resposta = perguntar_bebeto(pergunta)
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
