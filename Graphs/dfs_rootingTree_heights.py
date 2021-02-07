""" Does this address log(N) rooting tree algo? """

from Matrix.functions import *



if __name__ == "__main__":
    # Rooted outtree
    #    0
    #    /\
    #   2  1
    #  /   /\
    # 4   5  3
    #       / 
    #      6
    #     /  
    #    7 
    graph = {
        0 : [1, 2],
        1 : [0, 3, 5],
        2 : [0, 4],
        3 : [1, 6],
        4 : [2],
        5 : [1],
        6 : [3, 7],
        7 : [6]
    }
    
    # LOGIC
    g = Graph(8)
    #g = Graph(8)
    #g.add_edge(0, 1)
    #g.add_edge(0, 2)
    #g.add_edge(1, 3)
    #g.add_edge(1, 5)
    #g.add_edge(2, 4)
    #g.add_edge(3, 6)
    #g.add_edge(6, 7)
    g.preserveKeys(graph)
    g.setUndirectedList()

    result = root_tree(g)
    print("We return to root:", result.id)
    
    longestPath = addBinaryPositions(result)
    print("....longest path:", calcTreeH(longestPath))
