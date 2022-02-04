from typing import List



class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Separate digits
        digits = list()
        idx = 0
        while idx < len(logs):
            line = logs[idx]
            if line.split(" ")[1].isdigit():
                logs.pop(idx)
                digits.append(line)
            else: idx += 1

        # Sort by [1...:]
        logs.sort(key=lambda x: x.split(" ")[1])

        # Sort [0] if [1..:] same
        idx = 0
        while idx < len(logs):
            pointer = idx+1
            pattern = logs[idx].split(" ")[1:]
            if pointer < len(logs)-1 and pattern == logs[pointer].split(" ")[1:]:
                while pointer < len(logs) and pattern == logs[pointer].split(" ")[1:]:
                    pointer += 1
                t = logs[idx:pointer]
                t.sort(key=lambda x: x.split(" ")[0])
                logs = t + logs[pointer:]
                idx = pointer
            else: idx += 1

        return logs + digits


if __name__ == "__main__":
    l = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    l = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    l = ["a1 9 2 3 1", "g1 act car", "c1 act car", "a1 act car", "zo4 4 7","ab1 off key dog","a8 act zoo"]
    obj = Solution()
    print(obj.reorderLogFiles(l))
