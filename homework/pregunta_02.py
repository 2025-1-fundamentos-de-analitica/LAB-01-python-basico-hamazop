"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    # Create an empty dictionary
    answer = {}

    # Open the document
    data = open("files/input/data.csv", "r")

    # Read each line
    for line in data:

        # Extract the letter
        letter = line.strip().split("\t")[0]

        # Check if it exists in the dicionary

        # If it does increase its counter
        if letter in answer:
            answer[letter] = answer[letter] + 1

        # If it doesn't start the counter
        else:
            answer[letter] = 1

    # Return the dictionary as a list of tuples 
    return sorted(answer.items())