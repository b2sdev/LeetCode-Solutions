class Solution:
    def mincostTickets(self, days, costs):
        dp = [0] * (days[-1] + 1)
        travel_days = set(days)

        for i in range(1, len(dp)):
            if i not in travel_days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2],
                )

        return dp[-1]

    def mincostTickets0(self, days, costs):
        # 날짜 x를 포함하여 이전의 모든 여행 날짜를 커버하는 티킷의 최소 비용
        def solve(x):
            if x < 0:
                # 비용의 합을 음수로 만들 수 없기에 무한대
                return float("inf")
            if x == 0:
                # 비용이 필요하지 않기에 0
                return 0
            if x not in travel_days:
                # 날짜 x가 여행 날짜에 포함되지 않으므로
                # 이전 날짜의 최소 비용을 유지
                return solve(x - 1)

            return min(
                solve(x - 1) + costs[0],
                solve(x - 7) + costs[1],
                solve(x - 30) + costs[2],
            )

        travel_days = set(days)
        return solve(days[-1])


s = Solution()
print(s.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
print(s.mincostTickets0([1, 4, 6, 7, 8, 20], [2, 7, 15]))
print(s.mincostTickets0([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
