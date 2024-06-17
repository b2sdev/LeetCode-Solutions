class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        result = 0
        for num1 in nums1:
            for num2 in nums2:
                if num1 % (num2 * k) == 0:
                    result += 1
        return result
    
s = Solution()
assert s.numberOfPairs([1,3,4], [1,3,4], 1) == 5
assert s.numberOfPairs([1,2,4,12], [2,4], 3) == 2