# River sizes problem
import copy



def river_sizes(array):
    # Along the lines of the Algo suggestion
    # 1. get rid of 0s
    # 2. copy 2d array to stack
    # 3. starting at 0-0
    #    a. inside recur
    #    b. go left, right, down (and from each do the same)
    #    c. accumulate 1s till hitting dead end
    #    d. all 3 directions failing equals stop
    #    e. marking visited positions as you go
    # this could be recur outside for loop
    # it could be while with boundaries
    # it could be done using BFS and a visited tag
    visited = [ [False for col in row] for row in array ]
    for row in array:
        for col in row:
            if not visited[row][col]:
                explore_segments(row, col, array, rivers)


def explore_segments(r, c, array, rivers):
    if array[r][c] == 1:
        rivers.append(position)
        #for edge in positions:
        for edge in get_positions():
            if (edge in visited) and (not visited[edge]):
                explore_segments(edge)


def get_positions():
    #return a list of available positions, evaluating edges of matrix
    pass


def riverSizes(test):
    # The algo submission

    def pullRiverParts(riverRows):
        # Build tuples of positions
        parts = []
        for row in range(len(riverRows)):
            for col in range(len(riverRows[row])):
                if riverRows[row][col] == 1:
                    parts.append((row, col))
        return parts

    def dfs(index, segment):
        # each new edge we find gets explored to utmost
        if segment in stack:
            rivers[index] += 1
            stack.remove(segment)
            for edge in positions:
                newPos = tuple(sum(i) for i in zip(segment, edge))
                #if -1 in newPos: continue
                #if (newPos[0] or newPos[1]) >= len(riverRows): continue
                dfs(index, newPos)

    def compileRiver():
        while len(stack) != 0:
            #print(f"We begin: {stack[0]}")
            rivers.append(0)
            dfs(rivers.index(rivers[-1]), stack[0])

    # 1. pos
    positions = [
        (1, 0), # down
        (-1, 0), # up
        (0, 1), # right
        (0, -1) # left
    ]
    # 2. empty list
    rivers = []
    # 3. build stack
    stack = pullRiverParts(test)
    if len(stack) == 0: return []
    # 4. compile and return
    compileRiver()
    # 5. return
    return rivers


def twoDRiver():
    # A five by five matrix
    riverRows = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
      ]

    return riverRows



if __name__ == "__main__":
    # Global vars
    riverRows = twoDRiver()
    print(riverSizes(riverRows))

    for row in riverRows:
        print(str(row).replace("0", " "))
