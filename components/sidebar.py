import streamlit as st
# from services.cep_main import search_cep
# from services.cnpj_main import search_cnpj


def sidebar_component(*args, **kwargs):
    st.sidebar.title("Consultas Unificadas")
    st.sidebar.subheader("Esta aplicação reúne buscar informações de dados sobre CEP/Endereços, CNPJ e Tabela Fipe de Carros")
    search = st.sidebar.radio("Escolha a opção de busca", options=["CEP", "CNPJ", "FIPE"])

    # if search == "CEP":
    #     search_cep()

    # elif search == "CNPJ":
    #     search_cnpj()
    return search
