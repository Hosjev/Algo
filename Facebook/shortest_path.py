from queue import PriorityQueue


class ShortestPath:

    def __init__(self, graph):
        self.graph = graph
        self.prev = {}
        self.path_weight = {}
        self.remaining = PriorityQueue()
        for key in self.graph.nodes.keys():
            self.prev[key] = None
            self.path_weight[key] = float("inf")
            self.remaining.insert(
                PriorityQueueNode(key, self.path_weight[key]))

    def find_sp(self, start_node_key, end_node_key):
        if not start_node_key or not end_node_key:
            raise TypeError("Input nodes a must!")
        if start_node_key not in self.graph.nodes or \
           end_node_key not in self.graph.nodes:
            raise ValueError("Invalid start or end")
        self.path_weight[start_node_key] = 0
        self.remaining.decrease_key(start_node_key, 0)
        while self.remaining:
            min_node_key = self.remaining.extract_min().obj
            min_node = self.graph.nodes[min_node_key]
            for adj in min_node.adj_nodes.keys():
                new_weight = (min_node.adj_weights[adj] + \
                              self.path_weight[min_node_key])
                if self.path_weight[adj] > new_weight:
                    self.prev[adj] = min_node_key
                    self.path_weight[adj] = new_weight
                    self.remaining.decrease_key(adj, new_weight)
        result = []
        current_node_key = end_node_key
        while current_node_key:
            result.append(current_node_key)
            current_node_key = self.prev[current_node_key]
        return result[::-1]
