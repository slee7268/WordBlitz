from WordBlitz import *

def score(path, grid):
    return 100

def BruteForce(grid):
    return 1000

def testCase1():
    #from actual screenshot of the game
    return 1


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