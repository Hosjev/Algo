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
Using BFS and some conditions, this works specifically for Stops.
Next version before quitting, get the flight legs

"""
import uuid
import sys
sys.path.append("/home/wendiw/Xenial_Backup/PythonPlay/")
from Graphs.Matrix.functions import *


class FlightsBFS:
    def __init__(self, g, q):
        self.g = g
        self.q = q

    def bfs(self, s, e, k, infinity):
        # B/c BFS works by ALL edges before depth, this works to process by layer of edge
        min_cost = infinity
        stops = k

        # We watch the Q so we don't pop from nothing
        #  and we watch stops to honor the restraint
        # On a larger scale, it would only make sense to
        #  track the flight legs. Inside an optimized hash table?
        # In this algorithm, perhaps the adjacency list would prepped w/legs?
        while not q.empty() and not stops < 0: # O(1)
            stops -= 1 # O(1)
            print(f"At stop: {stops}")
            q_size = self.q.qsize() # O(1)

            for x in range(q_size): # O(i)
                node, weight = q.get() # O(1)
                print(f"...popped node/weight: {node,weight}")
                if node == e: continue # Do NOT process destination edges O(1)
                for edge in self.g.adjacent[node]: # O(i)
                    # THE MAGIC. An accumulative weight gain by layer (BFS)
                    print(f"...processing edge: {edge.id}")
                    q.put((edge.id, (weight + edge.weight))) # O(1)
                    if edge.id == e and stops == -1: # O(1)
                        min_cost = min(min_cost, (weight + edge.weight)) # O(1)
                        print(f"...reset mincost: {min_cost}")

        return min_cost

    def solve(self, s, e, k):
        infinity = float("inf") # O(1)
        self.q.put((s, 0)) # O(1)
        result = self.bfs(s, e, k, infinity) # O(i)
        if result == infinity:
            return f"No flight found with start city {s} with {k} stop(s)."
        return result



def trips2(n):
    g = Graph(n, reverse = False)
    g.add_edge(4, 1, 1)
    g.add_edge(1, 2, 3)
    g.add_edge(0, 3, 2)
    #g.add_edge(0, 4, 1)
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

    q = GraphQueue("fifo").buildQ()
    b = FlightsBFS(g, q)
    print(b.solve(0, 4, 3))
    # Test a 4 stop (non-existent flight)
    # Test a 0 stop w/no direct (non-existent flight)
