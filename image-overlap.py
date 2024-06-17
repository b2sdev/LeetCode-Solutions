from copy import deepcopy
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        count = [[0] * (2 * n - 1) for _ in range(2 * n - 1)]
        
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    for i2 in range(n):
                        for j2 in range(n):
                            if img2[i2][j2] == 1:
                                count[i - i2 + n - 1][j - j2 + n - 1] += 1
        print(count)
        return max([max(row) for row in count])

s = Solution()
assert s.largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]) == 3
assert s.largestOverlap([[0,1],[1,1]],[[1,1],[1,0]]) == 2