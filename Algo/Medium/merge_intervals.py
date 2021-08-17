"""
Write a function that takes in an array of non-arbitray intervals, merges any overlapping intervals, and returns new overlapping intervals in no particular order.

Input:
    input = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
Output:
    [[1, 2], [3, 8], [9, 10]]

** [1, 2] is a single interval with 0 = start and 1 = end
** [5, 7] and [8, 9] are not overlapping
** [5, 7] and [7, 9] ARE overlapping (so distinct)
** the start of ANY interval will always be less than its end [0 < 1]
** O(nlog(n)) time | O(n) space
"""
import time


def sort_array_shorthand(array):
    return array.sort(key=lambda pair: (pair[0], pair[1]))


def mergeOverlappingIntervals(intervals):

    # Write your code here.
    # 1 - evaluate pairs to order by idx 0
    # 2 - first integer 0 will be less than last 1
    # 3 - eval last_int with first_int on next pair
    # 4 - if last_int less than or equal to next_int_zero

    # Sort my array by pairs
    sort_array_shorthand(intervals)
    # Create new array with first pair
    answer_intervals = []
    # Set variables to loop over
    idx = 0
    low_pair = intervals[idx][0]
    high_pair = intervals[idx][1]
    done_flag = False

    while not done_flag:
        try:
            # Last idx, we write no matter what
            if idx == len(intervals):
                answer_intervals.append([low_pair, high_pair])
                done_flag = True
            else:
                # Get value for next_int
                next_pair_zero = intervals[idx+1][0]

                if high_pair >= next_pair_zero:
                    # Start pair remains same, end_pair should change
                    high_pair = max(intervals[idx+1][1], high_pair)
                else:
                    # Add to final array when NOT overlapping
                    answer_intervals.append([low_pair, high_pair])
                    low_pair = next_pair_zero
                    high_pair = intervals[idx+1][1]
            # Advance loop
            idx += 1
        except IndexError:
            idx = len(intervals)

    return answer_intervals


if __name__ == "__main__":
    input = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
    #input = [[1, 2], [3, 4], [5, 7], [6, 9], [9, 10]]
    #input = [[1, 2], [3, 7], [3, 4], [8, 9], [9, 10]]
    #input = [[43, 49], [9, 12], [12, 54], [45, 90], [91, 93]]

    print(mergeOverlappingIntervals(input))
