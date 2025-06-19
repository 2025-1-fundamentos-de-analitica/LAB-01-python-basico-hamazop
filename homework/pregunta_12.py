"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import re

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    # Array to store the counting
    conteo = {}

    # Open the document
    data = open("files/input/data.csv", "r")

    c = 0

    for line in data:
        key = line.strip().split("\t")[0]
        values = sub_line = re.split(r"[,:]", line.strip().split("\t")[4])
        aux = 0
        while(aux < len(sub_line)):
            if key in conteo:
                conteo[key] = conteo[key] + int( sub_line[aux+1] )
            else:
                conteo[key] = int( sub_line[aux+1] )
            aux = aux + 2
    
    claves_organizadas = sorted(conteo.items())
    conteo_organizado = dict(claves_organizadas)
    return conteo_organizado