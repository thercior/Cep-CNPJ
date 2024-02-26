import streamlit as st
from api import cep_api, format_cep


def main():
    st.title('Busca Por CEP/CNPJ')
    st.write('Este é um buscador de dados de endereço e cep. Escolha o método desejado para buscar e terá o retorno caso válido')
    method = st.radio('Escolha o método de busca:', options=['CEP', "Endereço"])

    if method == 'CEP':
        cep_input = st.text_input("Digite o CEP:")
    elif method == 'Endereço':
        uf = st.text_input('Digite o Estado:')
        localidade = st.text_input('Digite a Cidade')
        logradouro = st.text_input('Digite o nome da Rua')

    bt_consultar = st.button('Consultar')

    if method == 'CEP':

        if bt_consultar:
            if cep_input:
                cep = format_cep(cep_input)

            if len(cep) != 8:
                return st.error("CEP Inválido. Por favor, insira um valor válido")

            data_cep = cep_api(cep)

            try:
                if data_cep:
                    st.subheader("Dados do CEP")
                    st.write(f'CEP: {data_cep["cep"]}')
                    st.write(f'Endereço: {data_cep["logradouro"]}')
                    st.write(f'Bairro: {data_cep["bairro"]}')
                    st.write(f'Cidade: {data_cep["localidade"]}')
                    st.write(f'Estado: {data_cep["uf"]}')
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
                        st.write(f'CEP: {data_cep["cep"]}')
                        st.write(f'Endereço: {data_cep["logradouro"]}')
                        st.write(f'Bairro: {data_cep["bairro"]}')
                        st.write(f'Cidade: {data_cep["localidade"]}')
                        st.write(f'Estado: {data_cep["uf"]}')
                    else:
                        st.error(f"Erro ao obter os dados do endereço. Verifique se o endereço {logradouro}, {localidade} - {uf} está correto")
                except Exception as e:
                    st.error(f"Erro {e}. Por favor, verifique os dados novamente")


if __name__ == '__main__':
    main()
