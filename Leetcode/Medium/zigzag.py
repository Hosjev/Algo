def zigzag(s, numRows):
    """
    1. solving this with boolean pattern
    2. use negative numbers to move up
    3. take absolute value to get proper index
    4. store this in a type (but less exp) data structure
       a. ["", ""...] array of strings
    """
    # Edge case
    if numRows == 1: return s

    # Prime/init our linear eval
    row = 0
    answer = [""] * numRows

    # Linear eval O(N) -- best TC
    for idx in range(len(s)):
        answer[abs(row)] += s[idx]
        # Changing directions
        if row == numRows - 1:
            row = (numRows - 1) * -1
        # We advance row no matter direction
        row += 1

    return "".join(answer)



def leet_py_solution(s, numRows):
        # By row then col
        row = 0
        pointer = 1
        output = [""] * numRows # ["", "", ""]

        # 14
        for i in range(len(s)):
            # 0 -- outp ["p",...]
            # 1 -- outp ["p", "a"...]
            # 2 -- outp ["p", "a", "y"]
            # 3 -- outp ["p", "ap", "y"]
            # 4 -- outp ["pa", "ap", "y"]
            # 5 -- outp ["pa", "apl", "y"]
            # 6 -- outp ["pa", "apl", "yi"]
            # 7 -- outp ["pa", "apls", "yi"]
            # 8 -- outp ["pah", "apls", "yi"]
            # 9 -- outp ["pah", "aplsi", "yi"]
            # 10 -- outp ["pah", "aplsi", "yir"]
            # 11 -- outp ["pah", "aplsii", "yir"]
            # 12 -- outp ["pahn", "aplsii", "yir"]
            # 13 -- outp ["pahn", "aplsiig", "yir"]
            output[row] += s[i]
            if numRows > 1: # 3
                # 0 -- row = 0 + 1 = 1
                # 1 -- row = 1 + 1 = 2
                # 2 -- row = 2 + -1 = 1
                # 3 -- row = 1 + -1 = 0
                # 4 -- row = 0 + 1 = 1
                # 5 -- row = 1 + 1 = 2
                # 6 -- row = 2 + -1 = 1
                # 7 -- row = 1 + -1 = 0
                # 8 -- row = 0 + 1 = 1
                # 9 -- row = 1 + 1 = 2
                # 10 -- row = 2 + -1 = 1
                # 11 -- row = 1 + -1 = 0
                # 12 -- row = 0 + 1 = 1
                # 13 -- row = 1 + 1 = 2
                row = row + pointer
                # 0 -- 1 is 0? OR 1 is 3-1?
                # 1 -- 2 is 0? OR 2 is 3-1? Y
                # 2 -- 1 is 0? OR 1 is 3-1? 
                # 3 -- 0 is 0? OR 0 is 3-1? Y
                # 4 -- 1 is 0? OR 1 is 3-1?
                # 5 -- 2 is 0? OR 2 is 3-1? Y
                # 6 -- 1 is 0? OR 1 is 3-1?
                # 7 -- 0 is 0? OR 0 is 3-1? Y
                # 8 -- 1 is 0? OR 1 is 3-1?
                # 9 -- 2 is 0? OR 2 is 3-1? Y
                # 10 -- 1 is 0? OR 1 is 3-1?
                # 11 -- 0 is 0? OR 0 is 3-1? Y
                # 12 -- 1 is 0? OR 1 is 3-1?
                if (row == 0) or (row == numRows -1):
                    # 1 -- p = 1 * -1 = -1
                    # 3 -- p = -1 * -1 = 1
                    # 5 -- p = 1 * -1 = -1
                    # 7 -- p = -1 * -1 = 1
                    # 9 -- p = 1 * -1 = -1
                    # 11 -- p = -1 * -1 = 1
                    pointer = pointer * -1

        print(output)
        outputStr = ""
        for j in range(numRows):
            outputStr += output[j]
        return outputStr


s = "paypalishiring"
s = "ab"
print(zigzag(s, 1))
