# Traveling salesman problem.
# Functions work on directed/weighted edges graph.
# The shortDistance function--evaluates each edge cost 
#  given its inbound edge weight from starting node to every other node.
#  It also works off the topsort list, which was created from the directed edges.
import sys
sys.path.append("/home/wendiw/Xenial_Backup/PythonPlay/")
from Utilities.decorators import *
from graphs.Matrix.functions import *
import random



def calcDistances(pCount, p1, p2, p3):
    # Create a unique key
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


def tsp(g, memo, S):
    N = len(g)
    setup(g, memo, S, N)
    solve(g, memo, S, N)
    minCost = findMinCost(g, memo, S, N)
    trip = findOptimalTrip(g, memo, S, N)

    return (minCost, trip)


#@debug
def setup(g, memo, S, N):
    for i in range(N):
        if i == S: continue
        memo[i][(1 << S | 1 << i)] = g[S][i]


def solve(g, memo, S, N):
    #r = number of nodes in a partial trip
    for r in range(3, N+1):
        for subset in combinations(r,N): # returns list
            if testBit(S, subset): continue
            for nNext in range(N):
                if nNext == S or testBit(nNext, subset): continue
                state = subset ^ 1 << nNext
                minDist = float("inf")
                for e in range(N):
                    if e == S or e == nNext or testBit(e, subset): continue
                    print(f"...value for e and state: {e, state}")
                    newDistance = memo[e][state] + g[e][nNext]
                    print(f"...new dist: {newDistance}")
                    if newDistance < minDist: minDist = newDistance
                memo[nNext][subset] = minDist


def testBit(i, subset):
    # Compare 1 bits of i shifted left and integer of subset
    return (1 << i) & subset == 0


def combinations(r, n):
    # subsets is a list of integers representing binary values
    # r meant to be number of nodes in partial trip
    subsets = []

    def ssCombinations(sSet, at, r, n, subsets):
        if r == 0:
            subsets.append(sSet)
        else:
            for i in range(at, n):
                sSet |= 1 << i # is bit set?
                ssCombinations(sSet, i+1, r-1, n, subsets)
                sSet &= ~(1 << i)

    # we start with 0,0,3,4,emptylist
    ssCombinations(0, 0, r, n, subsets)
    return subsets


def findMinCost(g, memo, S, N):
    # All this does is iterate through the nodes and add
    # the previously computed State to the start node.
    END_STATE = (1 << N) -1
    minTripCost = float("inf")
    for e in range(N):
        if e == S: continue
        tripCost = memo[e][END_STATE] + g[e][S]
        if tripCost < minTripCost:
            minTripCost = tripCost
    return minTripCost


def findOptimalTrip(g, memo, S, N):
    lastIndex = S # last step is node 0
    state = (1 << N) - 1 # again, set memo[node] to 15
    trip = [None] * (N+1) # a list of empty vals of nodes plus start (to return)

    revNodes = [x for x in range(N)]
    revNodes.reverse()
    for i in revNodes: # iterate 3-0, last node first
        index = -1
        # iterate 0-3 to reset j to the most promising node
        # then store it to trip and continue
        for j in range(N):
            if j == S or testBit(j, state): continue
            if index == -1: index = j
            # prevD is simply the computed 3 trip plus node back to start
            prevDist = memo[index][state] + g[index][lastIndex]
            newDist = memo[j][state] + g[j][lastIndex]
            if newDist < prevDist: index = j

        trip[i] = index
        if index != -1: state = state ^ (1 << index)
        lastIndex = index

    trip[0] = trip[N] = S
    return trip


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
    g[3][1] = 7
    g[3][2] = -4

    return g


if __name__ == "__main__":
    # Graph processing specific variables
    distSums = {}
    cityNames = {0: "a", 1: "b", 2: "c", 3: "d"}
    g = twoDMatrix()
    # Fill up distSums variable
    maxRecursion = 3
    processGraph(g)
    print(distSums)

    # Now we pick the shortest distance measured
    shortPath = min(distSums.values())
    for k,v in distSums.items():
        if v == shortPath: myPath = "Cities: "+str(k)+"a\n...distance:"+str(v)
    print(f"The shortest distance, visiting every city once and returning to home, is:\n {myPath}") 


    # The above demonstrates a brute force method that processing every path.
    # The below uses dynamic programming.

    # Create the memo table for binary caching
    memo = [ [] for x in range(len(g))]
    for line in range(len(memo)):
        memo[line] = [None] * (1 << len(g))

    setup(g, memo, 0, len(g))
    print(memo)

    solve(g, memo, 0, len(g))
    print(memo)

    minCost = findMinCost(g, memo, 0, len(g))
    print(f"Minimum cost for travel: {minCost}")

    trip = findOptimalTrip(g, memo, 0, len(g))
    print(trip)
