# DFS algorithm on undirected cyclic graph using Queue FIFO(?)
from Matrix.functions import *


# dive as deep into edges until no more, then reverse
def dfsBridges(current, parent, bridges):
    # A recursion function that combines DFS with lowLink eval and will spawn children
    # This works because we compare IDS with lowest values of ALL edges. So when 8 evals
    # its edges, 5 completes a cycle and gets a low value of 5 as its nearest low node/ID

    visited[current] = True
    global nid
    nid = nid + 1
    lowLink[current] = ids[current] = nid
    print(f"Working on NID for current/parent: {nid, current, parent}")

    for child in g.adjacent[current]:
        if child.id == parent: continue # if we start backtracking, do NOTHING
        if not visited[child.id]:
            dfsBridges(child.id, current, bridges)
            lowLink[current] = min(lowLink[child.id], lowLink[current])
            if ids[current] < lowLink[child.id]:
                bridges.append( (current, child.id) )
        else:
            lowLink[current] = min(lowLink[current], ids[child.id])


def dfsArticulationPoints(root, current, parent):
    # A recursion function that combines DFS with lowLink eval and will spawn children
    global outEdgeCount
    if parent == root: outEdgeCount += 1
    visited[current] = True
    global aid
    aid = aid + 1
    lowLink[current] = ids[current] = aid
    print(f"Working on NID for root/current: {nid, root, current}")

    for child in g.adjacent[current]:
        if child.id == parent: continue # if we start backtracking, do NOTHING
        if not visited[child.id]:
            dfsArticulationPoints(root, child.id, current)
            lowLink[current] = min(lowLink[child.id], lowLink[current])
            if ids[current] < lowLink[child.id]: # detects via bridge
                artPoints[current] = True
            if ids[current] == lowLink[child.id]: # detects via cycle
                artPoints[current] = True
        else:
            lowLink[current] = min(lowLink[current], ids[child.id])


def findBridges():
    bridges = []
    #for i in range(g.num_nodes):
        #print("Run number:", i)
        #if not visited[i]:
            #dfs(i, -1, bridges)
    dfsBridges(0, -1, bridges)
    return bridges


def findArticulationPoints():
    for i in range(g.num_nodes):
        print("Run number:", i)
        if not visited[i]:
            outEdgeCount = 0
            dfsArticulationPoints(i, i, -1)
            artPoints[i] = outEdgeCount > 1
    return artPoints


def graph1():
    # graph object
    g = Graph(10)
    g.add_edge(0, 1)
    g.add_edge(0, 7)
    g.add_edge(0, 8)
    g.add_edge(1, 8)
    g.add_edge(2, 6)
    g.add_edge(2, 8)
    g.add_edge(3, 5)
    g.add_edge(4, 8)
    g.add_edge(4, 9)
    g.add_edge(5, 8)
    g.add_edge(6, 9)
    return g


def graph2():
    # graph object
    g = Graph(9)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(5, 8)
    return g



if __name__ == "__main__":
    # Queue object and first node
    q = GraphQueue("lifo").buildQ()

    # Graph object
    g = graph2()
    nid = 0
    aid = 0
    outEdgeCount = 0
    lowLink = [ 0 ] * g.num_nodes
    ids = [ 0 ] * g.num_nodes
    visited = [ False ] * g.num_nodes
    artPoints = [ False ] * g.num_nodes

    # LOGIC
    #findBridges()
    findArticulationPoints()
