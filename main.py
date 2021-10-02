from arquivo_classificador_de_imagem import funcao_classificar_imagem
import streamlit as st
from PIL import Image

# TÍTULO DO SITE.
st.title("Mask helper.")

# BOTÃO PARA FAZER UPLOAD DA IMAGEM A SER CLASSIFICADA.
uploaded_file = st.file_uploader("Escolha um arquivo", type=["jpeg", "jpg", "gif"] )

# CLASSIFICAÇÃO DA IMAGEM.
if uploaded_file is not None:

    # ABRIR A IMAGEM CARREGADA.
    image = Image.open(uploaded_file)

    # MOSTRAR A IMAGEM.
    st.image(image, caption='', use_column_width=True)

    # TEXTO INDICANDO QUE A IMAGEM ESTÁ SENDO CLASSIFICADA.
    st.write("Classificando...")

    # CHAMAR A FUNÇÃO DE CLASSIFICAÇÃO DE IMAGEM
    # E ARMAZENAR O RESULTADO NA VARIÁVEL LABEL.
    label = funcao_classificar_imagem(uploaded_file, '/content/keras_model.h5')

    # CONDICIONAL PARA IDENTIFICAR A CLASSE DA IMAGEM.
    if label == 0:

        # INSIRA O NOME DA PRIMEIRA CLASSE.
        st.write("com máscara.")

    elif label == 1:

       # INSIRA O NOME DA SEGUNDA CLASSE.
        st.write("sem máscara.")
    else:

      # INSIRA O NOME DA TERCEIRA CLASSE.
        st.write("Máscara para baixo")
