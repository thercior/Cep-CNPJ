import pandas as pd
import streamlit as st
from api.api import cep_api, ibge_api
from components.button import button_search
# from components.inputs import input_cep
from utils.uf import uf_choices


def format_cep(cep_input):
    # Remove caracteres não numéricos
    cep = ''.join(filter(str.isdigit, cep_input))
    # Limita a 8 digitos
    cep = cep[:8]
    return cep


def search_cep():
    method = st.radio('Escolha o método de busca:', options=['CEP', "Endereço"], horizontal=True)
    col1, col2 = st.columns(2, gap="large")
    colA, colB, colC = st.columns(3, gap="large")
    fields = ["cep", "logradouro", "complemento", "bairro", "localidade", "uf"]
    bt_search = button_search("Consultar")

    # Functions para renderizar o layout de acordo com o método de busca.
    def search_by_cep():

        with col1:
            cep_input = st.text_input("Digite o CEP:", max_chars=10)
            # cep_input = input_cep("Digite o CEP:")

        if bt_search:
            if cep_input:
                cep = format_cep(cep_input)
            else:
                st.error('CEP vazio. Por favor, adicione um valor para o Cep')

            if len(cep) != 8:
                return st.error("CEP Inválido. Por favor, insira um valor válido")

            data_cep = cep_api(cep)

            try:
                if data_cep:
                    data_cep = [data_cep[field] for field in fields]
                    st.subheader("Dados do CEP procurado")
                    df_cep = pd.DataFrame([data_cep], columns=fields)
                    st.dataframe(df_cep, use_container_width=True)
                else:
                    st.error(f"Não foram encontrados dados para o cep {cep} que foi informado")
            except Exception as e:
                return st.error(f'Erro inesperado: o valor para {str(e)} é inválido')

    def search_by_address():

        with colA:
            uf_select = st.selectbox('Selecione um Estado:', sorted([state[1] for state in uf_choices]), index=0)
            uf = [uf for uf, state in uf_choices if state == uf_select][0]
        with colB:
            # localidade = st.text_input('Digite a Cidade')
            localidade_select = ibge_api(uf)
            if localidade_select:
                localidade = st.selectbox('Selecione uma cidade', [city["nome"] for city in localidade_select])
            else:
                localidade = st.text_input('Digite a Cidade')
                st.info(f"A consulta não retornou nenhum dado para o estado {uf}")
                
        with colC:
            logradouro = st.text_input('Digite o nome da Rua')

        if bt_search:

            if uf and localidade and logradouro:
                try:
                    data_address = cep_api(uf=uf, localidade=localidade, logradouro=logradouro)

                    if data_address:
                        st.subheader("Dados do Endereço")
                        st.text(f"Você escolheu buscar informações do endereço: {logradouro} em {localidade} - {uf}")

                        # Construção do DataFrame exibir a lista dos resultados da requisição somente com os campos desejados
                        df_address = [{key: value for key, value in data.items() if key in [field for field in fields]} for data in data_address]
                        df_address = pd.DataFrame(df_address)
                        st.dataframe(df_address, use_container_width=True)
                    else:
                        st.error(f"Erro ao obter os dados do endereço. Verifique se o endereço {logradouro}, {localidade} - {uf} está correto")
                except Exception as e:
                    st.error(f"Erro {e}. Por favor, verifique os dados novamente")
            else:
                st.error("Por favor, preencha todos os campos")

    # Layout para renderizar
    if method == 'CEP':
        search_by_cep()

    elif method == 'Endereço':
        search_by_address()
