# Input: undirected graph, 2D matrix AND number of colors
# can the graph nodes be colored with the unique num of colors and never be adjacent


class GraphColor:
    def __init__(self, nodes):
        self.V = nodes
        self. graph = [ [0] * self.V for x in range(self.V) ]


    def is_safe(self, v, color_array, color):
        for i in range(self.V): # 1--4
            # the == 1 is node check
            if (self.graph[v][i]) == 1 and (color_array[i] == color):
                print(f"...we failed inside is_safe on vector/i: {v,i}")
                return False
        return True # there's no color match, we return true

    def graph_color_util(self, m, color_array, v):
        if v == self.V: # counting v UP
            return True

        for color in range(1, m + 1): # for 1--4(3)
            print(f"...inside _util, color/vector: {color, v}")
            if self.is_safe(v, color_array, color):
                color_array[v] = color # 1st run, v0 set to 1
                print(f"....color array index {v} set to {color}")
                if self.graph_color_util(m, color_array, v + 1):
                    return True
                print(f"....so we reset vector for color: {v,color}")
                color_array[v] = 0 # backtracking

    def graph_coloring(self, m):
        color_array = [0] * self.V
        if self.graph_color_util(m, color_array, 0) == None:
            return "Not enough colors"

        for c in color_array:
            print(c)
        return "Solution found"



if __name__ == "__main__":
    # We want an array of colors, with no adjacent edges. [0, x, x, x]
    g = GraphColor(4)
    g.graph = [
        [ 0, 1, 1, 1 ],
        [ 1, 0, 1, 0 ],
        [ 1, 1, 0, 1 ],
        [ 1, 0, 1, 0 ]
        ]
    m = 3

    res = g.graph_coloring(m)
    print(res)
