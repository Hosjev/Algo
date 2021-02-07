# Testing out undirected rooted tree with DFS using deque (LIFO)
from Matrix.functions import *


def dfs_undirected(stack, g):
    visited = []
    stack.append(g.id)
    while stack:
        node = stack.pop()
        for child in g.adjList[node]:
            if child not in visited:
                stack.append(child)
        visited.append(node)
    return visited




if __name__ == "__main__":
    #    7
    #   /  \
    #  6    1
    #  \ 
    #   2    5
    #  / \  /\    
    # 0    3  4
    #
    #
    graph = {
        0 : [2],
        1 : [7],
        2 : [0, 3, 6],
        3 : [2, 5],
        4 : [5],
        5 : [3, 4],
        6 : [2, 7],
        7 : [1, 6]
    }
    
    #    0       2
    #     \    / |\
    #      3--/  | 1
    #       \    |
    #   4    8    5
    #    \  / \
    #     7    6
    graph2 = {
        0 : [3],
        1 : [2],
        2 : [1, 3, 5],
        3 : [0, 2, 8],
        4 : [7],
        5 : [2],
        6 : [8],
        7 : [4, 8],
        8 : [3, 6, 7]
    }
    
    # initialize Queue
    stack = GraphQueue("deque").buildQ()

    # build graph object
    g = Graph(8)
    g.preserveKeys(graph)
    g.setUndirectedList()

    # LOGIC
    visited = dfs_undirected(stack, g)
    print(visited)

    print(find_center(g))
    g2 = Graph(9)
    g2.preserveKeys(graph2)
    g2.setUndirectedList()
    print(find_center(g2))
