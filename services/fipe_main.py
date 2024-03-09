import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from api.api import fipe_api, fipe_brands_models_api, fipe_model_year_api
from components.button import button_search
from utils.fipe_choices import vehicle_choices, cars_brands_choices, motorcycles_brands_choices, trucks_brands_choices


def search_fipe():
    method = st.radio('Escolha o método de busca:', options=['Veículo', 'Código Fipe'], horizontal=True)
    col1, col2, col3, col4 = st.columns(4, gap="large")
    colA, colB, colC = st.columns(3, gap="large")
    bt_search = button_search("Consultar")

    
    def search_fipe_vehicle():
        with col1:
            vehicle_select = st.selectbox('Selecione o tipo do veículo:', [vehicle[1] for vehicle in vehicle_choices])
            type_vehicle = [type_vehicle for type_vehicle, vehicle in vehicle_choices if vehicle == vehicle_select][0]
            model = ''
            year = ''
            fipe_code = ''
        
        with col2:
            match vehicle_select:
                case 'Carros':
                    brands_cars = st.selectbox('Selecione a marca do carro', [brand[1] for brand in cars_brands_choices])
                    brands = [brands for brands, brand in cars_brands_choices if brand == brands_cars][0]

                case 'Motos':
                    brands_motorcyles = st.selectbox('Selecione a marca da moto', [brand[1] for brand in motorcycles_brands_choices])
                    brands = [brands for brands, brand in motorcycles_brands_choices if brand == brands_motorcyles][0]

                case 'Caminhões':
                    brands_trucks = st.selectbox('Selecione a marca do carro', [brand[1] for brand in trucks_brands_choices])
                    brands = [brands for brands, brand in trucks_brands_choices if brand == brands_trucks][0]

        with col3:
            data_model = fipe_brands_models_api(type_vehicle=type_vehicle, brands=brands, model=model, year=year)

            if data_model:
                model_select = st.selectbox('Selecione o modelo do veículo:', [model['name'] for model in data_model])
                model = next(model['code'] for model in data_model if model['name'] == model_select)

            else:
                model = st.text_input('Digite o modelo do veículo')
                st.info(f'A consulta não retornou nenhuma informação para o veículo {model} da marca {brands}')

        with col4:
            data_model_year = fipe_model_year_api(type_vehicle=type_vehicle, brands=brands, model=model, year=year, fipe_code=fipe_code)

            if data_model_year:
                year_select = st.selectbox('Selecione o ano do modelo:', [year['code'] for year in data_model_year])
                year = year_select

        if bt_search:

            data_fipe = [fipe_api(
                type_vehicle=type_vehicle, brands=brands, model=model, year=year, fipe_code=fipe_code
            )]

            if data_fipe:
                # AgGrid(data=pd.DataFrame(data_fipe),fit_columns_on_grid_load=True)
                st.dataframe(data_fipe, use_container_width=True)

            else:
                st.info("Não foram encontrados informações para a consulta requerida")
    
    
    def search_fipe_code():
        ...

    if method == 'Veículo':
        search_fipe_vehicle()

    elif method == 'Código Fipe':
        search_fipe_code()
