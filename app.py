import pandas as pd
import streamlit as st
from api import cep_api, format_cep
from uf import uf_choices


def main():
    st.title('Busca Por CEP/CNPJ')
    st.write('Este é um buscador de dados de endereço e cep. Escolha o método desejado para buscar e terá o retorno caso válido')
    col1, col2 = st.columns(2, gap="large")
    fields = ["cep", "logradouro", "complemento", "bairro", "localidade", "uf"]
    method = st.radio('Escolha o método de busca:', options=['CEP', "Endereço"], horizontal=True)

    if method == 'CEP':
        with col1:
            cep_input = st.text_input("Digite o CEP:")
    elif method == 'Endereço':
        colA, colB, colC = st.columns(3, gap="large")
        with colA:
            uf_select = st.selectbox('Selecione um Estado:', sorted([state[1] for state in uf_choices]), index=0)
            uf = [uf for uf, state in uf_choices if state == uf_select][0]
        with colB:
            localidade = st.text_input('Digite a Cidade')
        with colC:
            logradouro = st.text_input('Digite o nome da Rua')

    bt_consultar = st.button('Consultar')

    if method == 'CEP':

        if bt_consultar:
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

    elif method == 'Endereço':

        if bt_consultar:
            if uf and localidade and logradouro:
                try:
                    data_address = cep_api(uf=uf, localidade=localidade, logradouro=logradouro)

                    if data_address:
                        st.subheader("Dados do Endereço")
                        st.text(f"Você escolheu buscar informações do endereço: {logradouro} em {localidade} - {uf}")

                        for data in data_address:
                            st.write(f'CEP: {data["cep"]}')
                            st.write(f'Endereço: {data["logradouro"]}')
                            st.write(f'Número: {data["complemento"]}')
                            st.write(f'Bairro: {data["bairro"]}')
                            st.write(f'Cidade: {data["localidade"]}')
                            st.write(f'Estado: {data["uf"]}')
                            st.divider()

                        # df_address = pd.DataFrame([data_address[field] for field in fields], columns=fields)
                        # st.dataframe(df_address, use_container_width=True)
                    else:
                        st.error(f"Erro ao obter os dados do endereço. Verifique se o endereço {logradouro}, {localidade} - {uf} está correto")
                except Exception as e:
                    st.error(f"Erro {e}. Por favor, verifique os dados novamente")
            else:
                st.error("Por favor, preencha todos os campos")


if __name__ == '__main__':
    main()
