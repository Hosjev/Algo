import copy
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
    g = Graph(graph)
    result = root_tree(g)
    print("We return to root:", result.id)
    
    # Run logic for longest path thru tree
    binary_pos = add_binary_positions(result)
    print("....longest path:", calc_tree_height(binary_pos))

    # Run logic for encoding
    print("....encoded tree:", encode(result))

    # Run logic for determining isomorphism
    graph2 = copy.deepcopy(graph)
    graph2[5].append(8)
    graph2[8] = [5]
    g2 = Graph(graph2)
    print("....isomorphic g1/g1?:", trees_isomorphic(g, g))
    print("....isomorphic g1/g2?:", trees_isomorphic(g, g2))
