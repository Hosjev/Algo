class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
  
  
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices # Set number of rows/cols
        self.graph = [None] * self.V # Set array of empty elements
        # .graph stores OBJECTS at each index.
        # .vertex = first (or last) then NESTED objects in .next(.next).vertex
    # Function to add an edge in an undirected graph, both out and inbound.
    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        # Adding the source node to the destination as 
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
    # Recursive method to print the graph 
    def print_graph(self): 
        def print_next(objN):
            print(f" vertex: {objN.vertex} ", end="")
            if objN.next != None:
                print_next(objN.next)
            return
        for i in range(self.V):
            print(f"\nIn Row {i}:")
            print_next(self.graph[i])
        print("\n")

  
  
# Driver program to the above graph class 
if __name__ == "__main__": 
    #       0 1 2 3 4
    #      ----------
    # Y  0|   1     1
    #    1| 1   1 1 1
    # a  2|   1   1
    # x  3|   1 1   1
    # i  4| 1 1   1
    # s   
    #       X axis
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4)

    graph.print_graph()
