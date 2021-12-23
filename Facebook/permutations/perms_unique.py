class Permutations:
    def _evaluate(self, sub_arr, placeholder, result):
        if not sub_arr and placeholder:
            result.append(placeholder)

        for i in range(len(sub_arr)):
            # Skip repetitions of sameness
            #   -if we don't check len, we could wrap around
            if len(sub_arr) > 1 and \
               sub_arr[i] == sub_arr[i - 1] and \
               i != 0:
                   continue
            local_placeholder = placeholder + sub_arr[i]
            local_sub_arr = sub_arr[:i] + sub_arr[i + 1:]
            self._evaluate(local_sub_arr, local_placeholder, result)

        return result

    def evaluate(self, string):
        return self._evaluate(sorted(string), "", [])


if __name__ == "__main__":
    s = "abac"
    obj = Permutations().evaluate(s)
    print(obj)
