# Notes during video:
# augmenting paths
# residual edges
# flow augmentation
# SEVERAL methods can used to increase the efficiency of the above
# Alone, Fulkerson is DFS 
import sys
sys.path.append("/home/wendiw/Xenial_Backup/PythonPlay/graphs")
from Matrix.functions import *


class NetworkFlowSolverBase():
    def __init__(self):
        INF = MAX_VALUE /2
        n = s = t = int()
        visitedToken = 1
        visited = []
        solved = bool()
        maxFlow = int()
        #graph = [] # Edges/adjacency list?


def fulkerson():
    f = dfs(s, INF)
    while f != 0:
        visitedToken += 1
        maxFlow += f
        f = dfs(s, INF)


def dfs(node, flow):
    if node == t: return flow

    visited[node] = visitedToken

    edges = g.adjacent[node]
    for edge in edges:
        if edge.remaining_capacity() > 0 and visited[edge.eTo] != visitedToken:
            bottleNeck = dfs(edge.eTo, min(flow, edge.remaining_capacity()))
        # callback
            if bottleNeck > 0:
                edge.augment(bottleNeck)
                return bottleNeck

    return 0


def graph_lookie_loo(obj):
    for item in range(obj.num_nodes):
        for child in obj.adjacent[item]:
            if child.capacity != 0:
                print(f"Parent -- {item} connected to -- {child.id} at capacity: {child.capacity}")


def graph1():
    # this will require new method in graph class
    n = 11 # numberofnodes
    s = n - 2 # start-2 (itself and sink?)
    t = n - 1 # sink-1 (itself?)
    #
    g = Graph(n)
    # Edges from source/start source/dest/capacity
    g.add_net_edge(s, 0, 10)
    g.add_net_edge(s, 1, 5)
    g.add_net_edge(s, 2, 10)
    #
    # Middle edges
    g.add_net_edge(0, 3, 10)
    g.add_net_edge(1, 2, 10)
    g.add_net_edge(2, 5, 10)
    g.add_net_edge(3, 1, 10)
    g.add_net_edge(3, 6, 10)
    g.add_net_edge(4, 1, 10)
    g.add_net_edge(4, 3, 10)
    g.add_net_edge(5, 4, 10)
    g.add_net_edge(5, 8, 10)
    g.add_net_edge(6, 7, 10)
    g.add_net_edge(7, 4, 10)
    g.add_net_edge(7, 5, 10)
    #
    # Edges to sink
    g.add_net_edge(6, t, 15)
    g.add_net_edge(8, t, 10)
    #
    return g


if __name__ == "__main__":
    # Graph object
    g = graph1()
    #graph_lookie_loo(g)

