# BFS algorithm on undirected cyclic graph using Queue FIFO
from Matrix.functions import *



# the below algorithm will add visited nodes to the queue
def startBFS(q, g):
    q.put(g.id)
    visited = [g.id]
    return exploreGraph(q, g, visited)

def exploreGraph(q, g, visited):
    while not q.empty():
        current = q.get()
        for node in g.adjacent[current]:
            if node.id not in visited:
                q.put(node.id)
                visited.append(node.id)
    return visited


if __name__ == "__main__":
    # dict graph of matrix
    # 
    #     8
    #   /   \  
    # 3---4--0
    #   / | \
    #  9  |  1 
    #     2  \
    #   /     5
    #  6     /
    #       7
    # 
    graph = {
        0 : [4, 8],
        1 : [4, 5],
        2 : [4, 6],
        3 : [4, 8],
        4 : [0, 1, 2, 3, 9],
        5 : [1, 7],
        6 : [2],
        7 : [5],
        8 : [0, 3],
        9 : [4]
    }

    # graph object
    g = Graph(10)
    g.add_edge(0, 4)
    g.add_edge(0, 8)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 4)
    g.add_edge(2, 6)
    g.add_edge(3, 4)
    g.add_edge(3, 8)
    g.add_edge(4, 9)
    g.add_edge(5, 7)

    # queue object
    q = GraphQueue("fifo").buildQ()

    # LOGIC
    visited = startBFS(q, g)

    print(visited)
