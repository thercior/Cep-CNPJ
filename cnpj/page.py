import pandas as pd
import streamlit as st
from cnpj.service import CNPJService
from components.button import button_search
from utils.cnpj_utils import df_data, format_cnpj
from utils.mask import mask_cnpj


def search_cnpj():
    script = mask_cnpj()
    st.markdown(script, unsafe_allow_html=True)
    cnpj_input = st.text_input("Digite o CNPJ:", max_chars=18, key="cnpj_input", help="Digite somente números")
    bt_search = button_search("Consultar")

    if bt_search:
        if cnpj_input:
            cnpj_formated = format_cnpj(cnpj_input)

            if len(cnpj_formated) != 14:
                return st.error('CNPJ Inválido! Por favor, insira um valor válido')

            cnpj_service = CNPJService(cnpj_formated)
            cnpj = cnpj_service.get_cnpj(cnpj_formated)

            if cnpj:
                st.subheader(f"Resultado dos dados para o CNPJ {cnpj_input}")

                tab1, tab2 = st.tabs(["Dados da Empresa", "Quadro Social da empresa"])

                with tab1:
                    st.write(f"Dados da Empresa de CNPJ {cnpj_input}")
                    df_cnpj = df_data(cnpj)
                    st.dataframe(df_cnpj, use_container_width=True)

                with tab2:
                    st.write(f"Quadro social da empresa {cnpj['nome']}")
                    data_cnpj_qsa = cnpj.get("qsa", [])

                    if data_cnpj_qsa:
                        df_cnpj_qsa = pd.DataFrame(data_cnpj_qsa)
                        st.dataframe(df_cnpj_qsa, use_container_width=True)
                    else:
                        st.info("NÃO HÁ INFORMAÇÃO DE QUADRO DE SÓCIOS E ADMINISTRADORES (QSA) NA BASE DE DADOS DO CNPJ")
            else:
                st.error(f"Não foram encontrados dados para o CNPJ {cnpj_input} pois ele é inválido ou campo está vazio")
        else:
            st.error("CNPJ vazio. Por favor, forneça um valor válido de CNPJ para pesquisar")
