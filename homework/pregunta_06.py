"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import math
import re

# We create a specific class to handle the data
class Node:

    # Constructor 
    def __init__(self, new_data: str):
        self.Data = new_data;
        self.Max = -math.inf;
        self.Min = math.inf;
        self.Next = None;
    
    def GetData(self):
        return self.Data;

    def GetNext(self):
        return self.Next;

    def SetNext(self, new_node: "Node"):
        self.Next = new_node;

    # Check the new number with the current max and min
    def Insert(self, new_number: int):
        if self.Max < new_number:
            self.Max = new_number;
        if self.Min > new_number:
            self.Min = new_number;
    
    # To String() Method
    def To_String(self):
        return (self.Data, self.Min, self.Max)

# We create a specific class to handle the nodes
class TupleList:

    # Constructor
    def __init__(self):
        self.Root = None;

    # Check if already exists
    def Exists(self, NewNode: "Node"):

        # Check if there is root
        if self.Root is None:
            return False
        
        # Create an iterator
        Temp = self.Root

        # While the iterator points has next
        while Temp.GetNext() is not None:

            # Check if the actual is same as new
            if Temp.GetData() == NewNode.GetData():

                # If it is return true
                return True
            
            # Get Next
            Temp = Temp.GetNext();

        # Check if the actual is same as new
        if Temp.GetData() == NewNode.GetData():
            # If it is return true
            return True
        
        # If it nevers is the same, return false
        return False
    
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

        # Sort the list
        aux.sort()

        # Give back the sorted list
        return aux

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    answer = TupleList()

    # Open the document
    data = open("files/input/data.csv", "r")

    # Read each line
    for line in data:
        sub_line = re.split(r"[,:]", line.strip().split("\t")[4])
        aux = 0
        while(aux < len(sub_line)):
            new_data = sub_line[aux]
            new_number = int( sub_line[aux+1] )

            NewNode = Node(new_data)
            # Check if the data exists
            if not answer.Exists(NewNode):
                # Add if it doesn't add it
                answer.Add(NewNode)
            answer.Compare(NewNode, new_number)
            aux = aux + 2
    return answer.Show()