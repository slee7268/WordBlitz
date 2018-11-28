from WordBlitz import *
import random
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
with open('dawg.pkl', 'rb') as input:
    dawg = pickle.load(input)

#dawg has 16117 nodes

def score(path, grid):
    return 100

def BruteForce(grid):
    return 1000

def RandWordSearch(grid):
    #start at random letter
    i=random.randint(0,3)
    j=random.randint(0,3)
    #random start node
    wordFound = False
    word = grid.letterArr[i][j].name #initialize word (starts as a letter)
    #print(word)
    while(wordFound==False):
        node = grid.letterArr[i][j]
        randNum = random.randint(0, len(node.edgeList) - 1)
        randEdge = node.edgeList[randNum]
        nextLetter = randEdge.end
        print(word+nextLetter.name)
        if((dawg.search_with_prefix(word+nextLetter.name))!=None):
            word=word+nextLetter.name
        #print(word)
        if(word+nextLetter.name in dawg):
            print("found one")
            wordFound=True

    return word


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
print(RandWordSearch(gridCase1))

#testCase2()


