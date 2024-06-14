from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def same(r, c):
            while r < m - 1 and c < n - 1:
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
                r += 1
                c += 1
            return True

        m, n = len(matrix), len(matrix[0])
        c = 0
        for r in range(m):
            if not same(r, c):
                return False
        r = 0
        for c in range(n):
            if not same(r, c):
                return False
        return True


assert Solution().isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]) == True
assert Solution().isToeplitzMatrix([[1, 2], [2, 2]]) == False
