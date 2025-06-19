"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    # Create an empty dictionary
    answer = {}

    # Open the document
    data = open("files/input/data.csv", "r")

    # Read each line
    for line in data:

        # Extract the month
        month = line.strip().split("\t")[2].split("-")[1]

        # Check if it exists in the dicionary
        
        # If it does increase its counter
        if month in answer:
            answer[month] = answer[month] + 1

        # If it doesn't start the counter
        else:
            answer[month] = 1
    
    return sorted(answer.items())