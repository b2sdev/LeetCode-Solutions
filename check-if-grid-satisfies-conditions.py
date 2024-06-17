class Solution:
    def satisfiesConditions(self, grid):
        H, W = len(grid), len(grid[0])
        for r in range(H):
            for c in range(W):
                if r + 1 < H:
                    if grid[r][c] != grid[r + 1][c]:
                        return False
                if c + 1 < W:
                    if grid[r][c] == grid[r][c + 1]:
                        return False
        return True

s = Solution()
assert s.satisfiesConditions([[1,0,2],[1,0,2]]) == True
assert s.satisfiesConditions([[1,1,1],[0,0,0]]) == False
assert s.satisfiesConditions([[1],[2],[3]]) == False