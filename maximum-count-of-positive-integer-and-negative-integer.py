class Solution:
    def maximumCount(self, nums):
        pos, neg = 0, 0
        for n in nums:
            if n < 0:
                neg += 1
            elif n > 0:
                pos += 1
        return max(pos, neg)
    
s = Solution()
assert s.maximumCount([-2,-1,-1,1,2,3]) == 3
assert s.maximumCount([-3,-2,-1,0,0,1,2]) == 3
assert s.maximumCount([5,20,66,1314]) == 4