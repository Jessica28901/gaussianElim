import streamlit as st

def code_page():
    st.title('Código de la calculadora')
    st.text("""
    Funcion principal. Determina si la matriz tiene solucion.En caso de que si, 
    llama a la funcion que empieza el metodo de eliminacion gaussiana
        """)
    st.code("""
        def solve(matrix):                     
            row = matrix.shape[0] # numero de filas
            columns = matrix.shape[1] # numero de columnas

            #Nos interesa obtener la matriz cuadrada asi podemos calcular 
            # el determinante y saber sus soluciones
            m = np.array([matrix[i][:columns-1] for i in range(row)])

            #Si el determinante es cero
            det = round(np.linalg.det(m))
            if det == 0:
                return 'infinite number of solutions or no solution'
            else:
                return gaussian_elim(matrix)
        """)

    st.text("""
    La siguiente funcion que lleva acabo el procedimiento principal. Crea la 
    diagonal de unos y añade los ceros. Basicamente resuelve utilizando el metodo
        """)
    st.code("""
        def gaussian_elim(matrix):
            rows = matrix.shape[0]
            for i in range(rows):
                j=0
                while i > j:
                    matrix[i] = matrix[i] - matrix[j]*matrix[i][j]
                    j+=1
                matrix[i] = matrix[i]/matrix[i][i]
            return get_result(matrix)
        """,language="python")

    st.text(""" 
    Ultima funcion. Una vez teniendo la matriz resuelta, se encarga de 
    resolver las ultimas operaciones para asi obtener los valores de cada variable 
    correspondiente""")
    st.code(""" 
        VARIABLES = ['x','y','z','a','b','c','d','e','f','g','h','i','j','k']
        def get_result(matrix):
            values = [] 
            rows = matrix.shape[0] 

            for i in range(rows-1,-1,-1): 
                idx = 0
                x = -2
                variable = matrix[i][-1] 
                while idx < len(values): 
                    variable -=matrix[i][x]*values[idx]
                    idx+=1
                    x-=1
                values.append(variable) 
            result = {VARIABLES[i]:values[::-1][i] for i in range(len(values))}
            return result
        """)