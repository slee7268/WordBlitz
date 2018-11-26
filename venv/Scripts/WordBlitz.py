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
#manhsdtan
class Edge:
    def __init__(self, start, end, weight):
        self.start=start
        self.end=end
        self.weight=weight

class letterGrid:
    def __init__(self, size=4):
        self.size=size
    def genRandomGrid(self):
        #initialize 2d Array
        letterArr=[["fill" for i in range(self.size)] for j in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                randLetter=random.choice(string.ascii_uppercase)
                letterArr[i][j]=Letter(randLetter, scrabbleDict[randLetter], [])

        letterArr=np.array(letterArr)

        return letterArr
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
#register edges

def score(path, grid):
    return 100

def BruteForce(grid):
    return 1000

def displayGrid(grid):
    letters=(list(l.name for row in grid for l in row))
    #l for l in letters
    letterMat=np.reshape(letters, (4,4))
        #np.array([[l for l in letters for i in range(4)] for j in range(4)])
    print(letterMat)
    return (letterMat)



L1 = Letter("E", 2, [])
L2=Letter("T", 3, [])
L3=Letter("D", 3, [])
E1=Edge(L1, L2, 5)
E2=Edge(L1, L3, 5)
L1.addEdge(E1)
#L1.addEdge(E2)
L2.getNeighbors()

grid=letterGrid(4)
randGrid=grid.genRandomGrid()
randGrid=grid.connectGrid(randGrid)

disp=displayGrid(randGrid)


#print(disp[0,1].value)

