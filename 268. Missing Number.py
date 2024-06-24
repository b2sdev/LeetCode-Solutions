class Solution:
    def missingNumber(self, nums):
        A = [0] * (len(nums) + 1)
        for num in nums:
            A[num] = 1
        for i, num in enumerate(A):
            if num == 0:
                return i


s = Solution()
assert s.missingNumber([3, 0, 1]) == 2
assert s.missingNumber([0, 1]) == 2
assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
