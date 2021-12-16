import streamlit as st
from Metodo.solver import solve
import numpy as np
import pandas as pd

def main_page():
    st.title('Calculadora de Eliminación Gaussiana')
    row = int(st.number_input('Numero de filas o  incognitas', step=1,min_value=2))
    col = row + 1

    st.title('Ingresa los valores de tu matriz')
    st.text(""" 
        Ingresa los valores de cada columna separados por comas. Ej. 1,2,3. También 
        recuerda no sobrepasar el numero de columnas seleccionadas
        """)

    matrix = np.zeros((row,col))
    df = pd.DataFrame(matrix)

    for i in range(row):
        val = st.text_input(label=f"Fila: {i}").split(",")
        try:
            values = list(map(float, val))
            if len(values) > col:
                st.warning("Los valores deben ser del mismo tamaño que el numero de columnas")
            matrix[i] = values[:col]
            
        except ValueError:
            if val != ['']:
                st.warning("Ingresa los valores separados por comas. No ingreses letras o espacios")
            values = []


    st.title("Matriz")
    st.text("Aca podemos apreciar la matriz con los valores correspondientes")
    st.table(df)

    btn = st.button(label='Calcular')
    if btn:
        if val == ['']:
            st.warning("Debes ingresar valores en la matriz")
        else:
            result = solve(matrix)
            if result =='Error':
                st.warning('Soluciones infinitas o sin solución')
            else:
                st.title("Resultados")
                for key in result.keys():
                    st.subheader(f'{key} = {result[key]}')
