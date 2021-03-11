"""
Given 2 args. 1-int k repping the number of workers. 2-array of positive ints repping the duration of work for a task. Each worker must complete 2 unique tasks and can only work on 1 at a time. The number of tasks will always be equal to 2k such that each worker has exactly 2 to complete. Workers will complete tasks in parallel and the time taken to complete ALL tasks will be equal to the time taken to complete the longest pair of tasks.

Your function should the tasks to workers pairing that optimizing this algorithm.

Input:
    k = 3
    tasks = [1, 3, 5, 3, 1, 4]
Output:
    [
        [0, 2], # 1 + 5 = 6
        [4, 5], # 1 + 4 = 5 
        [1, 3]  # 3 + 3 = 6
    ]

** note there are multiple solutions
    [2, 4], [0, 5], [1, 3]
** will always be len(tasks)/k = 2
** sum(tasks) / (k) == optimal time (tho this is true, I don't think it's gonna help me)
** maybe using a binary search with above # swapping less than and greater than btw sides
** tasks always even # (divisible by 2)
"""
import time


def taskAssignment(k, tasks):
    # Write your code here.
    matching_pairs = []
    sorted_tasks = [(idx, i) for idx, i in enumerate(tasks)]
    sorted_tasks.sort(key=lambda x: x[1])
    for i in range(int(len(sorted_tasks) / 2)):
        match = (len(sorted_tasks) - i) - 1
        matching_pairs.append([sorted_tasks[i][0], sorted_tasks[match][0]])

    return matching_pairs


tasks = [1, 3, 5, 3, 1, 4]
# tasks = [5, 6, 2, 3, 15, 15, 16, 19, 2, 10, 10, 3, 3, 32, 12, 1, 23, 32, 9, 2]

k = 3
print(taskAssignment(k, tasks))
