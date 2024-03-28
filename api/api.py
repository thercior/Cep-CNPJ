import requests
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
        type_vehicle = args[0]
        url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/"

    elif 'type_vehicle' in kwargs and 'brands' in kwargs and 'model' in kwargs and 'year' in kwargs and 'fipe_code' in kwargs:
        type_vehicle = url_quote(kwargs['type_vehicle'])
        brands = (kwargs['brands'])
        model = url_quote(kwargs['model'])
        year = url_quote(kwargs['year'])
        fipe_code = url_quote(kwargs['fipe_code'])
        print(f'API: {type_vehicle} - {brands} - {model} - {year} - {fipe_code}')

        if type_vehicle and brands and model and year:
            url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/{brands}/models/{model}/years/{year}/"

        elif type_vehicle and brands and model:
            url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/{brands}/models/{model}/years/"

        elif type_vehicle and brands:
            url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/{brands}/models/"

        elif type_vehicle and fipe_code and year:
            url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/{fipe_code}/years/{year}/"

        elif type_vehicle and fipe_code:
            url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/{fipe_code}/years/"

        else:
            url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/{fipe_code}/years/{year}/history/"

    else:
        raise ValueError("Parâmetros Inválidos para Busca")

    try:
        print(url)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data:
            return data
        else:
            return None
    except requests.exceptions.RequestException as e:
        raise Exception(f'Erro na requisição: {str(e)}')


def fipe_brands_models_api(*args, **kwargs):

    if 'type_vehicle' in kwargs and 'brands' in kwargs and 'model' in kwargs and 'year' in kwargs:
        type_vehicle = url_quote(kwargs['type_vehicle'])
        brands = (kwargs['brands'])
        model = url_quote(kwargs['model'])

        if type_vehicle and brands:
            url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/{brands}/models/"

        elif type_vehicle and brands and model:
            url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/{brands}/models/{model}/years/"

    else:
        raise ValueError("Parâmetros Inválidos para Busca")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data:
            return data
        else:
            return None
    except requests.exceptions.RequestException as e:
        raise Exception(f'Erro na requisição: {str(e)}')


def fipe_model_year_api(*args, **kwargs):

    if 'type_vehicle' in kwargs and 'brands' in kwargs and 'model' in kwargs and 'year' in kwargs:
        type_vehicle = url_quote(kwargs['type_vehicle'])
        brands = (kwargs['brands'])
        model = url_quote(kwargs['model'])

        if type_vehicle and brands and model:
            url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/{brands}/models/{model}/years/"

        elif type_vehicle and brands:
            url = f"https://parallelum.com.br/fipe/api/v2/{type_vehicle}/brands/{brands}/models/"

    else:
        raise ValueError("Parâmetros Inválidos para Busca")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data:
            return data
        else:
            return None
    except requests.exceptions.RequestException as e:
        raise Exception(f'Erro na requisição: {str(e)}')


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
