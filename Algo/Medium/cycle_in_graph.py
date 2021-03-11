"""
You're given an array representing an unweighted directed graph. Write a function that returns a boolean, whether or not the graph contains a cycle.

Input:
    edges = [
        [1, 3],
        [2, 3, 4],
        [],
        [0],
        [2, 5],
        []
    ]
Output:
    True

** will always be 1+ node
** run a DFS but will be O(n*m) cause we have to iterate thru all vertices then edges, not just edges
** the visited list will get rewritten every iteration (go deep as you can)
** DIRECTED
"""
import time


def cycleInGraph(edges):
    # Write your code here.
    for node in range(len(edges)):
        cycle = dfsEdges(node, edges)
        if cycle:
            return True
    return False


def dfsEdges(node, edges):
    queue = [node]
    visited = [node]
    cycle = False
    while queue:
        current = queue.pop(0)
        for outbound_edge in edges[current]:
            if outbound_edge == node:
                # print("caught loop", node, outbound_edge)
                cycle = True
                break
            else:
                if outbound_edge not in visited:
                    visited.append(outbound_edge)
                    queue.append(outbound_edge)

    return cycle


if __name__ == "__main__":
    edges = [
        [1, 3],
        [2, 3, 4],
        [],
        [0],
        [2, 5],
        []
    ]  # T
    edges3 = [
        [1, 2],
        [2],
        []
    ]  # F
    #     0
    #   /  \
    #  A    A
    #  1---> 2
    #
    edges2 = [
        [1, 2],
        [2],
        [1]
    ]  # T
    print(cycleInGraph(edges))
