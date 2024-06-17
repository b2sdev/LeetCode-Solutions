class Solution:
    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        neg = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] < 0:
                    neg += 1
        return neg


s = Solution()
assert s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]) == 8
assert s.countNegatives([[3,2],[1,0]]) == 0