# Write function that takes array of integers as input and returns a 2-digit complete range within.
# example input: [5, 9, 10, 3, 2, 1, 0, 7, 13]
# example input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
# example output: [0, 3]
# My solution: sort then iterate through numbers matching each to the previous, forming ranges
# Their solution: -form a hash table with key=number, value=False
#                 -iterate through array checking is previous and future numbers present in
#                  hash table, marking as True (the most continguous "True" is the winner
import copy

test1 = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
test2 = [1, 6, 7, 8, 9, 10, 11, 18, 20, 22, 24]
test3 = [0, 2, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 24, 25, 26, 27, 28, 29, 30, 32, 35, 38, 39, 40, 43, 48, 50, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 64, 65, 66, 67, 70, 73, 76, 77, 83, 84, 85, 86, 87, 89, 90, 91, 92, 93, 95, 96, 98, 99, 100, 101, 105, 106, 107, 109, 112, 113, 116, 117, 119, 120, 122, 123, 124]
test8 = [ 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14 ]


def largestRangeAlgo(testCase):
    # this is horrible right now
    rangeHash = {}
    ranges = []
    rangeFinals = []
    stack = copy.deepcopy(testCase)

    # Create hash table
    for x in testCase:
        rangeHash[x] = False

    # Iterate through stack, tagging only contiguous nums
    for x in stack:
        if not rangeHash[x]:
            if (x - 1) in stack:
                rangeHash[x] = True
                rangeHash[x - 1] = True
            if (x + 1) in stack:
                rangeHash[x] = True
                rangeHash[x + 1] = True

    # Create ranges arrays for TRUEs
    for k, v in rangeHash.items():
        if v:
            ranges.append(k)


    # Function to order them from small to large
    def largest(index, now, future):
        while len(ranges) != 0:
            future = ranges.pop(0)
            if (now + 1) == future:
                rangeFinals[index].append(future)
            else:
                rangeFinals.append([future])
                index = rangeFinals.index(rangeFinals[-1])
            largest(index, future, 0)

    # sort them 
    ranges.sort()
    now = ranges.pop(0)
    rangeFinals.append([now])
    largest(0, now, 0)
    # nab biggie
    maxLen = max(len(x) for x in rangeFinals)
    maxR = [x for x in rangeFinals if len(x) == maxLen][0]
    return [ maxR[0], maxR[-1] ]



def largestRange(testCase):

    def compareRangeInts(index, current):
        # do stuff
        while len(stack) != 0:
            nextInt = stack.pop(0)
            if (current + 1) == nextInt:
                ranges[index].append(nextInt)
                newIndex = index
            else:
                ranges.append([nextInt])
                newIndex = ranges.index([nextInt])
    
            compareRangeInts(newIndex, nextInt)

    def beginRangeComparison():
        nextInt = stack.pop(0)
        ranges.append([nextInt])
        compareRangeInts(ranges.index([nextInt]), nextInt)

    def scrubHighs():
        high = len(testCase) + 1
        for x in testCase:
            if x > high:
                testCase.remove(x)
        return testCase

    def makeItPretty():
        lenWinner = max(len(x) for x in ranges)
        for x in ranges:
            if len(x) == lenWinner: return [ x[0], x[-1] ]


    # Sanity check
    if len(testCase) == 0: return []
    # Get rid of duplicates
    testCase = list(set(testCase))
    # Sort numerically/make stack/create ranges array/run the main logic
    # Next step below, to optimize, would be getting rid of sort
    testCase.sort()
    stack = scrubHighs()
    ranges = []
    beginRangeComparison()
    return makeItPretty()


if __name__ == "__main__":
    #
    largest = largestRange(test8)
    print(largest)

    print(largestRangeAlgo(test1))
