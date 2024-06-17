from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        width = [-1, n]
        height = [-1, n]
        r, c = 0, 0
        k = 1
        dir = 0
        while k <= n * n:
            matrix[r][c] = k
            if dir == 0:
                c += 1
                if c >= width[1]:
                    c -= 1
                    dir += 1
                    r += 1
                    height[0] += 1
            elif dir == 1:
                r += 1
                if r >= height[1]:
                    r -= 1
                    dir += 1
                    c -= 1
                    width[1] -= 1
            elif dir == 2:
                c -= 1
                if c <= width[0]:
                    c += 1
                    dir += 1
                    r -= 1
                    height[1] -= 1
            elif dir == 3:
                r -= 1
                if r <= height[0]:
                    r += 1
                    dir += 1
                    c += 1
                    width[0] += 1
            if dir == 4:
                dir = 0
            k += 1
        return matrix


assert Solution().generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert Solution().generateMatrix(4) == [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]
