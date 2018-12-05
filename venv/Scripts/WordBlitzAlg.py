from WordBlitz import *
import random

def score(path, grid):
    return 100

def RandWordSearch(grid):
    # prob better to search recursively
    wordFound = False
    word = grid.chooseRand().name #initialize word (starts as a letter)
    #print(word)
    pathList=[[]]
    while(wordFound==False):
        node = grid.chooseRand()
        nextLetter = node.randNeighbor()
        print(word+nextLetter.name)
        if((dawg.search_with_prefix(word+nextLetter.name))!=None):
            word=word+nextLetter.name
        #print(word)

        if(word+nextLetter.name in dawg):
            print("found one that is " + str(len(word+nextLetter.name)) + " letters long")
            wordFound=True

    return word
def GreedySearch(grid):
    return

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

#gridCase1=testCase1()
#print(RandWordSearch(gridCase1))

"""
with open('dawg.pkl', 'rb') as input:
    dawg = pickle.load(input)
"""
x=[]
x.append([1,4])
print(x)
x.append([1,3])
print(x)
print([1,4] in x)