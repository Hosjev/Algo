from Matrix.functions import *
import random



def topSort(g):
    # We ultimately return the order list
    # *variable "i" superfluous but dfs_top recursion needs it
    n = g.num_nodes
    visited = [False] * n
    order = [0] * n
    i = n - 1

    for node in range(n):
        print("processing node:", node)
        if visited[node] == False:
            i = dfs_top(i, node, visited, order, g)

    return order


def dfs_top(i, node, visited, order, g):
    # In this function we add to the ordered list in reverse, starting at the end.
    # Then we randomly pick "not" visited nodes when the recursions are (or not) exhausted.
    visited[node] = True

    edges = g.adjacent[node]
    for edge in edges:
        print("...inside edges for node:", node, edge.id)
        if visited[edge.id] == False:
            i = dfs_top(i, edge.id, visited, order, g)

    order[i] = node # Here, the 1st instance will be 1st node in "n" (0) at "i" (last idx)
    print(node, i, order)
    return i - 1



if __name__ == "__main__":
    # My graph
    # < L or up; > R or down
    # 0<-- 4 -->8
    #  \<  \>
    #   2   5
    #   >\ /<
    #     1  7
    #   </  </
    # 3    </
    #  <\ </
    #    6
    #

    g = Graph(9, reverse = False)
    g.add_edge(1, 5)
    g.add_edge(2, 0)
    g.add_edge(2, 1)
    g.add_edge(3, 1)
    g.add_edge(4, 0)
    g.add_edge(4, 5)
    g.add_edge(4, 8)
    g.add_edge(6, 3)
    g.add_edge(7, 6)

    # [7, 6, 4, 8, 3, 2, 1, 5, 0]
    print(topSort(g))

    g.add_in_out_edges()
    print(g.inEdges)
    print(g.outEdges)
