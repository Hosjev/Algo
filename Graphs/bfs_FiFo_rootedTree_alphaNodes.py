# Testing out undirected rooted tree with DFS using deque (LIFO)
from Matrix.functions import *


def dfs_undirected(stack, g):
    visited = []
    stack.append(g.id)
    while stack:
        node = stack.pop()
        for child in g.graph[node]:
            if child not in visited:
                stack.append(child)
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
    #
    #       a
    #     /   \
    #   b      c
    #  /     /  \
    # e     d    f
    #       |
    #       g
    graph = {
        "a" : ["b", "c"],
        "b" : ["a", "e"],
        "c" : ["a", "d", "f"],
        "d" : ["c", "g"],
        "e" : ["b"],
        "f" : ["c"],
        "g" : ["d"]
    }
    
    # initialize Queue
    stack = GraphQueue("deque").buildQ()

    # build graph object
    g = Graph(7, start = "a")
    g.preserveKeys(graph)

    # LOGIC
    visited = dfs_undirected(stack, g)
    print(visited)

