"""Given a graph of N Nodes and E edges in form of {U, V, W} such that there exists an edge between U and V with weight W. You are given an integer K and source src and destination dst. The task is to find the cheapest cost path from given source to destination from K stops.

Input: N = 3, edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 1
Output: 200

Input: N = 3, edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 0
Output: 500

n0 = [0, 1, 100]
n1 = [1, 2, 100]
n2 = [0, 2, 500]

From city 0
To city 2
1 stop

My code: 1)capture flight constrictions s+k+e, 2)process hash, 3)sum flights and return min
NONE of the Geek code actually respects the stops restraint. You could include DP with a new adj list
and Then relax edges using bellman or dijkstra
"""
import uuid
import sys
sys.path.append("/home/wendiw/Xenial_Backup/PythonPlay/")
from Graphs.Matrix.functions import *
from queue import PriorityQueue


class FlightsDFS:
    def __init__(self, g, q):
        self.g = g
        self.q = q
        self.flights = []
        self.cost = float("inf")

    def cheapest(self):
        # Hello? No relaxing here. The flight path is stuck due to the constraint K
        # hash returned with cost as key
        f_hash = {}
        for arr in range(len(self.flights)):
            cost = 0
            for f in range(len(self.flights[arr])-1): # Run in pairs
                for e in self.g.adjacent[self.flights[arr][f]]:
                    if e.id == self.flights[arr][f+1]: cost += e.weight
            #self.cost = min(self.cost, cost) TO just return cost
            f_hash[cost] = self.flights[arr]

        return min((k,v) for k,v in f_hash.items())

    def dfs(self, node, index, path, e, k):
        # Set path index to DFS run
        path[index] = node

        # We reached destination
        if node == e:
            temp = []
            for x in path:
                temp.append(x) 
                if x == e: break
            if len(temp) == (1+k+1):
                self.flights.append(temp)
            return

        for edge in self.g.adjacent[node]:
            self.dfs(edge.eTo, index+1, path, e, k)

        if len(self.flights) > 0: return True
        return False

    def solve(self, s, e, k):
        path = [None] * self.g.num_nodes
        if self.dfs(s, 0, path, e, k):
            return self.cheapest()
        return f"No flight found with start city and {k} stop(s)."



def trips2(n):
    g = Graph(n, reverse = False)
    g.add_edge(4, 1, 1)
    g.add_edge(1, 2, 3)
    g.add_edge(0, 3, 3)
    g.add_edge(0, 4, 1)
    g.add_edge(3, 1, 1)
    g.add_edge(2, 4, 2)
    g.add_edge(0, 6, 4)
    g.add_edge(6, 5, 3)
    g.add_edge(6, 2, 1)
    g.add_edge(1, 4, 3)
    return g



if __name__ == "__main__":
    # Graph object
    g = trips2(7)

    q = PriorityQueue()
    d = FlightsDFS(g, q)
    print(d.solve(0, 4, 2))

