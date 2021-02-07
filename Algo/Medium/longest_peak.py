"""
Write function that takes an array of ints and returns the length of the longest peak in the array.
A peak is defined as adjacent ints in the array that are strictly increasing until they reach
a tip (the highest value in the peak) at which point they become strictly decreasing. At least
3 ints are required to form a peak.
For ex: [1, 4, 10, 2] form a peak but [4, 0, 10] doesn't or [1, 2, 2, 0] or [1, 2, 3].
Input:
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
Output:
    6 # 0, 10, 6, 5, -1, -3

* at least 3
* start peak count at 1st increase
* if you don't ever reach a decrease, return None
* upon the first decrease, shift peak count to result
* keep track of decreases, when another increase, restart from current index
    and set min(stored res to current)
* you're keeping track of patterns
* you need at least 3 ints for the pattern to even exist
    you could take 3 elements off 1st then what?
answer - O(N)T / O(1)S
"""
import time

def longestPeak(array):

    all_peaks = []
    peak_build = 0


    if len(array) < 3:
        return 0

    for idx in range(len(array)-2):
        if array[idx] < array[idx+1] > array[idx+2]:
            peak_build += 3
            l = idx
            while l != 0:
                if array[l-1] < array[l]:
                    peak_build += 1
                    l -= 1
                else: break
            r = idx+2
            while r != len(array)-1:
                if array[r] > array[r+1]:
                    peak_build += 1
                    r += 1
                else: break
            all_peaks.append(peak_build)
            peak_build = 0

    return max(all_peaks) if all_peaks else 0


def longestPeakW(array):

    peaks_idx = []
    peaks = []
    # identify peaks
    for item in range(len(array)-2):
        if array[item] < array[item+1] > array[item+2]:
            peaks_idx.append(item+1)

    def inner_peaks(x):
        for L in range(x, 0, -1):
            if array[L-1] < array[L]:
                peaks[-1].insert(0, array[L-1])
            else: break
        for R in range(x, len(array)-1):
            if array[R+1] < array[R]:
                peaks[-1].append(array[R+1])
            else: break
        
    for x in peaks_idx:
        peaks.append([array[x]])
        inner_peaks(x)

    if not peaks: return 0
    return max(len(x) for x in peaks)



if __name__ == "__main__":

    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    #array = [1, 3, 2]
    #array = [5, 4, 3, 2, 1, 2, 10, 12]


    print(longestPeak(array))
