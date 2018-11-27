from WordBlitz import *
import random

with open("words_alpha.txt") as f:
    words = [line.rstrip('\n') for line in f]
#370099 words in lexicon

words=[word for word in words if len(word)<=16 and len(word)>1]
#364215 words after reducing to words of length 1-16
print(words[0:10])

def score(path, grid):
    return 100

def BruteForce(grid):
    return 1000

def RandWordSearch(grid):
    #start at random letter
    i=random.randint(0,3)
    j=random.randint(0,3)
    #random Letter object
    randLetter=grid.letterArr[i][j]
    wordFound=False
    while(wordFound==False):
        randNum=random.randint(0, len(randLetter.edgeList)-1)
        #randomEdge
        randEdge=randLetter.edgeList[randNum]

    return 1

def testCase1():
    #from actual screenshot of the game
    letterTest1 = [["A", "N", "A", "N"],
                   ["S", "I", "R", "E"],
                   ["R", "G", "U", "G"],
                   ["S", "U", "N", "D"]]
    grid = letterGrid(4)
    grid1 = grid.genGrid(letterTest1)
    grid1 = grid.connectGrid()
    grid1.displayGrid()
    return grid1

def testCase2():
    letterTest2 = [["S", "O", "L", "C"],
                   ["O", "F", "A", "U"],
                   ["L", "C", "E", "T"],
                   ["W", "O", "V", "O"]]
    grid = letterGrid(4)
    grid2 = grid.genGrid(letterTest2)
    grid2 = grid.connectGrid()
    grid2.displayGrid()
    return grid2

gridCase1=testCase1()
#RandWordSearch(gridCase1)

#testCase2()
