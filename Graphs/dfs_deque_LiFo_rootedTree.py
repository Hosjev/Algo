# Testing out undirected rooted tree with DFS using deque (LIFO)
from Matrix.functions import *


def dfs_undirected(stack, g):
    visited = []
    stack.append(g.id)
    while stack:
        node = stack.pop()
        for child in g.adjacent[node]:
            if child.id not in visited:
                stack.append(child.id)
        visited.append(node)
    return visited


def experiment(stack, g):
    processed = []
    #create list of branches
    #each time there's a split, create new branch
    stack.append(g.id)
    # start a new key each time there's a branch
    while stack:
        node = stack.pop()
        processed.append(node)
        for child in g.adjList[node]:
            if child not in processed:
                stack.append(child)
            processed.append(child)
    return processed


if __name__ == "__main__":
    graph = {
        0 : [1, 2],
        1 : [0, 4],
        2 : [0, 3, 5],
        3 : [2, 6],
        4 : [1],
        5 : [2],
        6 : [3]
    }
    
    # initialize Queue
    stack = GraphQueue("deque").buildQ()

    # build graph object
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    # LOGIC
    visited = dfs_undirected(stack, g)
    print(visited)

