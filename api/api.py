import requests
import streamlit as st
from urllib.parse import quote as url_quote


def cep_api(*args, **kwargs):

    # Argumentos para busca pelo cep
    if args:
        cep = args[0]
        url = f"https://viacep.com.br/ws/{cep}/json"

    # Argumentos para busca por endereço
    elif 'uf' in kwargs and 'localidade' in kwargs and 'logradouro' in kwargs:
        uf = url_quote(kwargs['uf'])
        localidade = url_quote(kwargs['localidade'])
        logradouro = url_quote(kwargs['logradouro'])
        url = f"https://viacep.com.br/ws/{uf}/{localidade}/{logradouro}/json"

    else:
        raise ValueError("Parâmetros Inválidos para Busca")

    try:
        # Faz a requisição
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise Exception(f'Erro na requisição: {str(e)}')


def cnpj_api(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if data:
        return data
    else:
        return None


def fipe_api(*args, **kwargs):

    if args:
        fipe_id = args[0]
        url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands"

    elif ('type_vehicle' and 'brands' and 'model' and 'year' and 'fipe_code') in kwargs:
        type_vehicle = url_quote(kwargs['type_vehicle'])
        brands = url_quote(kwargs['brands'])
        model = url_quote(kwargs['model'])
        year = url_quote(kwargs['year'])
        fipe_code = url_quote(kwargs['fipe_code'])

        case_brands = True if type_vehicle and brands else False
        case_models = True if type_vehicle and brands and model else False
        
        url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/"
        url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/{fipe_code}/years/"
        url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/{fipe_code}/years/{year}/"
        url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/{fipe_code}/years/{year}/history/"
        url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/{brands}/models/"
        url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/{brands}/models/{model}/years/"
        url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/{brands}/models/{model}/years/{year}/"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data:
            return data
        else:
            return None
    else:
        raise ValueError("Parâmetros Inválidos para Busca")


def ibge_api(uf):
    url = f"https://brasilapi.com.br/api/ibge/municipios/v1/{uf}?providers=dados-abertos-br,gov,wikipedia"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if data:
        return data
    else:
        return None


def ncm_api(code):
    url = f"https://brasilapi.com.br/api/ncm/v1?search={code}"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if data:
        return data
    else:
        return None
