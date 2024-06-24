class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * (n + 1)
        for end in range(1, n):
            for start in range(end):
                if nums[start] < nums[end]:
                    dp[end] = max(dp[end], dp[start] + 1)
        return max(dp)


s = Solution()
assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert s.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
assert s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
