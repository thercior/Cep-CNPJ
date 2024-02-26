import requests


def format_cep(cep_input):
    # Remove caracteres não numéricos
    cep = ''.join(filter(str.isdigit, cep_input))
    # Limita a 8 digitos
    cep = cep[:8]
    return cep

def cep_api(*args, **kwargs):
    # URL da ViaCEP
    print(args)
    if 'cep' in args:
        url = f"https://viacep.com.br/ws/{args['cep']}/json"
        print(url)
    elif 'uf' in args and 'localidade' in args and 'logradouro' in args:
        url = f"https://viacep.com.br/ws/{args['uf']}/{args['localidade']}/{args['logradouro']}/json"
    else:
        raise ValueError("Parâmetros Inválidos para Busca")

    try:
        # Faz a requisição
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise Exception(f'Erro na requistição: {str(e)}')

def cnpj_api(cnpj):
    ...
