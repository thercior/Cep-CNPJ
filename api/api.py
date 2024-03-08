import requests
import streamlit as st
from urllib.parse import quote as url_quote


def cep_api(*args, **kwargs):
    # URL da ViaCEP

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
