import pandas as pd
import streamlit as st
from api.api import ncm_api
from components.button import button_search
from st_aggrid import AgGrid


def search_ncm():
    ncm_input = st.text_input('Digite o código NCM ou descrição do produto')
    bt_search = button_search('Pesquisar')

    if bt_search:
        data_ncm = ncm_api(ncm_input)

        if data_ncm:
            st.subheader(f'Resultados para pesquisa: {ncm_input}')

            AgGrid(data=pd.DataFrame(data_ncm))
        else:
            st.error(f'Código NCM {ncm_input} não existe!')
