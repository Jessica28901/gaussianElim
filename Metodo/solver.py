import numpy as np

VARIABLES = ['x','y','z','a','b','c','d','e','f','g','h','i','j','k']
def get_result(matrix):
  """ 
  Una vez teniendo la matriz resuelta, se encarga de resolver las 
  ultimas operaciones para asi obtener los valores
  correspondientes
  """
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

def gaussian_elim(matrix):
  """ 
  Funcion que lleva acabo el procedimiento principal. Basicamente crea la 
  diagonal de unos y añade los ceros 
  """
  rows = matrix.shape[0]
  for i in range(rows):
    j=0
    while i > j:
      matrix[i] = matrix[i] - matrix[j]*matrix[i][j]
      j+=1
    matrix[i] = matrix[i]/matrix[i][i]
  return get_result(matrix)

def solve(matrix):     
    """ 
    Funcion principal, determina si la matriz tiene solucion. 
    En caso de que si, llama a la funcion que empieza el 
    metodo
    """                 
    row = matrix.shape[0]
    columns = matrix.shape[1]
    m = np.array([matrix[i][:columns-1] for i in range(row)])
    det = round(np.linalg.det(m))
    if det == 0:
      return 'Error'
    else:
      return gaussian_elim(matrix)

