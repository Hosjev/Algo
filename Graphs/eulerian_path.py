# Eulerian path/trail is a path of edges that visits all the edges in a graph ONCE.
# Eulerian circuit is a eulerian path that connects back to the starting vertex/node.
# *not all graphs contain either a path or circuit, some contain either/or.
# *every circuit means we have a path
# *for a path, we need start and end nodes at:
#          out - in greater by 1 = 1(start) & in - out greater by 1 = 1(end)
# *for both path/circuit, every node with NON-ZERO degree (# of edges) needs to
# *this algorithm is about EDGES, not nodes as its focus
#  belong to a sinle strongly connected component
import copy
from Matrix.functions import *



def dfsSCCs(node, parent):
    # A recursion function that combines DFS with lowLink eval and will spawn children
    global sccCount
    global nid
    stack.append(node)
    onStack[node] = True
    nid += 1
    ids[node] = lowLink[node] = nid

    print(f"Working on NID for node: {nid, node}")

    for child in g.adjacent[node]:
        print(f"...working on child of node: {child.id, node}")
        if not ids[child.id]:
            print(f"...dfs spawned for child: {child.id}")
            dfsSCCs(child.id, node)
        print(f"...we've reached a callback on node/child: {node, child.id}")
        if onStack[child.id] and child.id != parent:
            lowLink[node] = min(lowLink[node], lowLink[child.id])
            print(f"...{node} LL value: {lowLink[node]}")

    # The STACK is what allows the algorithm to keep track of processed nodes. This prevents
    # processing nodes twice and looks for the start point, when it stops pulling from the stack.
    # Because this is deque (lifo), the nodes get removed in reverse order, working backward through
    # the connected cycle till we hit the originating node.
    if ids[node] == lowLink[node]:
        print(f"...inside if statement for node: {node}")
        while stack:
            item = stack.pop()
            onStack[item] = False
            lowLink[item] = ids[node] # Connect our nodes!
            if item == node:
                print(f"...item {item} broke while")
                break
        sccCount += 1


def findEulerianPath(g):
    # 1. find edge degrees (now graph object)
    # 2. determine if edge meet Eulerian reqs
    # 3. dfs thru edges
    # 4. return path if edge count pairs up

    # Sanity checks
    if sum(g.outEdges) < 1 or sum(g.inEdges) < 1: return "Null edges"

    if not graphHasEulerianPath: return None

    dfsEulerian(findStartNode())

    if len(ePath) == (sum(g.outEdges) + sum(g.inEdges))/2  + 1:
        return ePath
    return None


def findStartNode():
    # Return 1st start node you find that meets reqs.
    start = 0
    for i in range(g.num_nodes):
        if g.outEdges[i] - g.inEdges[i] == 1: return i
        if g.outEdges[i] > 0: start = i
    return start

    
def graphHasEulerianPath():
    start_nodes, end_nodes = 0, 0
    for i in range(g.num_nodes):
        if (g.outEdges[i] - g.inEdges[i] > 1) or \
           (g.inEdges[i] - g.outEdges[i] > 1):
            return False
        elif g.outEdges[i] - g.inEdges[i] == 1:
            start_nodes += 1
        elif g.inEdges[i] - g.outEdges[i] == 1:
            end_nodes += 1
    return (end_nodes == 0 and start_nodes == 0) or \
           (end_nodes == 1 and start_nodes == 1)


def dfsEulerian(current):
    # Depth first search that backtracks over previous nodes
    # while counting down the nodes edges in copy_outEdges.
    # Most DFS cares about nodes, this one cares about edges.
    # The ePath insert is the callback that adds to path as edges are exhausted.
    while copy_outEdges[current] != 0:
        index = copy_outEdges[current] - 1
        copy_outEdges[current] -= 1
        next_edge = g.adjacent[current][index].eTo
        dfsEulerian(next_edge)
    ePath.insert(0, current)
    

def graph1():
    g = Graph(7, reverse = False)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 2)
    g.add_edge(2, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 1)
    g.add_edge(3, 2)
    g.add_edge(3, 5)
    g.add_edge(4, 3)
    g.add_edge(4, 6)
    g.add_edge(5, 6)
    g.add_edge(6, 3)
    g.add_in_out_edges()
    return g


def graph2():
    # Small balanced directed graph to test functions
    g = Graph(5, reverse = False)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 1)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_in_out_edges()
    return g


if __name__ == "__main__":
    # Queue object and first node
    stack = GraphQueue("deque").buildQ()

    # Graph object
    g = graph1()

    # Algorithm specific/global variables
    copy_outEdges = copy.deepcopy(g.outEdges)
    ePath = []

    # LOGIC
    path = findEulerianPath(g)

    print(path)
