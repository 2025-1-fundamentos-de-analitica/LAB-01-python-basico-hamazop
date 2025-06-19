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

    # Counter
    total = 0

    # Open the document
    data = open("files/input/data.csv", "r")

    # Read each line
    for line in data:

        # Extract the number then add it to the total
        total = total + int( line.strip().split("\t")[1] )

    # Return the total
    return total