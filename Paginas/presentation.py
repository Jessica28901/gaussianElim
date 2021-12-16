import streamlit as st
from PIL import Image

def pag_presentacion():  
    title = """
    <div class="title">
        <h1>Universidad Tecnológica de Panamá</h1>
        <h2>Facultad de Ingeniería Industrial</h2>
    </div>
    <h2 class="materia">Licenciatura en Ingeniería Industrial</h2>
    <h2 class="materia">Métodos Numéricos</h2>
    <h2 class="materia">Trabajo Semestral</h2>
    <div class="integrantes">
        <h3>MARIO CANDANEDO  8-980-1027</h3>
        <h3>JESSICA QUIJADA 8-936-1539 </h3>
        <h3>ANDREA RAMOS 8-948-2495</h3>
        <h3>ZURISADAI ZUÑIGA 8-982-974</h3>
    </div>
    <h3 class="profesor">Ing. Samuel Jiménez</h3>
    <h3>2ndo Semestre 2021</h3>
    <style>
        h3,
        h2 {
        text-align: center;
        }
        .title {
        width: 100%;
        margin-bottom: 100px;
        text-align: center;
        }
        .integrantes {
        width: 100%;
        margin-bottom: 100px;
        text-align: center;
        }
        .materia {
        margin-bottom: 100px;
        }
        .profesor{
            margin-bottom:100px;
        }
    </style>
    """
    st.markdown(title, unsafe_allow_html=True)


def pag_finalizacion():
    title = """
    <h1 class="title">¡Gracias por todo!</h1>
     <h2> Espero tenga feliz navidad y prospero año nuevo</h2>
        <style>
        h1,h2{
        width: 100%;
        text-align: center;
        letter-spacing:1px;
        margin-bottom:20px;
        }
    </style>
    """
    st.markdown(title , unsafe_allow_html=True)
    image = Image.open(r"navidad.png")
    st.image(image)
