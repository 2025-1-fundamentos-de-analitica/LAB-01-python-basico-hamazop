"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

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

        # If it does add the number
        if letter in answer:
            answer[letter] = answer[letter] + int( line.strip().split("\t")[1] )

        # If it doesn't we start the counter
        else:
            answer[letter] = int( line.strip().split("\t")[1] )

    # Return the dictionary as a list of tuples 
    return sorted(answer.items())