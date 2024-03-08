import pandas as pd
import streamlit as st
from api.api import cnpj_api
from components.button import button_search
from utils.mask import mask_cnpj
from utils.cnpj_utils import df_data, format_cnpj


def search_cnpj():
    script = mask_cnpj()
    st.markdown(script, unsafe_allow_html=True)
    cnpj_input = st.text_input("Digite o CNPJ:", max_chars=18, key="cnpj_input", help="Digite somente números")
    bt_search = button_search("Consultar")

    if bt_search:
        if cnpj_input:
            cnpj = format_cnpj(cnpj_input)

            if len(cnpj) != 14:
                return st.error('CNPJ inválido. Por favor, insira um valor válido')

            data_cnpj = cnpj_api(cnpj)

            # Verifica se houve retorno de dados da request
            if data_cnpj:
                st.subheader(f"Resultado dos dados para o CNPJ {cnpj_input}")

                tab1, tab2 = st.tabs(["Dados da Empresa", "Quadro Social da Empresa"])
                with tab1:
                    st.write(f"Dados da empresa de CNPJ {cnpj_input}")
                    df_cnpj = df_data(data_cnpj)  # tratar os dados da request
                    st.dataframe(df_cnpj, use_container_width=True)

                with tab2:
                    st.write(f"Quadro Social da empresa {data_cnpj['nome']}")
                    data_cnpj_qsa = data_cnpj.get("qsa", [])

                    if data_cnpj_qsa:
                        df_cnpj_qsa = pd.DataFrame(data_cnpj_qsa)
                        st.dataframe(df_cnpj_qsa, use_container_width=True)
                    else:
                        st.info("NÃO HÁ INFORMAÇÃO DE QUADRO DE SÓCIOS E ADMINISTRADORES (QSA) NA BASE DE DADOS DO CNPJ ")
            else:
                st.error(f"Não foram encontrados dados para o CNPJ {cnpj_input} pois ele é inválido ou campo está vazio")

        else:
            st.error('CNPJ vazio. Por favor, forneça um valor válido de cnpj para pesquisar')
