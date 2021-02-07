# This Dijkstra rhythm should work for both acyclic and cyclic graphs.
# But no NEGATIVE numbers
# Lazy D == queue insertion (duplicate nodes w/diff weights)
# Eager D == queue decreaseValue (or Key) method for dups
from Matrix.functions import *
import random



def recursPath():
    #write recursive min return on sum paths to get shortest from 0-end
    # write it 1st w/o naming path then name node path
    pass


def lazy_dijkstra(g, q, s, e):
    visited = [False] * g.num_nodes
    prev = [None] * g.num_nodes
    infinity = float("inf")
    dist = [infinity] * g.num_nodes
    dist[s] = 0

    # Initialize then pop lowest value pairing off Priority Queue
    q.put( (0, s) )
    while not q.empty():
        minValue, index = q.get()
        visited[index] = True

        # Do nothing if our distance value is already lower
        if dist[index] < minValue: continue

        for edge in g.adjacent[index]:
            if visited[edge.eTo]: continue
            # weight relaxing
            newDist = dist[index] + edge.weight
            if newDist < dist[edge.eTo]:
                prev[edge.eTo] = index
                dist[edge.eTo] = newDist
                q.put( (newDist, edge.eTo) )
        if index == e:
            return (dist, prev)

    return infinity


class NodeOutOfRangeException(Exception):
    pass


def find_short_path(dist, prev, s, e):
    """Find the shortest distance between two nodes.

    Input:
        dist (list): list of best distances btw nodes
        prev (list): list of parent nodes (by indices)
        s (int): node number to start at
        e (int): node number to stop at

    Return:
        (list) Best path from start to end node.
    """
    if e > len(prev):
        raise NodeOutOfRangeException("Check your end node [" +
                str(e) + "] is in range.")
    if (s < 0 or s >= e):
        raise NodeOutOfRangeException("Check your start node [" +
                str(s) + "] is in range.")

    path = []
    if dist[e] == float("inf"): return path
    path.append(e)
    while e != s:
        val = prev[e]
        path.append(val)
        e = val
    path.reverse()
    return path
    

def updateQValue():
    # future function to find node and remove it then insert newer/lower value
    # thereby mocking Eager D algorithm
    pass


def longestPaths(g, topsort):
    # We start at topsort zero relaxing edges as we evaluate
    distance = [None] * g.num_nodes
    distance[0] = topsort[0]
    distance[0] *= -1

    for nodeIndex in topsort:
        for edge in g.adjacent[nodeIndex]:
            edge.weight *= -1
            newDist = distance[nodeIndex] + edge.weight
            if distance[edge.eTo] == None:
                distance[edge.eTo] = newDist
            else:
                distance[edge.eTo] = min(distance[edge.eTo], newDist)
    dist = [x * -1 for x in distance]
    return dist


def shortestPaths(g, topsort):
    # We start at topsort zero relaxing edges as we evaluate
    distance = [None] * g.num_nodes
    distance[0] = topsort[0]
    # 0, 1, 3, 2, 4 5
    for nodeIndex in topsort:
        print("Node:", nodeIndex)
        for edge in g.adjacent[nodeIndex]:
            newDist = distance[nodeIndex] + edge.weight
            print(f"...newDist for edge {edge.eTo}: {newDist}")
            if distance[edge.eTo] == None:
                distance[edge.eTo] = newDist
                print("we have None insert on weight:", distance[edge.eTo])
            else:
                distance[edge.eTo] = min(distance[edge.eTo], newDist)
                print("we have winning weight:", distance[edge.eTo])
    return distance


def graph1():
    g = Graph(5, reverse = False)
    g.add_edge(0, (4, 1))
    g.add_edge(0, (1, 2))
    g.add_edge(1, (1, 3))
    g.add_edge(2, (2, 1))
    g.add_edge(2, (5, 3))
    g.add_edge(3, (3, 4))
    return g


def graph2():
    g = Graph(6, reverse = False)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 3)
    g.add_edge(1, 4, 20)
    g.add_edge(2, 1, 3)
    g.add_edge(2, 4, 12)
    g.add_edge(3, 2, 3)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 6)
    g.add_edge(4, 5, 1)
    return g




if __name__ == "__main__":
    # run graphs
    g = graph2()

    # For shits and giggles
    topOrder = top_sort(g)

    # Queue
    q = GraphQueue("pq").buildQ()

    # Ideally, findShortPath would be called by lazyDijkstra to avoid different endpoints
    dist, prev = lazy_dijkstra(g, q, g.id, len(g.adjacent)-1)
    print("Dijkstra shortest:", dist, prev)
    print("...shortest path:", find_short_path(dist, prev, 0, 5))
