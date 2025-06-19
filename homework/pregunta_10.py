"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import re

# We create a specific class to handle the data
class Node:

    # Constructor 
    def __init__(self, new_data: str, count_col4: int, count_col5: int):
        self.Data = new_data;
        self.Col4 = count_col4;
        self.Col5 = count_col5;
        self.Next = None;
    
    def GetData(self):
        return self.Data;

    def GetNext(self):
        return self.Next;

    def SetNext(self, new_node: "Node"):
        self.Next = new_node;
    
    # To String() Method
    def To_String(self):
        return (self.Data, self.Col4, self.Col5)

# We create a specific class to handle the nodes
class TupleList:

    # Constructor
    def __init__(self):
        self.Root = None;
    
    # Add() Method
    def Add(self, NewNode: "Node"):

        # If the list is NOT empty
        if self.Root is not None:

            # Get the existing root
            TupleIterator = self.Root
            
            # if NOT tail, move to the next one
            while TupleIterator.GetNext() is not None:
                TupleIterator = TupleIterator.GetNext()
            
            # At tail, add new node
            TupleIterator.SetNext(NewNode)
        
        # If the list is empty set it as Root
        else:
            self.Root = NewNode;

    # Compare the number for every item
    def Compare(self, NewNode: "Node", new_number: int):

        # Create an iterator
        Temp = self.Root

        # While the iterator is NOT the new one, get next
        while Temp.GetData() != NewNode.GetData():
            Temp = Temp.GetNext()
        
        # Try to replace the numbers
        Temp.Insert(new_number)
    
    # Show every element, sorted, with its data
    def Show(self):

        # Create an iterator
        Temp = self.Root

        # Create the list
        aux = []

        # While iterator has NEXT node
        while Temp.GetNext() is not None:

            # Add actual node
            aux.append(Temp.To_String())

            # Get NEXT node
            Temp = Temp.GetNext()
        
        # Once there is not NEXT node, add current one
        aux.append(Temp.To_String())

        # Give back the sorted list
        return aux

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    answer = TupleList()

    # Open the document
    data = open("files/input/data.csv", "r")

    # Read each line
    for line in data:

        # Extract the data and and the number
        new_data = line.strip().split("\t")[0]
        new_col4 = len( line.strip().split("\t")[3].split(",") )
        new_col5 = int( len(re.split(r"[,:]", line.strip().split("\t")[4]) ) / 2 )

        NewNode = Node(new_data, new_col4, new_col5)
        answer.Add(NewNode)

    return answer.Show()