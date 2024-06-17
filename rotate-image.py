from typing import List


class Solution:
    def rotate(self, matrix):
        H, W = len(matrix), len(matrix[0])

        # Transpose the matrix
        for r in range(H):
            for c in range(r, W):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reverse each row
        for r in range(H):
            matrix[r] = matrix[r][::-1]

        return matrix

s = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
assert s.rotate(matrix) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(s.rotate(matrix))
# Output: [[9, 5, 1], [10, 6, 2], [11, 7, 3], [12, 8, 4]]