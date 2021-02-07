# Bellman-Ford algorithm for Single Source Shortest Path from start-to-all-nodes with negative cycle detection.

from Matrix.functions import *


def bellmanFord(g):
    infinity = float("inf")
    neg_infinity = float("-inf")
    dist = [ infinity ] * g.num_nodes
    dist[g.id] = g.id

    # First set of vertices relaxation
    for iteration in range(g.num_nodes):
        for node in range(g.num_nodes):
            for edge in g.adjacent[node]:
                newDist = dist[node] + edge.weight
                if newDist < dist[edge.eTo]:
                    dist[edge.eTo] = newDist
        print(f"...iteration {iteration} - {dist}")

    # Second set of vertices relaxation
    for iteration in range(g.num_nodes):
        for node in range(g.num_nodes):
            for edge in g.adjacent[node]:
                newDist = dist[node] + edge.weight
                if newDist < dist[edge.eTo]:
                    dist[edge.eTo] = neg_infinity
        print(f"...iteration {iteration} - {dist}")

    return dist


def graph2():
    g = Graph(4, start = 0, reverse = False)
    # a = 0, b = 1, c = 2, d = 3
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(0, 3, 9)
    g.add_edge(1, 0, 3)
    g.add_edge(1, 2, 6)
    g.add_edge(1, 3, 11)
    g.add_edge(2, 0, 4)
    g.add_edge(2, 1, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 0, 6)
    g.add_edge(3, 1, 5)
    g.add_edge(3, 2, -4)

    return g


if __name__ == "__main__":
    #     6   7   8
    # 
    # 0   1   5   9
    #     
    #
    # 3   2   4
    

    # queue object
    q = GraphQueue("fifo").buildQ()
    
    # graph object
    g = graph2()

    # LOGIC
    print("Bellman-Ford - finding shortest path from start" \
           " to every other node and identifying negative cycles.")
    dist = bellmanFord(g)

    for x in range(g.num_nodes):
        print(f"The cost to get from node {g.id} to {x} is: {dist[x]}")
