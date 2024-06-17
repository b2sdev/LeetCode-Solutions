from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1 = {'x1': rec1[0], 'y1': rec1[1], 'x2': rec1[2], 'y2': rec1[3]}
        r2 = {'x1': rec2[0], 'y1': rec2[1], 'x2': rec2[2], 'y2': rec2[3]}
        if r1['x1'] < r2['x2'] and r1['x2'] > r2['x1'] \
                and r1['y1'] < r2['y2'] and r1['y2'] > r2['y1']:
            return True
        return False
    
s = Solution()
assert s.isRectangleOverlap([0,0,2,2], [1,1,3,3]) == True
assert s.isRectangleOverlap([0,0,1,1], [1,0,2,1]) == False