import streamlit as st
from components.sidebar import sidebar_component
from services.cep_main import search_cep
from services.cnpj_main import search_cnpj
from services.ncm_main import search_ncm
from services.fipe_main import search_fipe


def main():
    # search = ''
    search = sidebar_component()

    match search:
        case "CEP":
            st.title('Busca Por CEP')
            st.write('Este é um buscador de dados de endereço e cep. Escolha o método desejado para buscar e terá o retorno caso válido')
            search_cep()

        case "CNPJ":
            st.title('Busca pelo CNPJ')
            st.write('Este é um buscador de dados de empresas pelo CNPJ. Escolha o método desejado para buscar e terá o retorno caso válido')
            search_cnpj()

        case "NCM":
            st.title('Buscar produto pelo registro NCM')
            st.write('Este é um buscador de dados de produtos pelo código NCM ou descrição do produto. Escolha o método desejado para buscar e terá o retorno caso válido')
            search_ncm()

        case "FIPE":
            st.title("Consulta de dados e valores de veículos pela Tabela Fipe")
            st.write('Este buscar realizar uma consulta de dados e informações de veículos pela tabela Fipe. Escolha o método desejado para consulta')
            search_fipe()

        case _:
            st.error("Opção de busca não encontrada")


if __name__ == '__main__':
    main()
