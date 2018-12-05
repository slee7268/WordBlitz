from WordBlitz import *
import random

def score(path, grid):
    return 100

def RandWordSearch(grid):
    #choose random start node
    i = random.randint(0, 3)
    j = random.randint(0, 3)
    print("The start letter is: " + grid.letterArr[i][j].name)
    word=Word(grid.letterArr[i][j].name, grid.letterArr[i][j].value)
    grid.genWordsStart(i, j, word, [])
    return grid.wordArr

def findHighestLetter(grid):
    #how should i handle ties
    max=0
    for letter in [y for x in grid.letterArr for y in x]:
        if letter.value>max:
            max=letter.value
            startNode=letter
    return startNode
def findHighestNeighbor(startNode):
    max=0
    for edge in startNode.edgeList:
        if(edge.end.value>max):
            max=edge.end.value
            neighbor=edge.end
    return edge.end
def GreedySearch(grid):
    #find highest letter, follow edges with largest weights
    words=[]
    startNode=findHighestLetter(grid)
    neighbor = findHighestNeighbor(startNode)
    return

def testCase1():
    #from actual screenshot of the game
    letterTest1 = [["A", "N", "A", "N"],
                   ["S", "I", "R", "E"],
                   ["R", "G", "U", "G"],
                   ["S", "U", "N", "D"]]
    grid = letterGrid([],4)
    grid1 = grid.genGrid(letterTest1)
    grid1 = grid.connectGrid()
    grid1.displayGrid()
    return grid1

def testCase2():
    letterTest2 = [["S", "O", "L", "C"],
                   ["O", "F", "A", "U"],
                   ["L", "C", "E", "T"],
                   ["W", "O", "V", "O"]]
    grid = letterGrid([],4)
    grid2 = grid.genGrid(letterTest2)
    grid2 = grid.connectGrid()
    grid2.displayGrid()
    return grid2

gridCase1=testCase1()
randWords=RandWordSearch(gridCase1)
randWords.sort(key=operator.attrgetter("value"), reverse=True)
print(randWords[0].string)

print(findHighestNeighbor(findHighestLetter(gridCase1)).name)

"""
with open('dawg.pkl', 'rb') as input:
    dawg = pickle.load(input)
"""

