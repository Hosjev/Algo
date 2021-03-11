"""
Given an array of non-empty positive ints representing the amount of time specific queries take to execute. Only query can be executed at a time but in any order.
A query's WAITING TIME is the amt of time it must wait before execution starts. IF a query is executed 2nd, its WT is the duration of 1st. IF 3rd, its WT is the sum of 1st and 2nd.
Write function that returns min WT of all query's WT.
For ex queries: [1, 4, 5] executed in order [5, 1, 4] -- (0) + (5) + (5 + 1) = 11WT


Input:
    q = [3, 1, 2, 2, 6]
Output:
    17

**this one makes no sense and appears to use an imaginary number
**I'm think of it a queue and tallying exec times, yes the WT grows deeper into Q, but Duh
**formula is at idx
newWT = WT + prevExec (0+0)
newWT = WT + prevExec (0 + 5) 
newWT = WT + prevExec (5 + 1)
"""
import time


def minimumWaitingTimeW(queries):
    # Write your code here. (don't get this one)
    # wait time is an imaginary #? isn't this like a Q?
    # is the hint "can mutate" a directive to "minumum"
    queries.sort()

    wait_times = [0 for x in queries]
    for idx in range(len(queries)):
        if idx == 0:
            wait_times[idx] = 0
        else:
            wait_times[idx] = wait_times[idx-1] + queries[idx-1]

    return sum(wait_times)


# Algo solution
def minimumWaitingTime(q):
    # ex: [1, 2, 2, 3, 6]
    q.sort()
    total_WT = 0
    for idx, runtime in enumerate(q):
        q_remaining = len(q) - (idx + 1)
        total_WT += runtime * q_remaining
        # R1 5-(0+1) = 4
        # R1 0 += 1 * 4 = 4
        # R2 5-(1+1) = 3
        # R2 4 += 2 * 3 = 10
        # R3 5-(2+1) = 2
        # R3 10 += 2 * 2 = 14
        # R4 5-(3+1) = 1
        # R4 14 += 3 * 1 = 17
        # R5 5-(4+1) = 0
        # R5 17 += 6 * 0 = 17
    return total_WT


q = [3, 2, 1, 2, 6]
print(minimumWaitingTimeW(q))
