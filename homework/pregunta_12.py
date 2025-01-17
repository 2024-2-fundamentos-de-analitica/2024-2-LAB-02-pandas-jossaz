"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

#
# Se toman los valores agrupados en formato de lista y se retornan como diccionario
# Cada clave equivale al valor de c0, y cada valor de una clave corresponde a una lista con
# los valores combinados de c5a:c5b para cada valor de c0. Estos ya estan ordenados
#
def list_to_dic(lista):
     dic = {}

     # Se itera sobre la lista de valores, acumulando las cadenas en un diccionario
     # según su clave
     for clave, c5a, c5b in lista:
          # Se convierte de in a str
          c5b = str(c5b)

          # Si no esta en el diccionario, se crea
          if clave not in dic:
               dic[clave] = [c5a+':'+c5b]
          else:
               dic[clave].append(c5a+':'+c5b)
     
     # Se ordenan las listas y se convierten en cadenas
     for clave in dic:
          dic[clave] = sorted(dic[clave])

          dic[clave] = ','.join(dic[clave])
     
     return dic
     

def pregunta_12():
     tb2 = 'files/input/tbl2.tsv'
     df = pd.read_csv(tb2, sep='\t')

     # Tomamos lo que necesitamos para operarlo aparte
     agrupado = df[['c0','c5a','c5b']].groupby('c0')

     # Lo convertimos a una lista
     resultado_lista = []
     for group in agrupado:
          resultado_lista.extend(group[1].values.tolist())

     # Se toman los datos manipulados
     datos = list_to_dic(resultado_lista).items()

     # Se crea el nuevo dataframe
     df_manipulado = pd.DataFrame(datos,columns=['c0','c5'])
     
     return df_manipulado


pregunta_12()
"""
Construya una tabla que contenga `c0` y una lista separada por ','
de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
tabla `tbl2.tsv`.

Rta/
     c0                                   c5
0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
1     1              aaa:3,ccc:2,ddd:0,hhh:9
2     2              ccc:6,ddd:2,ggg:5,jjj:1
...
37   37                    eee:0,fff:2,hhh:6
38   38                    eee:0,fff:9,iii:2
39   39                    ggg:3,hhh:8,jjj:5
"""
