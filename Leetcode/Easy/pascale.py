class Solution:
    def generate(self, numRows: int) -> list:
        # Edge and Prime
        result = [ [1] ]
        if numRows == 1:
            return result
        result.append([1, 1])
        if numRows == 2:
            return result
        level = 2

        # Main logic (iter)
        while level != numRows:
            subarray = result[-1]
            iter_num = len(subarray)//2
            local = [1]
            for i in range(iter_num):
                local.append(subarray[i] + subarray[i + 1])
            if (len(subarray) % 2) == 0:
                local = local + local[len(local) - 2::-1]
            else: local = local + local[::-1]
            result.append(local)
            level += 1

        return result


if __name__ == "__main__":
    print(Solution().generate(8))
