from collections import deque

class BFS:

    def __init__(self, graph):
        self.graph = graph
        self.keys = list(self.graph.keys())

    def get_idx(self, char):
        return self.keys.index(char)

    def from_key(self, idx):
        return self.keys[idx]

    def shortest_path(self, start, end):
        previous = self._shortest_path(start)
        return self._reconstruct(start, end, previous)

    def _shortest_path(self, start):
        previous = [None] * len(self.graph)
        visited = [False] * len(self.graph)
        visited[self.get_idx(start)] = True
        q = deque()
        q.append(start)
        while q:
            parent = q.popleft()
            for child in self.graph[parent]:
                if not visited[self.get_idx(child)]:
                    q.append(child)
                    visited[self.get_idx(child)] = True
                    previous[self.get_idx(child)] = self.get_idx(parent)
        return previous

    def _reconstruct(self, s, e, p):
        s_idx, e_idx = self.get_idx(s), self.get_idx(e)
        path = [e_idx]
        c_idx = e_idx
        while True:
            path.append(p[c_idx])
            if p[c_idx] == s_idx: break
            c_idx = p[c_idx]
        return [self.from_key(x) for x in reversed(path)]


def main():
    g = {
        "a": ["b", "c", "d"],
        "b": ["a", "h"],
        "c": ["a", "d"],
        "d": ["a", "c"],
        "e": ["f", "g"],
        "f": ["g", "j"],
        "g": ["e", "f", "j", "h"],
        "h": ["b", "g", "i"],
        "i": ["h", "j"],
        "j": ["g", "i"]
    }
    print(BFS(g).shortest_path("a", "i"))


main()
