import requests
from urllib.parse import quote as url_quote


def format_cep(cep_input):
    # Remove caracteres não numéricos
    cep = ''.join(filter(str.isdigit, cep_input))
    # Limita a 8 digitos
    cep = cep[:8]
    return cep


def cep_api(*args, **kwargs):
    # URL da ViaCEP
    print(args)
    print(kwargs)
    if args:
        url = f"https://viacep.com.br/ws/{args[0]}/json"
        print(url)
    elif 'uf' in kwargs and 'localidade' in kwargs and 'logradouro' in kwargs:
        uf = url_quote(kwargs['uf'])
        localidade = url_quote(kwargs['localidade'])
        logradouro = url_quote(kwargs['logradouro'])
        url = f"https://viacep.com.br/ws/{uf}/{localidade}/{logradouro}/json"
        print(url)
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
    ...
