import streamlit as st
import database as db

db.criar_tabela()

st.title("Esse é um titulo")
st.header("Esse é um cabeçalho")
st.subheader("Esse é um cabeçalho menor")
st.text("Esse é um texto genérico")


with st.form("form_cadastro_aluno"):

    nome = st.text_input("Nome")
    idade = st.number_input("Idade", value=50)
    nota = st.number_input("Nota",value=0.0, step=0.5, min_value=0.0, max_value=10.0)

    btn_cadastro_aluno = st.form_submit_button("Cadastrar")

if btn_cadastro_aluno:
    msg = db.cadastro_aluno(nome, idade, nota)
    st.warning(msg)

with st.form("form_delete_aluno"):
    id_aluno = st.number_input("ID do aluno", value=0, step=1, min_value=0)

    btn_delete_aluno = st.form_submit_button("Deletar", 
    help="Ao clicar aqui você deleta um aluno")

if btn_delete_aluno:
    msg = db.delete_aluno(id_aluno)
    st.success(msg)
