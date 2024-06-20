class Solution:
    def maxSubArray(self, nums):
        best_sum = float("-inf")
        curr_sum = 0
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            best_sum = max(best_sum, curr_sum)
        return best_sum


s = Solution()
assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert s.maxSubArray([1]) == 1
assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
