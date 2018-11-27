import string
import random
from array import *
import numpy as np
scrabbleDict={
    "E" : 1, "A" : 1, "I" : 1, "O" : 1, "S" : 1, "N" : 1, "R" : 1, "T" : 1, "L" : 1, "U" : 1,
    "D" : 2, "G" : 2, "B" : 3, "C" : 3, "M" : 3, "P" : 3, "F": 4 , "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5, "J": 8, "X": 8, "Q": 10, "Z":10
}

class Letter:
    def __init__(self, name, value, edgeList, multi=1):
        self.name=name
        self.value=value
        self.edgeList=[]
        self.multi=multi
    def dataOutput(self):
        print("The Letter is: " +self.name+" The value is: " +str(self.value) + " The multiplier is: " + str(self.multi))
    def addEdge(self, edge):
        if(edge.start!=self):
            print("Can't add an Edge because start attribute does not match")
        else:
            self.edgeList.append(edge)
            edge1=Edge(edge.end, edge.start, edge.weight)
            edge.end.edgeList.append(edge1)
    def getNeighbors(self):
        for i in self.edgeList:
            print(i.end.name)
    def getNumNeighbors(self):
        print(len(self.edgeList))

class Edge:
    def __init__(self, start, end, weight):
        self.start=start
        self.end=end
        self.weight=weight

class letterGrid:
    def __init__(self, size=4):
        self.size=size
    #generate random Grid of Letter objects
    def genRandomGrid(self):
        #initialize 2d Array
        letterArr=[["fill" for i in range(self.size)] for j in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                randLetter=random.choice(string.ascii_uppercase)
                letterArr[i][j]=Letter(randLetter, scrabbleDict[randLetter], [])

        letterArr=np.array(letterArr)
        return letterArr
    #register edges
    def connectGrid(self, letterArr):
        for i in range(self.size):
            for j in range(self.size):
                if(i+1<self.size):
                    edge=Edge(letterArr[i][j], letterArr[i+1][j], letterArr[i][j].value + letterArr[i+1][j].value)
                    letterArr[i][j].addEdge(edge)
                if(j+1<self.size):
                    edge = Edge(letterArr[i][j], letterArr[i][j+1], letterArr[i][j].value + letterArr[i][j+1].value)
                    letterArr[i][j].addEdge(edge)
                if(j+1< self.size & i+1<self.size):
                    edge = Edge(letterArr[i][j], letterArr[i + 1][j+1], letterArr[i][j].value + letterArr[i + 1][j+1].value)
                    letterArr[i][j].addEdge(edge)
                if(i+1<self.size and j-1>0):
                    edge = Edge(letterArr[i][j], letterArr[i + 1][j-1], letterArr[i][j].value + letterArr[i + 1][j-1].value)
                    letterArr[i][j].addEdge(edge)
        return letterArr


def displayGrid(grid):
    letters=(list(l.name for row in grid for l in row))
    letterMat=np.reshape(letters, (4,4))
    print(letterMat)
    return (letterMat)

