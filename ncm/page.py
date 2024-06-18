from ncm.service import NCMService
from components.button import button_search
from st_aggrid import AgGrid
import pandas as pd
import streamlit as st


def search_ncm():
    ncm_input = st.text_input('Digite o código NCM ou descrição do produto')
    bt_search = button_search('Pesquisar')

    if bt_search:
        ncm_service = NCMService(ncm_input)
        ncm = ncm_service.get_ncm()

        if ncm:
            st.subheader(f'Resultados para pesquisa: {ncm_input}')

            AgGrid(data=pd.DataFrame(ncm))
        else:
            st.error(f'Código NCM {ncm_input} não existe ou inválido!')
