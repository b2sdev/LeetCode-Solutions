class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        psum = 0
        ssum = 0
        pc = 0
        sc = n - 1
        for r in range(n):
            psum += mat[r][pc]
            if pc != sc:
                ssum += mat[r][sc]
            pc += 1
            sc -= 1
        return psum + ssum

s = Solution()
assert s.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]) == 25
assert s.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == 8
assert s.diagonalSum([[5]]) == 5