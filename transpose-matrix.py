from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        result = [[0] * m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                result[c][r] = matrix[r][c]
        return result
    
s = Solution()
assert s.transpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1,4,7],[2,5,8],[3,6,9]]
assert s.transpose([[1, 2, 3], [4,5,6]]) == [[1,4],[2,5],[3,6]]