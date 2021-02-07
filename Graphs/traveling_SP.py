# Traveling salesman problem. (brute force)
# Functions work on directed/weighted edges graph.
# The shortDistance function--evaluates each edge cost 
#  given its inbound edge weight from starting node to every other node.
#  It also works off the topsort list, which was created from the directed edges.
from Matrix.functions import *
import random



def recursPath():
    #write recursive min return on sum paths to get shortest from 0-end
    # write it 1st w/o naming path then name node path
    pass



def calcDistances(pCount, p1, p2, p3):
    # Another way to brute force this is to iterate over nodes per
    #   for node1 in 123: etc.
    #   then iterate over possible number of solutions per unique node (edges/nodes) -originating
    positionKey = "a"+cityNames[p1]+cityNames[p2]+cityNames[p3]
    # At the 1st sign of a match, we bail.
    if positionKey in distSums:
        return distSums
    else:
        distSums[positionKey] = g[0][p1] + g[p1][p2] + g[p2][p3] + g[p3][0]
    # Move positions to the right
    newPos1 = p3
    newPos2 = p1
    newPos3 = p2
    pCount += 1
    # We encountered a repeat, swap positions and continue.
    if pCount == maxRecursion:
        pCount = 0
        # Logic to determine swap position
        newPos2 = p2
        newPos3 = p1
    calcDistances(pCount, newPos1, newPos2, newPos3)


def processGraph(g):
    # First call pairings-- a- B, b-C, c-D, (d -a)
    # Second call pairings--a- D, d-B, b-C, (c -a)
    # etc.
    calcDistances(0, 1, 2, 3)


def calcD(pCount, p1, p2, p3, p4):
    # Bullshit function to brute force 5 node 2dMatrix
    posKey = "a"+str(p1)+str(p2)+str(p3)+str(p4)
    print("posKey string:", posKey)
    if posKey in distSums:
        return distSums
    else:
        distSums[posKey] = 0
    newPos1 = p4
    newPos2 = p1
    newPos3 = p2
    newPos4 = p3
    pCount += 1
    print("pCounter:", pCount)
    if pCount == 4:
        newPos3 = p3
        newPos4 = p2
    elif pCount == 8: # 1243 to 1423
        newPos2 = p3
        newPos3 = p2
    elif pCount == 12: # ?
        newPos2 = p3
        newPos3 = p2
    elif pCount == 16: # ?
        newPos2 = p3
        newPos3 = p2
    elif pCount == 20: # ?
        newPos2 = p3
        newPos3 = p2
    calcD(pCount, newPos1, newPos2, newPos3, newPos4)



def twoDMatrix():
    # 4 vertices and 12 edges
    #     a=0  b=1  c=2  d=3
    # a=0      4    1    9 
    # 
    # b=1 3         6    11
    # 
    # c=2 4    1         2
    #
    # d=3 6    5    -4
    #
    g = [ [] for x in range(4) ]
    for line in range(len(g)):
        g[line] = [0] * len(g)
    g[0][1] = 4
    calcD(pCount, newPos1, newPos2, newPos3, newPos4)



def twoDMatrix():
    # 4 vertices and 12 edges
    #     a=0  b=1  c=2  d=3
    # a=0      4    1    9 
    # 
    # b=1 3         6    11
    # 
    # c=2 4    1         2
    #
    # d=3 6    5    -4
    #
    g = [ [] for x in range(4) ]
    for line in range(len(g)):
        g[line] = [0] * len(g)
    g[0][1] = 4
    g[0][2] = 1
    g[0][3] = 9
    g[1][0] = 3
    g[1][2] = 6
    g[1][3] = 11
    g[2][0] = 4
    g[2][1] = 1
    g[2][3] = 2
    g[3][0] = 6
    g[3][1] = 5
    g[3][2] = -4

    return g


def twodMatrix():
    # 5 vertices and 20 edges
    #     a=0  b=1  c=2  d=3  e=4
    # a=0      4    1    9    5
    # 
    # b=1 3         6    11   -2
    # 
    # c=2 4    1         2    13
    #
    # d=3 6    5    -4        7
    #
    # e=4 9    3    1    4
    g = [ [] for x in range(5) ]
    for line in range(len(g)):
        g[line] = [0] * len(g)
    g[0][1] = 4
    g[0][2] = 1
    g[0][3] = 9
    g[0][4] = 5
    g[1][0] = 3
    g[1][2] = 6
    g[1][3] = 11
    g[1][4] = -2
    g[2][0] = 4
    g[2][1] = 1
    g[2][3] = 2
    g[2][4] = 13
    g[3][0] = 6
    g[3][1] = 5
    g[3][2] = -4
    g[3][4] = 7
    g[4][0] = 9
    g[4][1] = 3
    g[4][2] = 1
    g[4][3] = 4

    return g


def graph1():
    g = Graph(4, start = 0, reverse = False)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(0, 3, 9)
    g.add_edge(1, 0, 3)
    g.add_edge(1, 2, 6)
    g.add_edge(1, 3, 11)
    g.add_edge(2, 0, 4)
    g.add_edge(2, 1, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 0, 6)
    g.add_edge(3, 1, 5)
    g.add_edge(3, 2, -4)

    return g


if __name__ == "__main__":
    g = graph1()

    # Graph processing specific variables
    distSums = {}
    cityNames = {0: "a", 1: "b", 2: "c", 3: "d"}

    g = twoDMatrix()
    maxRecursion = len([num for x in g for num in x if num != 0]) / len(g)
    nodeSwap = 0
    processGraph(g)
    print(distSums)

    # Now we pick the shortest distance measured
    shortPath = min(distSums.values())
    for k,v in distSums.items():
        if v == shortPath: myPath = "Cities: "+str(k)+"a\n...distance:"+str(v)
    print(f"The shortest distance, visiting every city once and returning to home, is:\n {myPath}") 
