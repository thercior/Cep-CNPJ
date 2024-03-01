import pandas as pd
import locale


# Configurações da biblioteca para converter de um sistema para outro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


# Formatar moeda
def decimal_treat(decimal_str):
    treat_value = locale.currency(float(decimal_str), grouping=True)
    return treat_value


# Função para retornar a Atividade principal personalizada
def format_ativity_primary(data):

    if data['atividade_principal']:
        code = data['atividade_principal']['code']
        text = data['atividade_principal']['text']
        return f"Código CNAE: {code}\nAtividade: {text}"
    else:
        return None


# Função para retornar as Atividades secundárias personalizadas
def format_ativity_secondary(data):

    if data['atividades_secundarias']:
        ativity_formats = []

        for ativity in data['atividades_secundarias']:
            code = ativity['code']
            text = ativity['text']
            ativity_formats.append(f"Código CNAE: {code} | Atividade: {text}")

        return "\n".join(ativity_formats) if ativity_formats else None


def format_cnpj(cnpj_input):
    cnpj = ''.join(filter(str.isdigit, cnpj_input))  # Remove caracteres não numéricos
    cnpj = cnpj[:14]  # Limita a 14 digitos
    return cnpj


# Tratamento dos dados retornados da request
def df_data(data_cnpj):
    fields_company = [
        "status", "ultima_atualizacao", "cnpj", "tipo", "porte", "nome",
        "fantasia", "abertura", "atividade_principal", "atividades_secundarias",
        "natureza_juridica", "logradouro", "numero", "complemento", "cep",
        "bairro", "municipio", "uf", "email", "telefone", "situacao", "data_situacao",
        "motivo_situacao", "capital_social",
    ]

    data_cnpj_company = [data_cnpj[field] for field in fields_company]
    data_cnpj_company[-1] = decimal_treat(data_cnpj["capital_social"])
    df_cnpj = pd.DataFrame(data_cnpj_company, index=fields_company).pop(0)
    df_cnpj['atividade_principal'] = df_cnpj['atividade_principal'].pop(0)
    df_cnpj['atividade_principal'] = format_ativity_primary(df_cnpj)
    df_cnpj['atividades_secundarias'] = format_ativity_secondary(df_cnpj)

    return df_cnpj
