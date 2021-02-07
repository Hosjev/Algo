"""
Write a function that takes in 2 strings: a main string and a potential substring of the main. The function should return a version of the main string with every instance of the substring in it wrapped between underscores.

Input:
    str = "testthis is a testtest to see if testestest it works"
    substr = "test"

Output:
    "_test_this is a _testtest_ to see if _testestest_ it works"

answer - O(NM)T / O(NM)S --M is 2nd string
"""
import time


def underscorifySubstring(string, substr):
    """
    Algo version:
        -create empty hash table
        -this hash table will store unique characters and track their index
        -create solution string and store result (longest) here
        -track "start" of new non-dup strings with "pointer"
    """
    locations = get_locations(string, substr)
    if len(locations) == 0: return string

    # Else do main logic
    #print(locations)
    collapsed = collapse_locations(locations)
    #print(collapsed)
    string_list = list(string)
    # We have to insert from the REAR b/c indices change when we go from 0
    for x in reversed(collapsed):
        for y in reversed(x):
            string_list.insert(y, "_")

    return ("").join(string_list)


def collapse_locations(locations):
    collapsed = [locations[0]]
    for idx in range(1, len(locations)):
        prev = collapsed[-1]
        current = locations[idx]
        #print("idx/prev/curr:", idx, prev, current, collapsed)
        if prev[1] >= current[0]:
            collapsed[-1][1] = current[1]
        else:
            collapsed.append(current)

    return collapsed


def get_locations(string, substr):
    locations = []
    pointer = 0
    idx = 0
    while idx != -1:
        time.sleep(.2)
        print(idx)
        idx = string.find(substr, pointer)
        if idx != -1:
            locations.append([idx, idx+len(substr)])
            pointer = idx + 1

    return locations


if __name__ == "__main__":

    string = "testthis is a testtest to see if testestest it works"
    substr = "test"

    print(underscorifySubstring(string, substr))
