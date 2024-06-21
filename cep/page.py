from api.api_repository import GetIbgeApi
from cep.service import CEPService
from components.button import button_search
from utils.uf import uf_choices
from utils.cep_utils import format_cep
import pandas as pd
import streamlit as st


class SearchCep:

    def __init__(self):
        self.method = st.radio('Escolha o método de busca:', options=['CEP', 'Endereço'], horizontal=True)
        self.col1, self.col2 = st.columns(2, gap="large")
        self.colA, self.colB, self.colC = st.columns(3, gap="large")
        self.fields = ["cep", "logradouro", "complemento", "bairro", "localidade", "uf"]
        self.bt_search = button_search("Consultar")

    def search_cep(self):
        if self.method == 'CEP':
            self.search_by_cep()

        elif self.method == 'Endereço':
            self.search_by_address()

    def search_by_cep(self):
        with self.col1:
            cep_input = st.text_input("Digite o CEP:", max_chars=10)

        if self.bt_search:
            if cep_input:
                cep_formated = format_cep(cep_input)

                if cep_input and len(cep_formated) != 8:
                    return st.error("CEP Inválido. Por favor, insira um valor válido!")

                cep_service = CEPService(cep_formated)
                cep = cep_service.get_cep()

                if cep:
                    cep = [cep[field] for field in self.fields]
                    st.subheader(f"Dados do CEP procurado")
                    df_cep = pd.DataFrame([cep], columns=self.fields)
                    st.dataframe(df_cep, use_container_width=True)
                else:
                    st.error(f"Não foram encontrados dados para o cep {cep_input} que foi informado")
            else:
                st.error('CEP vazio. Por favor, adicione um valor para o Cep')

    def search_by_address(self):
        with self.colA:
            uf_select = st.selectbox('Selecione um Estado:', sorted([state[1] for state in uf_choices]), index=0)
            uf = [uf for uf, state in uf_choices if state == uf_select][0]

        with self.colB:
            locality_select_repository = GetIbgeApi(uf)
            locality_select = locality_select_repository.get_cities_api()

            if locality_select:
                locality = st.selectbox('Selecione uma cidade', [city["nome"] for city in locality_select])
            else:
                locality = st.text_input('Digite o nome de uma Cidade')
                st.info(f"A consulta não retorno nenhum dado para o estado {uf}")

        with self.colC:
            address = st.text_input('Digite o nome da rua')

        if self.bt_search:
            if uf and locality and address:
                try:
                    address_service = CEPService(uf=uf, locality=locality, address=address)
                    data_address = address_service.get_address()

                    if data_address:
                        st.subheader("Dados do endereço")
                        st.text(f"Você escolheu buscar informações do endereço: {address} em {locality} - {uf}")

                        df_address = [{key: value for key, value in data.items() if key in [field for field in self.fields]} for data in data_address]
                        df_address = pd.DataFrame(df_address)
                        st.dataframe(df_address, use_container_width=True)
                    else:
                        st.error(f'Erro ao obter os dados do endereço. verifique se o endereço "{address}, {locality} - {uf}" está correto')
                except Exception as e:
                    st.error(f'Erro {e}. Por favor, verifique os dados novamente')
            else:
                st.error("Por favor, preencha todos os campos")
