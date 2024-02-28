import streamlit as st
from streamlit.components.v1 import html
# from components.inputs import input_cep


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
