import requests


class GetCNPJAPI:

    def __init__(self, cnpj):
        self.__url_base = 'https://receitaws.com.br/v1/cnpj'
        self.__get_cnpj = f'{self.__url_base}/{cnpj}/'

    def get_cnpj(self):
        response = requests.get(self.__get_cnpj)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 404 or response.status_code == 400 or response.status_code == 401:
            return None

        raise Exception(f'Erro ao obter os dados da API. Status code: {response.status_code}')


class GetNCMAPI:

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
