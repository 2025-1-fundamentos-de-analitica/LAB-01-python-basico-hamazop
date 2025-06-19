"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

# We create a specific class to handle the data
class Node:

    # Constructor 
    def __init__(self, new_code: int):
        self.Code = new_code;
        self.Array = []
        self.Next = None;
    
    def GetCode(self):
        return self.Code;

    def GetNext(self):
        return self.Next;

    def SetNext(self, new_node: "Node"):
        self.Next = new_node;

    # Check the new letter with the current max and min
    def Insert(self, new_letter):
        self.Array.append(new_letter)
    
    # To String() Method
    def To_String(self):
        return (self.Code, self.Array)

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
            if Temp.GetCode() == NewNode.GetCode():

                # If it is return true
                return True
            
            # Get Next
            Temp = Temp.GetNext();

        # Check if the actual is same as new
        if Temp.GetCode() == NewNode.GetCode():
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
    # Compare the letter for every item
    def Store(self, NewNode: "Node", new_letter: str):

        # Create an iterator
        Temp = self.Root

        # While the iterator is NOT the new one, get next
        while Temp.GetCode() != NewNode.GetCode():
            Temp = Temp.GetNext()
        
        # Try to replace the letters
        Temp.Insert(new_letter)
    
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

        # Sort the array
        aux.sort()

        # Give back the sorted list
        return aux

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    answer = TupleList()

    # Open the document
    data = open("files/input/data.csv", "r")

    count = 0

    # Read each line
    for line in data:
        new_code = int( line.strip().split("\t")[1] )
        new_letter = line.strip().split("\t")[0]

        NewNode = Node(new_code)
        # Check if the data exists
        if not answer.Exists(NewNode):
            # Add if it doesn't add it
            answer.Add(NewNode)
        answer.Store(NewNode, new_letter)
    return answer.Show()