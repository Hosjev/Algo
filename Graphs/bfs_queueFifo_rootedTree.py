# DFS algorithm on undirected cyclic graph using Queue FIFO
from Matrix.functions import *


def solve(q, g, s):
    # initialize queue and visited
    q.put(g.id)
    visited = [g.id]
    previous = [None] * g.num_nodes

    while not q.empty():
        current = q.get()
        for child in g.adjacent[current]:
            if child.id not in visited:
                q.put(child.id)
                visited.append(child.id)
                previous[child.id] = current
    # 001223
    return previous


def bfs_undirected(q, g, s, e):
    prev = solve(q, g, s)
    return reconstructPath(s, e, prev)


def reconstructPath(s, e, prev):
    path = []
    for x in prev: 
        if x == None:
            continue
        path.append(x)
    if path[0] == s:
        return path
    return []

    

if __name__ == "__main__":
    # dict graph of matrix
    #      0
    #     / \
    #    1   2
    #   /   / \
    #  4   5   3
    #         /
    #        6

    graph = {
        0 : [1, 2],
        1 : [0, 4],
        2 : [0, 3, 5],
        3 : [2, 6],
        4 : [1],
        5 : [2],
        6 : [3]
    }

    # queue object
    q = GraphQueue("fifo").buildQ()
    
    # graph object
    g = Graph(7, start = 0)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    # LOGIC
    previous = bfs_undirected(q, g, g.id, g.adjacent[-1])

    print(previous)
