# DFS algorithm for Tarjan's strongly connected components
# def: SCCs are self-contained cycles within a directed graph (as in doing a DFS)
#      where every vertex in a cycle can reach every other vertex in the same cycle.
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


def findSCCs():
    dfsSCCs(0, -1)
    #for i in range(g.num_nodes):
        #print("Run number:", i)
        #if not ids[i]:
            #dfsSCCs(i)
    return lowLink


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
    stack = GraphQueue("deque").buildQ()

    # Graph object
    g = graph2()
    sccCount = 0
    nid = 0
    lowLink = [ 0 ] * g.num_nodes
    ids = [ False ] * g.num_nodes
    onStack = [ False ] * g.num_nodes

    # LOGIC
    #findBridges()
    findSCCs()

    print("LL:", lowLink)
    print("IDS:", ids)
    print(onStack)
    print(sccCount)
