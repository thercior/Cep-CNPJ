import streamlit as st


def mask_cep():
    html_str = f"""
        <style>
            #cep_input::-webkit-outer-spin-button,
            #cep_input::-webkit-inner-spin-button {{
                -webkit-appearance: none;
                margin: 0;
            }}
            #cep_input[type=number] {{
                -moz-appearance: textfield;
            }}
            #cep_input {{
                text-align: center;
            }}
        </style>
    """

    return st.markdown(html_str, unsafe_allow_html=True)


# def mask_cnpj(*args, **kwargs):
#     cnpj = args[0]
#     cnpj_mask = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
#     return cnpj_mask


def mask_cnpj():
    script = """
        <script>
            // Função para aplicar a máscara de CNPJ
            function aplicarMascaraCNPJ(valor) {
                valor = valor.replace(/\D/g, ''); // Remove caracteres não numéricos
                valor = valor.replace(/^(\d{2})(\d)/, '$1.$2'); // Adiciona ponto após os dois primeiros dígitos
                valor = valor.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3'); // Adiciona ponto após os três primeiros dígitos
                valor = valor.replace(/\.(\d{3})(\d)/, '.$1/$2'); // Adiciona barra após os três dígitos seguintes
                valor = valor.replace(/(\d{4})(\d)/, '$1-$2'); // Adiciona hífen após os quatro dígitos seguintes
                return valor;
            }

            // Função para atualizar o valor do campo CNPJ
            function atualizarCNPJ() {
                var input = document.getElementById("cnpj_input");
                input.value = aplicarMascaraCNPJ(input.value);
            }

            // Adiciona um ouvinte de eventos para atualizar o valor quando o usuário digitar
            document.getElementById("cnpj_input").addEventListener("input", atualizarCNPJ);
        <script>
    """

    return script
