class Solution:
    def resolve(self, array):
        # [ [[1,2,3],[4,5,6]],[7,9],[4,1] ]
        def recurse(answer, subarray):
            for thing in subarray:
                if isinstance(thing, list):
                    recurse(answer, thing)
                else:
                    answer.append(thing)
            return answer

        return sorted(recurse([], array))


if __name__ == "__main__":
    a = [ [[1,2,3],[4,5,6]],[7,9],[4,1] ]
    print(Solution().resolve(a))
