"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    total = 0
    
    data = open("../files/input/data.csv", "r")

    for line in data:
        total = total + int( line.strip().split("\t")[1] )

    return total