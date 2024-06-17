from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 0
        step_len = 1
        
        while len(result) < rows * cols:
            print(steps)
            for _ in range(2):
                dx, dy = dirs[steps % 4]
                for _ in range(step_len):
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart, cStart])
                    rStart += dx
                    cStart += dy
                steps += 1
            step_len += 1
        
        return result

s = Solution()
print(s.spiralMatrixIII(1, 4, 0, 0))
print(s.spiralMatrixIII(5,6, 1, 4))