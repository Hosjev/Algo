from typing import List


class Solution:
    def _dfs(self, node, visited, graph, stack, topSort):
        visited[node] = True
        stack.append(node)
        for edge in graph[node]:
            if edge in stack: raise Exception # CYCLE!
            if not visited[edge]:
                self._dfs(edge, visited, graph, stack, topSort)
        # callback
        topSort.append(stack.pop())

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # EC
        if not bool(prerequisites): return [i for i in range(numCourses)]

        # Build graph w/directed edges
        # pair [a <-- b]
        graph = {i:set() for i in range(numCourses)}
        for pair in prerequisites:
            graph[pair[1]].add(pair[0])

        print(graph)
        visited = {i:False for i in graph.keys()}
        order = []
        stack = []
        for n in graph:
            if not visited[n]:
                try:
                    self._dfs(n, visited, graph, stack, order)
                except:
                    return []
        return order[::-1][:numCourses]


if __name__ == "__main__":
    p = [[1,0],[2,0],[3,1],[3,2]]
    p = [[0,1],[2,0],[1,3],[3,2]]
    print(Solution().findOrder(4, p))
    p = [[1,0]]
    print(Solution().findOrder(3, p))
