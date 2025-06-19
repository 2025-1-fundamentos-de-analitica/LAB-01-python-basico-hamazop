"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import re

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    # Array to store the counting
    conteo = {}

    # Open the document
    data = open("files/input/data.csv", "r")

    # Read each line
    for line in data:
        value = int( line.strip().split("\t")[1] )
        new_list = line.strip().split("\t")[3].split(",")
        for element in new_list:
            if element in conteo:
                conteo[element] = conteo[element] + value
            else:
                conteo[element] = value
    claves_organizadas = sorted(conteo.items())
    conteo_organizado = dict(claves_organizadas)
    return conteo_organizado