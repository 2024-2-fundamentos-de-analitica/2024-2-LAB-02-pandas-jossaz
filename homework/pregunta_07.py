"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_07():
    tb0 = 'files/input/tbl0.tsv'
    df = pd.read_csv(tb0, sep='\t')

    sumas = df.groupby('c1')['c2'].sum()
    sumas.name = 'c2'

    return sumas

pregunta_07()

"""
Calcule la suma de la `c2` por cada letra de la `c1` del archivo
`tbl0.tsv`.

Rta/
c1
A    37
B    36
C    27
D    23
E    67
Name: c2, dtype: int64
"""
