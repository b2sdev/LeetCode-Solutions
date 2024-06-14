from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path = []
        h = len(matrix)
        w = len(matrix[0])
        rmin, rmax = -1, h
        cmin, cmax = -1, w
        r, c = 0, 0
        dir = 0
        i = w * h
        while i > 0:
            path.append(matrix[r][c])
            if dir == 0:
                c += 1
                if c >= cmax:
                    c -= 1
                    dir = 1
                    r += 1
                    rmin += 1
            elif dir == 1:
                r += 1
                if r >= rmax:
                    r -= 1
                    dir = 2
                    c -= 1
                    cmax -= 1
            elif dir == 2:
                c -= 1
                if c <= cmin:
                    c += 1
                    dir = 3
                    r -= 1
                    rmax -= 1
            elif dir == 3:
                r -= 1
                if r <= rmin:
                    r += 1
                    dir = 0
                    c += 1
                    cmin += 1
            i -= 1
        return path


assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
