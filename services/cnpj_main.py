import locale
import pandas as pd
import streamlit as st
from api.api import cep_api, cnpj_api
from components.button import button_search
from utils.mask import mask_cnpj
from utils.uf import uf_choices


# Configurações da biblioteca para converter de um sistema para outro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def decimal_treat(decimal_str):
    treat_value = locale.format_string('%.2f', float(decimal_str), grouping=True)
    return f'R$ {treat_value}'


def format_cnpj(cnpj_input):
    cnpj = ''.join(filter(str.isdigit, cnpj_input))  #  Remove caracteres não numéricos
    cnpj = cnpj[:14]  # Limita a 14 digitos
    print(f"Este é o retorno do cnpj tratado: {cnpj}")
    return cnpj


def search_cnpj():
    cnpj_input = st.text_input("Digite o CNPJ:", max_chars=18)
    fields_company = [
        "status", "ultima_atualizacao", "cnpj", "tipo", "porte", "nome",
        "fantasia", "abertura", "atividade_principal", "atividades_secundarias",
        "natureza_juridica", "logradouro", "numero", "complemento", "cep",
        "bairro", "municipio", "uf", "email", "telefone", "situacao", "data_situacao",
        "motivo_situacao", "capital_social",
    ]
    fields_qsa = ["nome", "qual"]
    bt_search = button_search("Consultar")

    if bt_search:
        if cnpj_input:
            cnpj = format_cnpj(cnpj_input)
        else:
            st.error('CNPJ vazio. Por favor, forneça um valor válido de cnpj para pesquisar')

        if len(cnpj) != 14:
            return st.error('CNPJ inválido. Por favor, insira um valor válido')

        data_cnpj = cnpj_api(cnpj)

        if data_cnpj:
            st.subheader(f"Resultado dos dados para o CNPJ {cnpj_input}")
            # df_cnpj_qsa = pd.DataFrame(data_cnpj_qsa, index=fields_qsa)

            tab1, tab2 = st.tabs(["Dados da Empresa", "Quadro Social da Empresa"])
            with tab1:
                st.write(f"Dados da empresa de CNPJ {cnpj_input}")
                data_cnpj_company = [data_cnpj[field] for field in fields_company]
                data_cnpj_company[-1] = decimal_treat(data_cnpj["capital_social"])
                df_cnpj_company = pd.DataFrame(data_cnpj_company, index=fields_company)
                st.dataframe(df_cnpj_company, use_container_width=True)

            with tab2:
                st.write(f"Quadro Social da empresa {data_cnpj['nome']}")
                data_cnpj_qsa = data_cnpj.get("qsa", [])

                if data_cnpj_qsa:
                    df_cnpj_qsa = pd.DataFrame(data_cnpj_qsa)
                    st.dataframe(df_cnpj_qsa, use_container_width=True)
                else:
                    st.info("NÃO HÁ INFORMAÇÃO DE QUADRO DE SÓCIOS E ADMINISTRADORES (QSA) NA BASE DE DADOS DO CNPJ ")
        else:
            st.error(f"Não foram encontrados dados para o CNPJ {cnpj_input}")
