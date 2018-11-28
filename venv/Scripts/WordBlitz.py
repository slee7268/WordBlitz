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
    def __init__(self, name, value, edgeList, degree, multi=1):
        self.name=name
        self.value=value
        self.edgeList=[]
        self.multi=multi
        self.degree=0
    def dataOutput(self):
        print("The Letter is: " +self.name+" The value is: " +str(self.value) + " The multiplier is: " + str(self.multi), "The Degree is: " +str(self.degree))
    def addEdge(self, edge):
        if(edge.start!=self):
            print("Can't add an Edge because start attribute does not match")
        else:
            self.edgeList.append(edge)
            edge1=Edge(edge.end, edge.start, edge.weight)
            edge.end.edgeList.append(edge1)
            self.degree=self.degree+1
            edge.end.degree=edge.end.degree+1
    def getNeighbors(self):
        for i in self.edgeList:
            print(i.end.name)

class Edge:
    def __init__(self, start, end, weight):
        self.start=start
        self.end=end
        self.weight=weight

class letterGrid:
    def __init__(self, letterArr, size=4):
        self.size=size
        self.letterArr=[["fill" for i in range(self.size)] for j in range(self.size)]
    #generate random Grid of Letter objects
    def genRandomGrid(self):
        #initialize 2d Array
        for i in range(self.size):
            for j in range(self.size):
                randLetter=random.choice(string.ascii_uppercase)
                self.letterArr[i][j]=Letter(randLetter, scrabbleDict[randLetter], [], 0)

        self.letterArr=np.array(self.letterArr)
        return self.letterArr
    def genGrid(self, letters):
        # generates a grid from a list of letters
        for i in range(self.size):
            for j in range(self.size):
                letters[i][j]=Letter(letters[i][j], scrabbleDict[letters[i][j]], [], 0)
        self.letterArr=letters
        return letters
    #register edges
    def connectGrid(self):
        for i in range(self.size):
            for j in range(self.size):
                print(i, j)
                if (i + 1 < self.size):
                    edge = Edge(self.letterArr[i][j], self.letterArr[i + 1][j],
                                self.letterArr[i][j].value + self.letterArr[i + 1][j].value)
                    self.letterArr[i][j].addEdge(edge)

                    print("connectDown")
                if (j + 1 < self.size):
                    edge = Edge(self.letterArr[i][j], self.letterArr[i][j + 1],
                                self.letterArr[i][j].value + self.letterArr[i][j + 1].value)
                    self.letterArr[i][j].addEdge(edge)
                    print("connectRight")
                if (j + 1 < self.size and i + 1 < self.size):
                    edge = Edge(self.letterArr[i][j], self.letterArr[i + 1][j + 1],
                                self.letterArr[i][j].value + self.letterArr[i + 1][j + 1].value)
                    self.letterArr[i][j].addEdge(edge)
                    print("connectRDiagonalDown")
                if (i + 1 < self.size and j - 1 >= 0):
                    edge = Edge(self.letterArr[i][j], self.letterArr[i + 1][j - 1],
                                self.letterArr[i][j].value + self.letterArr[i + 1][j - 1].value)
                    self.letterArr[i][j].addEdge(edge)
                    print("connnectLDiagonalDown")
                """
                if (i -1 >=0 and j +1 <self.size):
                    edge = Edge(self.letterArr[i][j], self.letterArr[i - 1][j + 1],
                                self.letterArr[i][j].value + self.letterArr[i - 1][j + 1].value)
                    self.letterArr[i][j].addEdge(edge)
                    print("connectRDiagonalUp")
                """
        return self

    def displayGrid(self):
        letters=(list(l.name for row in self.letterArr for l in row))
        letterMat=np.reshape(letters, (4,4))
        print(letterMat)
        return (letterMat)

class Path:
    def __init__(self, charArr):
        self.charArr=[]
