# Functions work on directed/weighted edges graph.
# The shortDistance function--evaluates each edge cost 
#  given its outbound edge weight from starting node to every other node.
#  It also works off the topsort list, which was created from the directed edges.
from Matrix.functions import *
import random



def recursPath():
    #write recursive min return on sum paths to get shortest from 0-end
    # write it 1st w/o naming path then name node path
    pass


def longDistance(g, topsort):
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


def shortDistance(g, topsort):
    # We start at topsort zero relaxing edges as we evaluate
    #   newDist = distance[nodeIndex] + edge.weight
    # The above line is the magic. We calc the previous node plus our outbound cost.
    distance = [None] * g.num_nodes
    distance[0] = topsort[0]

    for nodeIndex in topsort:
        for edge in g.adjacent[nodeIndex]:
            newDist = distance[nodeIndex] + edge.weight
            if distance[edge.eTo] == None:
                distance[edge.eTo] = newDist
            else:
                distance[edge.eTo] = min(distance[edge.eTo], newDist)
    return distance




if __name__ == "__main__":
    # My graph
    # < L or up; > R or down
    #
    #   1----->4
    #   ^     ^  \
    #  /  \  /    >
    # 0   >3-->5-->7
    #  \ /  \    /^
    #  >2---->>6/
    # node : [ (outbound edge weight, node),... ]
    graph = {
        0 : [ (10, 1), (3, 2) ],
        1 : [ (2, 3), (5, 4) ],
        2 : [ (1, 3), (6, 6) ],
        3 : [ (4, 4), (1, 5), (12, 6) ],
        4 : [ (11, 7) ],
        5 : [ (-4, 7) ],
        6 : [ (3, 7) ],
        7 : []
    }

    g = Graph(8, start = 0, reverse = False)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 3, 1)
    g.add_edge(2, 6, 6)
    g.add_edge(3, 4, 4)
    g.add_edge(3, 5, 1)
    g.add_edge(3, 6, 1)
    g.add_edge(4, 7, 1)
    g.add_edge(5, 7, -4)
    g.add_edge(6, 7, 3)


    topOrder = topSort(g)
    short = shortDistance(g, topOrder)
    print("Topological order:", topOrder)
    print("Shortest distances:", short)
    print("Longest distances:", longDistance(g, topOrder))
