# River sizes problem with expected naming conventions for Algo site

testC1 = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
testC2 = [[0]]
testC3 =  [[1]]
testC4 = [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]]
testC5 = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

def riverSizes(test):

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


if __name__ == "__main__":
    rivers = riverSizes(testC5)
    print(rivers)

    for row in testC5:
        print(str(row).replace("0", " "))
