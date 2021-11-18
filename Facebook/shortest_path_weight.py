from queue import Queue


class Vertex:

    def __init__(self, value, weight = 0):
        self.value = value
        self.weight = weight


class Graph:

    def __init__(self):
        self.graph = dict()

    def add_node(self, val):
        if val not in self.graph:
            node = Vertex(val)
            self.graph[val] = node

    def add_edge(self, val, e, w):
        if val in self.graph:
            node = self.graph[val]
            node.adj.append(Vertex(e, w))
        else:
            self.add_node(val)
            node = self.graph[val]
            node.adj = [Vertex(e, w)]
    

class ShortestPath:

    def _eval_weight(self, resolution, new, node, edge):
        if edge.value not in resolution:
            resolution[edge.value] = (new, node.value)
        else: # eval
            if new < resolution[edge.value][0]:
                resolution[edge.value] = (new, node.value)

    def _reconstruct(self, resolution, end):
        path = [end]
        parent = resolution[end][1]
        while parent:
            path.append(parent)
            parent = resolution[parent][1]
        return path[::-1]

    def find(self, g, start, end):
        # TODO: EC no start/end
        # Resolution => to 0: weight, from
        resolution = {start: (0, None)}
        visited = [start]
        q = Queue() 
        q.put(g.graph[start])
        while not q.empty():
            node = q.get()
            for edge in node.adj:
                cur_w = resolution[node.value][0] + edge.weight
                self._eval_weight(resolution, cur_w, node, edge)
                if edge.value not in visited:
                    if edge.value in g.graph:
                        q.put(g.graph[edge.value])
                    visited.append(edge.value)
        path = self._reconstruct(resolution, end)
        return path


def main():
    g = Graph()
    g.add_edge("a", "b", 3)
    g.add_edge("a", "c", 6)
    g.add_edge("b", "c", 4)
    g.add_edge("b", "d", 4)
    g.add_edge("b", "e", 11)
    g.add_edge("c", "d", 8)
    g.add_edge("c", "g", 11)
    g.add_edge("d", "e", -4)
    g.add_edge("d", "f", 5)
    g.add_edge("d", "g", 2)
    g.add_edge("e", "h", 9)
    g.add_edge("f", "h", 1)
    g.add_edge("g", "h", 2)
    print(ShortestPath().find(g, "a", "h"))

main()
