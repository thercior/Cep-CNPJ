from components.button import button_search
from fipe.service import FipeService
from utils.fipe_choices import vehicle_choices, cars_brands_choices, motorcycles_brands_choices, trucks_brands_choices
import pandas as pd
import streamlit as st


class FipeSearch:

    def __init__(self):
        self.method = st.radio('Escolha o método de busca:', options=['Veículo', 'Código Fipe'], horizontal=True)
        self.col1, self.col2, self.col3, self.col4 = st.columns(4, gap="large")
        self.colA, self.colB, self.colC = st.columns(3, gap="large")
        self.bt_search = button_search("Consultar")

    def search_fipe(self):
        if self.method == 'Veículo':
            self.search_by_vehicle()

        elif self.method == 'Código Fipe':
            self.search_by_cod_fipe()

    def search_by_vehicle(self):
        with self.col1:
            vehicle_select = st.selectbox('Selecione o tipo de veículo:', [vehicle[1] for vehicle in vehicle_choices])
            type_vehicle = [type_vehicle for type_vehicle, vehicle in vehicle_choices if vehicle == vehicle_select][0]

        with self.col2:
            match vehicle_select:
                case 'Carros':
                    brands_cars = st.selectbox('Selecione a marca do carro', [brand[1] for brand in cars_brands_choices])
                    brands = [brands for brands, brand in cars_brands_choices if brand == brands_cars][0]

                case 'Motos':
                    brands_motorcycles = st.selectbox('Selecione uma marca de moto', [brand[1] for brand in motorcycles_brands_choices])
                    brands = [brands for brands, brand in motorcycles_brands_choices if brand == brands_motorcycles][0]

                case 'Caminhões':
                    brands_trucks = st.selectbox('Selecione a marca do caminhão', [brand[1] for brand in trucks_brands_choices])
                    brands = [brands for brands, brand in trucks_brands_choices if brand == brands_trucks][0]

        with self.col3:
            model_service = FipeService(
                type_vehicle=type_vehicle,
                brand=brands,
            )
            data_model = model_service.get_model()

            if data_model:
                model_select = st.selectbox('Selecione o modelo do veículo:', [model['name'] for model in data_model])
                model = next(model['code'] for model in data_model if model['name'] == model_select)
            else:
                if brands == 0:
                    model = ''
                else:
                    st.info('Não foi possível obter os modelos da API. Limite excedido')
                    model = ''

        with self.col4:
            model_year_service = FipeService(
                type_vehicle=type_vehicle,
                brand=brands,
                model=model
            )
            data_model_year = model_year_service.get_model_year()

            if data_model_year:
                year_select = st.selectbox('Selecione o ano do modelo:', [year['code'] for year in data_model_year])
                year = year_select

        if self.bt_search:
            data_fipe_service = FipeService(
                type_vehicle=type_vehicle,
                brand=brands,
                model=model,
                year=year,
            )
            data_fipe = [data_fipe_service.get_fipe_vehicle()]

            if data_fipe:
                st.dataframe(data_fipe, use_container_width=True)
            else:
                st.info("Não foram encontrados informações para o veículo consultado")

    def search_by_cod_fipe(self):
        with self.colA:
            vehicle_select = st.selectbox('Selecione o tipo de veículo:', [vehicle[1] for vehicle in vehicle_choices])
            type_vehicle = [type_vehicle for type_vehicle, vehicle in vehicle_choices if vehicle == vehicle_select][0]

        with self.colB:
            fipe_code = st.text_input('Digite o Código Fipe do veículo')

        with self.colC:
            model_year_service = FipeService(
                type_vehicle=type_vehicle,
                fipe_code=fipe_code,
            )
            data_model_year = model_year_service.get_fipe_code_year()

            if data_model_year:
                year_select = st.selectbox('Selecione o ano do modelo', [year['code'] for year in data_model_year])
                year = year_select

        if self.bt_search:
            data_fipe_service = FipeService(
                type_vehicle=type_vehicle,
                fipe_code=fipe_code,
                year=year,
            )

            data_fipe = data_fipe_service.get_fipe_code_history()

            if data_fipe:
                price_history = data_fipe.pop('priceHistory')
                price_df = pd.DataFrame(price_history)

                for key, value in data_fipe.items():
                    price_df[key] = value

                price_df = price_df[['brand', 'model', 'modelYear', 'fuel', 'codeFipe', 'fuelAcronym', 'price', 'month', 'reference']]

                st.dataframe(price_df, use_container_width=True)
            else:
                st.info("Não foram encontrados informações para o veículo consultado")
