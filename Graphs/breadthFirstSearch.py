# Store functions that lend themselves to BFS algorithm here
from queue import Queue

# straight adjacency list = nodes with edges
graph = {
    0 : set([1,7,8]),
    1 : set([0,8]),
    2 : set([6,8]),
    3 : set([5]),
    4 : set([8,9]),
    5 : set([3,8]),
    6 : set([2,9]),
    7 : set([0]),
    8 : set([0,1,2,4,5]),
    9 : set([4,6])
}



def bfs(s,e):
    prev = solve(s)

    return reconstructPath(s, e, prev)


def nodes_count(graph):
    return len(graph)


def solve(s):
    q = Queue()
    q.put(s)

    nodes = nodes_count(graph)
    visited = [False for i in range(0,nodes)] # nodes visited
    visited[s] = True
    prev = [None for i in range(0,nodes)] 

    while not q.empty():
        node = q.get()
        neighbors = graph[node]
        for next in neighbors:
            if not visited[next]:
                q.put(next)
                visited[next] = True
                prev[next] = node
    print(prev)
    return prev


def reconstructPath(s, e, prev):
    path = []
    at = e
    while at != None:
        at = prev.pop()
        path.append(at)
    path.reverse()
    if path[0] == s: # if index 0 equals starting point
        return path
    return []



# logic
original_path = bfs(0,nodes-1)
print(original_path)
