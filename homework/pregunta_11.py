"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def manipulacion(lista):
     tuplas = []

     # Se itera sobre los valores, separando clave y valor
     for clave, valor in lista:
          # Se ordena
          valor = sorted(valor)

     #    # Se convierte cada elemento a str
     #    valor = list(map(str, valor))
          
          # Se separa por guiones
          valor = ','.join(valor)

          # Se arregla el retorno
          tuplas.append([clave,valor])

     return tuplas

def pregunta_11():
     tb1 = 'files/input/tbl1.tsv'
     df = pd.read_csv(tb1, sep='\t')

     # Tomamos lo que necesitamos para operarlo aparte
     agrupado = df.groupby('c0')['c4']

     # Lo convertimos a una lista
     agrupado_array = [(clave, valor.to_numpy().tolist()) for clave, valor in agrupado]

     # Se obtienen los datos manipulados en formato de lista y se convierten a df
     datos_manipulados = manipulacion(agrupado_array)
     df_manipulado = pd.DataFrame(datos_manipulados, columns=['c0','c4'])

     return df_manipulado

pregunta_11()
"""
Construya una tabla que contenga `c0` y una lista separada por ',' de
los valores de la columna `c4` del archivo `tbl1.tsv`.

Rta/
     c0       c4
0     0    b,f,g
1     1    a,c,f
2     2  a,c,e,f
3     3      a,b
...
37   37  a,c,e,f
38   38      d,e
39   39    a,d,f
"""
