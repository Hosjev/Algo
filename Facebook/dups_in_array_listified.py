class DupsArray:

    def find(self, arr):
        if len(arr) == len(set(arr)):
            return []

        arr.sort()
        result = set() # This could be empty
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                result.add(arr[i])
        return list(result)


if __name__ == "__main__":
    obj = DupsArray()
    print(obj.find([0,0,0,1,2,3,3]))
