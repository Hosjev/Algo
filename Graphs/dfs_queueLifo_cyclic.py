# DFS algorithm on undirected cyclic graph using Queue FIFO(?)
from Matrix.functions import *



# dive as deep into edges until no more, then reverse
def dfs(q, g):
    visited = []
    q.put(g.id)

    while not q.empty():
        current = q.get()
        for node in g.adjacent[current]:
            if node.id not in visited:
                q.put(node.id)
        if current not in visited:
            visited.append(current)

    return visited


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
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    return g



if __name__ == "__main__":
    # queue object and first node
    q = GraphQueue("lifo").buildQ()

    # graph object
    g = graph1()
    g2 = graph2()

    # LOGIC
    visited = dfs(q, g)
    visited2 = dfs(q, g2)

    print(visited2)
