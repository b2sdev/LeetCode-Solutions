from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        path = []
        dir = 0
        r, c = 0, 0
        i = 0
        while i < m * n:
            path.append(mat[r][c])
            if dir == 0:
                if c == n - 1:
                    r += 1
                    dir = 1
                elif r == 0:
                    c += 1
                    dir = 1
                else:
                    r -= 1
                    c += 1
            elif dir == 1:
                if r == m - 1:
                    c += 1
                    dir = 0
                elif c == 0:
                    r += 1
                    dir = 0
                else:
                    r += 1
                    c -= 1
            i += 1
        return path


assert Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
    1,
    2,
    4,
    7,
    5,
    3,
    6,
    8,
    9,
]
assert Solution().findDiagonalOrder([[1, 2], [3, 4]]) == [1, 2, 3, 4]
