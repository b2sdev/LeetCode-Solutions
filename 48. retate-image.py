from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        H, W = len(matrix), len(matrix[0])
        for r in range(H):
            for c in range(r + 1, W):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        for r in range(H):
            for c in range(W // 2):
                temp = matrix[r][c]
                matrix[r][c] = matrix[r][W - 1 - c]
                matrix[r][W - 1 - c] = temp
