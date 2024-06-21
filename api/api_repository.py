import requests


class GetCepApi:

    def __init__(self, cep=None, uf=None, locality=None, address=None):
        self.__url_base = 'https://viacep.com.br/ws'
        self.__get_cep = f'{self.__url_base}/{cep}/json'
        self.__get_address = f'{self.__url_base}/{uf}/{locality}/{address}/json'

    def get_cep_api(self):
        response = requests.get(self.__get_cep)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 400 or response.status_code == 401 or response.status_code == 404:
            return None

        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def get_address_api(self):
        response = requests.get(self.__get_address)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 400 or response.status_code == 401 or response.status_code == 404:
            return None

        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')


class GetCnpjApi:

    def __init__(self, cnpj):
        self.__url_base = 'https://receitaws.com.br/v1/cnpj'
        self.__get_cnpj = f'{self.__url_base}/{cnpj}/'

    def get_cnpj_api(self):
        response = requests.get(self.__get_cnpj)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 404 or response.status_code == 400 or response.status_code == 401:
            return None

        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')


class GetFipeApi:

    def __init__(self, type_vehicle=None, brand=None, model=None, year=None, fipe_code=None):
        self.__url_base = "https://parallelum.com.br/fipe/api/v2"
        self.__get_brands = f"{self.__url_base}/{type_vehicle}/brands"
        self.__get_models = f"{self.__get_brands}/{brand}/models"
        self.__get_years = f"{self.__get_models}/{model}/years"
        self.__get_fipe_code = f"{self.__url_base}/{type_vehicle}/{fipe_code}/years"
        self.__get_fipe_code_history = f"{self.__get_fipe_code}/{year}/history/"
        self.__get_fipe = f"{self.__url_base}/{type_vehicle}/brands/{brand}/models/{model}/years/{year}/"

    def get_fipe_vehicle_api(self):
        response = requests.get(self.__get_fipe)

        if response.status_code == 200:
            return response.json()

        if response.status_code != 200:
            return None

        raise Exception(f'Erro ao obter os dados da Tabela Fipe. Status code: {response.status_code}')

    def get_fipe_code_api(self):
        response = requests.get(self.__get_fipe_code)

        if response.status_code == 200:
            return response.json()

        if response.status_code != 200:
            return None

        raise Exception(f'Erro ao obter os dados da Tabela Fipe. Status code: {response.status_code}')

    def get_fipe_code_history_api(self):
        response = requests.get(self.__get_fipe_code_history)

        if response.status_code == 200:
            return response.json()

        if response.status_code != 200:
            return None

        raise Exception(f'Erro ao obter os dados da Tabela Fipe. Status code: {response.status_code}')

    def get_models_api(self):
        response = requests.get(self.__get_models)

        if response.status_code == 200:
            return response.json()

        if response.status_code != 200:
            return None

        raise Exception(f'Erro ao obter os dados da Tabela Fipe. Status code: {response.status_code}')

    def get_model_year_api(self):
        response = requests.get(self.__get_years)

        if response.status_code == 200:
            return response.json()

        if response.status_code != 200:
            return None

        raise Exception(f'Erro ao obter os dados da Tabela Fipe. Status code: {response.status_code}')


class GetIbgeApi:

    def __init__(self, uf):
        self.__url_base = 'https://brasilapi.com.br/api/ibge/municipios/v1'
        self.__get_cities = f'{self.__url_base}/{uf}?providers=dados-abertos-br,gov,wikipedia'

    def get_cities_api(self):
        response = requests.get(self.__get_cities)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 400 or response.status_code == 401 or response.status_code == 404:
            return None

        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')


class GetNcmApi:

    def __init__(self, ncm):
        self.__url_base = 'https://brasilapi.com.br/api/ncm/v1'
        self.__get_ncm = f"{self.__url_base}?search={ncm}"

    def get_ncm_api(self):
        response = requests.get(self.__get_ncm)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 400 or response.status_code == 401 or response.status_code == 404:
            return None

        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')
