class Substring:
    """ O(n*m) """
    def longest_match(self, str1, str2):
        if not str1 or not str2: return ""
        str1 = "_" + str1
        str2 = "_" + str2
        matrix = [[0 for j in range(len(str2))] for i in range(len(str1))]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if str1[i] == str2[j]:
                    matrix[i][j] = 1 + matrix[i-1][j-1]
                else:
                    matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

        print(matrix)
        return matrix[-1][-1]


def main():
    s1 = "affoobar"
    s2 = "foobar"
    print(Substring().longest_match(s1, s2))


main()
