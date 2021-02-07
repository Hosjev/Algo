# DFS algorithm on undirected cyclic graph using Queue FIFO
from Matrix.functions import *


def solve(q, g, s):
    # initialize queue and visited
    q.put(g.id)
    visited = [g.id]
    previous = [None] * g.num_nodes

    while not q.empty():
        current = q.get()
        for child in g.adjacent[current]:
            if child.id not in visited:
                q.put(child.id)
                visited.append(child.id)
                previous[child.id] = current
    # 001223
    return previous


def bfs_undirected(q, g, s, e):
    prev = solve(q, g, s)
    return reconstructPath(s, e, prev)




if __name__ == "__main__":
    # dict graph of matrix
    #      0
    #     / \
    #    1   2
    #   /   / \
    #  4   5   3
    #
    # simple dict style graph
    graph = {
        0 : [1, 2],
        1 : [0, 4],
        2 : [0, 3, 5],
        3 : [2, 6],
        4 : [1],
        5 : [2],
    
    # Graph as 2D matrix. Also, represents input for Floyd-Warshall algorithm.
    #
    #         a2
    #       0  1  2  3  4  5  6  7  8
    # a1 0     5
    # a1 1                 11
    # a1 2           15 -1 12
    # a1 3              10
    # a1 4                 20       7
    # a1 5                    -3 14
    # a1 6         
    # a1 7                    -21
    # a1 8         
    # 
    adj_array = [ [] for x in range(9) ]
    for col in range(len(adj_array)):
        adj_array[col] = [0] * len(adj_array)

    # Now we populate array
    adj_array[0][1] = 5
    adj_array[1][5] = 11
    adj_array[2][3] = 15
    adj_array[2][4] = -1
    adj_array[2][5] = 12
    adj_array[3][4] = 10
    adj_array[4][5] = 20
    adj_array[4][8] = 7
    adj_array[5][6] = -3
    adj_array[5][7] = 14
    adj_array[7][6] = -21
    

    # queue object
    q = GraphQueue("fifo").buildQ()
    
    # graph object
    g = Graph(7, start = 0)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    # LOGIC
    previous = bfs_undirected(q, g, g.id, g.adjacent[-1])

    print(previous)
