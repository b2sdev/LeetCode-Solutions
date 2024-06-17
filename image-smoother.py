class Solution:
    def imageSmoother(self, img):
        H, W = len(img), len(img[0])
        result = [[0] * W for _ in range(H)]
        dirs = (((0,0),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)))
        for r in range(H):
            for c in range(W):
                rounding_sum = 0
                count = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W:
                        rounding_sum += img[nr][nc]
                        count += 1
                result[r][c] = rounding_sum // count
        return result
    
s = Solution()
assert s.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]) == [[0,0,0],[0,0,0],[0,0,0]]
assert s.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]) == [[137,141,137],[141,138,141],[137,141,137]]