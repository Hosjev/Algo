"""
You're given a list of arbitrary jobs that need to be completed; the jobs are represented by distinct ints. You're also given a list of arrays representing dependencies. Pairs where the 1st job is a prerequisite of the 2nd job. The 1st must come before the 2nd in your answer, no matter what's in btw them.

You're going to need to check for "cycles" and if one exists, either track it or immediately return an empty array.

Input:
    jobs = [1, 2, 3, 4]
    deps = [ [1, 2], [1, 3], [3, 2], [4, 2], [4, 3] ]

Output:
    [1, 4, 3, 2]

* this is classic topological sort graph theory
answer - O(N^2)T O(N)S
"""
import time

def topologicalSort(jobs, deps):
    """
    Out of main function, iterate over jobs.
        -starting job is 1
        -order of storing indices is len(arr)-1
        -track visited jobs even from here (due to nested diving below)
    The recurring DFS function should do the following:
        -mark job as visited
        -dive into its (edges) dependencies
        -the 1st callback is a result of the return of the index
        -store the job at index in order arr
        -since we're going from right to left, return index - 1
    Lastly, are there any SCCs?
    Given I need to keep track of originating node/job, would a stack work better?
    * inside DFS--if we Have visited AND we were an outbound edge
      (being an outbound edge means having children)
      reset this outbound edge list every for loop in main func

    """
    # Cycle and in_process allow us to watch for cycles
    cycle = False
    in_process = [True] * len(jobs)
    visited = [False] * len(jobs) # The whole purpose of which is not DFS twice

    # The vars that hold our answers
    order = [0] * len(jobs)
    o_idx = len(jobs)-1 # The starting index (last) in our order array

    for j_idx in range(len(jobs)):
        if not visited[j_idx]:
            o_idx, cycle = dfs_top_sort(o_idx, j_idx, order, visited, in_process, cycle)

    return [] if cycle else order



def dfs_top_sort(o_idx, j_idx, order, visited, in_process, cycle):
    visited[j_idx] = True

    # E pairs: [ 1, 3 ] 3 is dependent on 1 completing 1st
    # So we deep dive until last job goes onto order...
    dep_arr = [x[1] for x in deps if x[0] == jobs[j_idx]]
    for e in dep_arr:
        # If I reached this point, then j_idx HAS outbound edges
        e_idx = jobs.index(e)
        if not visited[e_idx]:
            o_idx, cycle = dfs_top_sort(o_idx, e_idx, order, visited, in_process, cycle)
        elif in_process[e_idx]:
            cycle = True

    order[o_idx] = jobs[j_idx]
    in_process[j_idx] = False
    return o_idx - 1, cycle



if __name__ == "__main__":

    jobs = [1, 2, 3, 4]
    deps = [ [1, 2], [1, 3], [3, 2], [4, 2], [4, 3] ]
    #deps = [ [1, 2], [2, 3], [3, 1] ]

    print(topologicalSort(jobs, deps))
