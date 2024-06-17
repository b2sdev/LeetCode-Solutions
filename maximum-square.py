class Solution:
    def maximalSquare(self, matrix):
        H, W = len(matrix), len(matrix[0])
        max_square = 0

        for r in range(H):
            for c in range(W):
                if matrix[r][c] != 1:
                    continue
                # if c == W - 1:
                #     max_square = max(max_square, 1)
                #     continue
                print(r, c)
                offset = 1
                while r + offset < H and c + offset < W:
                    print((r, c, offset))
                    valid = True
                    for nr in range(r, r + offset + 1):
                        for nc in range(c, c + offset + 1):
                            print(nr, nc, matrix[nr][nc])
                            if matrix[nr][nc] != 1:
                                valid = False
                                break
                    if not valid:
                        break
                    print("HERE")
                    max_square = max(max_square, (1 + offset) * 2)
                    offset += 1
        print(max_square)    
        return max_square            
    
s = Solution()
assert s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4
