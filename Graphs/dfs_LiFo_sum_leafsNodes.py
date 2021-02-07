# Testing out undirected rooted tree with DFS using deque (LIFO)
from Matrix.functions import *


def dfs_undirected(stack, start, adjacencyList):
    visited = []
    leaves = []
    stack.append(start)
    while stack:
        node = stack.pop()
        for neighbor in adjacencyList[node]:
            if neighbor not in visited:
                stack.append(neighbor)
        if node not in visited:
            visited.append(node)
        # logic for leaves
        if len(adjacencyList[node]) == 1:
            leaves.append(node)
    
    return (visited, leaves)


def sum_leaves(graph, leaves):
    # sum the weight of the end nodes
    l_sum = int()
    for x in leaves:
       l_sum += graph[x][0]
    return l_sum


if __name__ == "__main__":
    # Rooted intree
    graph = {
        0 : (3, [1, 2]),
        1 : (-1, [0, 3, 5, 6]),
        2 : (4, [0, 4]),
        3 : (-4, [1]),
        4 : (7, [2, 7]),
        5 : (-1, [1]),
        6 : (10, [1]),
        7 : (12, [4])
    }
    # target: [[1, 7, 8], [0, 8], [6, 8], ...
    edges = [(node, edge) for node, vals in graph.items() for edge in vals[1]]
    adjacencyList = [[] for x in range(len(graph))]
    for edge in edges:
        adjacencyList[edge[0]].append(edge[1])
    
    # initialize Queue
    stack = GraphQueue("deque").buildQ()

    # set my start node
    start = 0

    # LOGIC
    visited, l_nodes = dfs_undirected(stack, start, adjacencyList)
    leafs = sum_leaves(graph, l_nodes)
    print(visited, leafs)

