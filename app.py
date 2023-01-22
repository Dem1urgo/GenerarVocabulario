import streamlit as st
import re

# importamos la libreria

st.title("Vocabulario")
# titulo de la pagina

st.image("https://www.lavanderablanca.com/wp-content/uploads/2016/09/La-letra-de-plomo_interior_023.jpg",
            width=400)

st.header('Aplicación para generar el vocabulario de un texto sin sus signos de puntuación.')

title = st.text_input('Introduce el texto a analizar: ')




def generar_vocabulario(cadena):
    # Eliminar signos de puntuación
    cadena = re.sub(r'[^\w\s]', '', cadena)
    # Poner todas las palabras en minúscula
    cadena = cadena.lower()
    # Generar vocabulario
    vocabulario = set(cadena.split())
    return vocabulario



cont = 2
# if st.button("Pulsa para el vocabulario",):
vocabulario = generar_vocabulario(title)
if  len(vocabulario) != 0:
    st.text(f'El vocabulario del texto introducido es {vocabulario}')