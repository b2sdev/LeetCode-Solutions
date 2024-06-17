from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        W, H = len(mat[0]), len(mat)
        if r * c != H * W:
            return mat
        A = [val for row in mat for val in row]
        result = []
        k = 0
        for _ in range(r):
            row = []
            for _ in range(c):
                row.append(A[k])
                k += 1
            result.append(row)
        return result


assert Solution().matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
assert Solution().matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]
