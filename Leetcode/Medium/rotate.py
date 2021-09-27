class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        Transpose then Mirror
        """
        def _swap(d_row, d_col, a_row, a_col):
            matrix[d_row][d_col], matrix[a_row][a_col] = matrix[a_row][a_col], matrix[d_row][d_col]


        def transpose(matrix):
            row = col = 0
            # Now we advance
            while not row == len(matrix):
                d_row, d_col = row + 1, col
                a_row, a_col = row, col + 1
                while not d_row == len(matrix):
                    _swap(d_row, d_col, a_row, a_col)
                    d_row += 1
                    a_col += 1
                # Advance outer loop
                row += 1
                col += 1


        def mirror(matrix):
            row = 0
            # Now we advance
            while not row == len(matrix):
                left = 0
                right = len(matrix) - 1
                while not left >= right:
                    _swap(row, left, row, right)
                    left += 1
                    right -= 1
                # Advance outer loop
                row += 1


        transpose(matrix)
        mirror(matrix) 
        return matrix


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = [[1, 2], [3, 4]]
s = Solution()
print(s.rotate(matrix))
print(s.rotate(m))

