def format_cep(cep_input):
    # Remove caracteres não numéricos
    cep = ''.join(filter(str.isdigit, cep_input))
    # Limita a 8 digitos
    cep = cep[:8]
    return cep
