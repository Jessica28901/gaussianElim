import streamlit as st
from Paginas.code_page import code_page
from Paginas.main_page import main_page
from Paginas.presentation import pag_presentacion,pag_finalizacion

option = 'Presentación'
option = st.sidebar.selectbox('¿Que deseas hacer?',('Presentación','Utilizar la calculadora','Ver codigo fuente','Finalización'))

if option == 'Presentación':
    pag_presentacion()
if option == 'Utilizar la calculadora':
    main_page()
if option == 'Ver codigo fuente':
    code_page()
if option == 'Finalización':
    pag_finalizacion()