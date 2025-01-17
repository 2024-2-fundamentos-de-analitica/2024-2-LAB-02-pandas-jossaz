"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_06():
    tb1 = 'files/input/tbl1.tsv'
    df = pd.read_csv(tb1, sep='\t')

    # Se puede usar .unique  (array de numpy) ó .drop_duplicates (forma de dataframe)
    unicos = df['c4'].drop_duplicates()
    # Se pone en mayuscula y se ordena (con pandas)
    #unicos['c4'] = unicos['c4'].str.upper()
    #unicos = unicos.sort_values(by='c4')
    # Se convierte en lista
    unicos = unicos.tolist()
    # Se ordena
    unicos = sorted(unicos)
    # Se poner en mayuscula
    unicos = [letra.upper() for letra in unicos]

    return unicos

pregunta_06()

"""
Retorne una lista con los valores unicos de la columna `c4` del archivo
`tbl1.csv` en mayusculas y ordenados alfabéticamente.

Rta/
['A', 'B', 'C', 'D', 'E', 'F', 'G']

"""
