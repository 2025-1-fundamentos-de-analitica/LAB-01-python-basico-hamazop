"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import re

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    # Array to store the counting
    conteo = {}

    # Open the document
    data = open("files/input/data.csv", "r")

    # Read each line
    for line in data:
        sub_line = re.split(r"[,:]", line.strip().split("\t")[4])
        aux = 0
        while(aux < len(sub_line)):
            new_data = sub_line[aux]
            if new_data in conteo:
                conteo[new_data] = conteo[new_data] + 1
            else:
                conteo[new_data] = 1
            aux = aux + 2

    claves_organizadas = sorted(conteo.items())
    conteo_organizado = dict(claves_organizadas)
    return conteo_organizado