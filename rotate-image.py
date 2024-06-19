from typing import List


class Solution:
    def rotate(self, matrix):
        matrix[:] = list(map(list, zip(*matrix[::-1])))
        return matrix

    def rotate0(self, matrix):
        H, W = len(matrix), len(matrix[0])

        # Transpose the matrix
        for r in range(H):
            for c in range(r, H):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reverse each row
        for r in range(W):
            matrix[r] = matrix[r][::-1]

        return matrix


s = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert s.rotate(matrix) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
assert s.rotate(matrix) == [
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11],
]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(s.rotate0(matrix))
# Output: [[9, 5, 1], [10, 6, 2], [11, 7, 3], [12, 8, 4]]
