class Solution:
    def setZeroes(self, matrix):
        H, W = len(matrix), len(matrix[0])
        zero_cells = []
        for r in range(H):
            for c in range(W):
                if matrix[r][c] == 0:
                    zero_cells.append((r,c))
        for r, c, in zero_cells:
            for nc in range(0, W):
                matrix[r][nc] = 0
            for nr in range(0, H):
                matrix[nr][c] = 0
        return matrix