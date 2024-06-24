# https://leetcode.com/problems/house-robber


class Solution:
    def rob(self, nums):
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(
                dp[i - 1],  # 인접한 이전 집까지 턴 돈
                dp[i - 2]
                + nums[i],  # 인접하지 않은 이전 집까지 턴 돈에 이번 집을 턴 돈의 합
            )
        print(dp)
        return dp[-1]

    def rob0(self, nums):
        def solve(x):
            if x < 0:
                return float("inf")
            if x == 0:
                return nums[0]
            if x == 1:
                return max(nums[0], nums[1])
            if ready[x]:
                return value[x]
            value[x] = max(solve(x - 1), solve(x - 2) + nums[x])
            ready[x] = True
            return value[x]

        ready = [False] * len(nums)
        value = [0] * len(nums)

        return solve(len(nums) - 1)


s = Solution()
assert s.rob0([1, 2, 3, 1]) == 4
assert s.rob0([2, 7, 9, 3, 1]) == 12
