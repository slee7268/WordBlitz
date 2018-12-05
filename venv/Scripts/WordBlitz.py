import string
import random
from array import *
import numpy as np
import copy
scrabbleDict={
    "E" : 1, "A" : 1, "I" : 1, "O" : 1, "S" : 1, "N" : 1, "R" : 1, "T" : 1, "L" : 1, "U" : 1,
    "D" : 2, "G" : 2, "B" : 3, "C" : 3, "M" : 3, "P" : 3, "F": 4 , "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5, "J": 8, "X": 8, "Q": 10, "Z":10
}
from lexpy.dawg import DAWG
import pickle

with open("words_alpha.txt") as f:
    words = [line.rstrip('\n') for line in f]
#370099 words in lexicon
words=[word for word in words if len(word)<=16 and len(word)>1]
#364215 words after reducing to words of length 1-16
words=[x.upper() for x in words] #make all words in uppercase
#following code used to create DAWG and then pickle it

"""
dawg = DAWG()
dawg.add_all(words)
dawg.reduce()
print(len(dawg))

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

save_object(dawg, 'dawg.pkl')
"""
#dawg has 16117 nodes
with open('dawg.pkl', 'rb') as input:
    dawg = pickle.load(input)

class Letter:
    def __init__(self, name, value, edgeList, degree, i, j, multi=1):
        self.name=name
        self.value=value
        self.edgeList=[]
        self.multi=multi
        self.degree=0
        #coordinates of letters
        self.i=i
        self.j=j
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
    def randNeighbor(self):
        randNum = random.randint(0, len(self.edgeList) - 1)
        randEdge = self.edgeList[randNum]
        return randEdge.end
class Edge:
    def __init__(self, start, end, weight):
        self.start=start
        self.end=end
        self.weight=weight

class Word:
    path=[]
    def __init__(self, string, value):
        #added path instance cause each word has a path
        self.string=string
        self.value=value
        #self.path=path

    def appendPath(self, index):
        self.path.append(index)
        return

class letterGrid:
    def __init__(self, wordArr, letterArr,  size=4):
        self.size=size
        self.wordArr=wordArr
        self.letterArr=[["fill" for i in range(self.size)] for j in range(self.size)]
    #generate random Grid of Letter objects
    def genRandomGrid(self):
        #initialize 2d Array
        for i in range(self.size):
            for j in range(self.size):
                randLetter=random.choice(string.ascii_uppercase)
                self.letterArr[i][j]=Letter(randLetter, scrabbleDict[randLetter], [], 0, i, j)

        self.letterArr=np.array(self.letterArr)
        return self.letterArr
    def genGrid(self, letters):
        # generates a grid from a list of letters
        for i in range(self.size):
            for j in range(self.size):
                letters[i][j]=Letter(letters[i][j], scrabbleDict[letters[i][j]], [], 0, i, j)
        self.letterArr=letters
        return letters
    #register edges
    def connectGrid(self):
        for i in range(self.size):
            for j in range(self.size):
                #print(i, j)
                if (i + 1 < self.size):
                    edge = Edge(self.letterArr[i][j], self.letterArr[i + 1][j],
                                self.letterArr[i][j].value + self.letterArr[i + 1][j].value)
                    self.letterArr[i][j].addEdge(edge)
                    #print("connectDown")
                if (j + 1 < self.size):
                    edge = Edge(self.letterArr[i][j], self.letterArr[i][j + 1],
                                self.letterArr[i][j].value + self.letterArr[i][j + 1].value)
                    self.letterArr[i][j].addEdge(edge)
                    #print("connectRight")
                if (j + 1 < self.size and i + 1 < self.size):
                    edge = Edge(self.letterArr[i][j], self.letterArr[i + 1][j + 1],
                                self.letterArr[i][j].value + self.letterArr[i + 1][j + 1].value)
                    self.letterArr[i][j].addEdge(edge)
                    #print("connectRDiagonalDown")
                if (i + 1 < self.size and j - 1 >= 0):
                    edge = Edge(self.letterArr[i][j], self.letterArr[i + 1][j - 1],
                                self.letterArr[i][j].value + self.letterArr[i + 1][j - 1].value)
                    self.letterArr[i][j].addEdge(edge)
                    #print("connnectLDiagonalDown")
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
    def listLetters(self):
        #return letterArray as list of letters
        a=[y for x in self.letterArr for y in x]
        a=[i.name for i in a]
        return a
    def chooseRand(self):
        # start at random letter
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        # random start node
        return self.letterArr[i][j]

    def genWordsStart(self, i, j, word, wordArr):
        #generate all valid words that start at index (i, j)
        #print(word.string)
        #print(np.matrix(visited))
        print(word.path)
        if word.string in dawg:
            self.wordArr.append(word)
            print("word found")
        for edge in self.letterArr[i][j].edgeList:
            next=edge.end.name
            #print(word.path)
            print(word.string + next)
            if((dawg.search_with_prefix(word.string+next))!=None and [edge.end.i, edge.end.j] not in word.path):
                #print(word.path)
                #newVisited=visited
                #newVisited[edge.end.i][edge.end.j]=True
                newPath=copy.deepcopy(word.path)
                print(word.path)
                newWord=Word(word.string+next, word.value+edge.end.value)
                newWord.path=newPath
                newWord.appendPath([edge.end.i, edge.end.j])
                print(newWord.path)
                self.genWordsStart(edge.end.i, edge.end.j, newWord, self.wordArr)
                #print(word+next)
        return
    def genAllWords(self):

        for i in range(self.size):
            for j in range(self.size):
                print("new letter Start")
                print(self.letterArr[i][j].name)
                word=Word(self.letterArr[i][j].name, self.letterArr[i][j].value)
                word.appendPath([i, j])
                #rootLetter= Word(self.letterArr[i][j].name, self.letterArr[i][j].value)
                #visited = [[False for i in range(self.size)] for j in range(self.size)]
                #visited[i][j] = True
                self.genWordsStart(i, j, word, self.wordArr)
        return self.wordArr


"""
letterTest2 = [["A", "B", "H", "D"],
                   ["C", "F", "G", "U"],
                   ["L", "Z", "E", "T"],
                   ["W", "O", "V", "N"]]

letterTest2 = [["S", "O", "L", "C"],
                   ["O", "F", "A", "U"],
                   ["L", "C", "E", "T"],
                   ["W", "O", "V", "O"]]
"""
letterTest2 = [["A", "N", "A", "N"],
                   ["S", "I", "R", "E"],
                   ["R", "G", "U", "G"],
                   ["S", "U", "N", "D"]]
grid = letterGrid([], 4)
print(grid.wordArr)

grid2 = grid.genGrid(letterTest2)
grid2 = grid.connectGrid()
grid2.displayGrid()
words=grid.genAllWords()


#for i in range(len(words)):
    #print(words[i].string)
    #print(words[i].value)

print(dawg.search_with_prefix("ACLO"))
print(len(words))

#how should I deal with non unique words
#should I just take the word itself and calculate all possible ways of making the word and then computing a score
#should I put the brute force result into a dawg so that future algorithms only search for words in the possible words?



