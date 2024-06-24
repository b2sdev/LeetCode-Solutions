class Solution:
    def change(self, amount, coins):
        count = [0] * (amount + 1)
        count[0] = 1
        # for x in range(1, amount + 1):
        #     for c in coins:
        #         if x - c >= 0:
        #             count[x] += count[x - c]
        for c in coins:
            for x in range(c, amount + 1):
                count[x] += count[x - c]
        return count[amount]

    def change0(self, amount, coins):
        def solve(x, start):
            if x == 0:
                return 1
            if (x, start) in memo:
                return memo[(x, start)]
            count = 0
            for i in range(start, len(coins)):
                c = coins[i]
                if x - c >= 0:
                    count += solve(x - c, i)
            memo[(x, start)] = count
            return count

        memo = {}
        return solve(amount, 0)


s = Solution()
print(s.change0(5, [1, 2, 5]))  # 4
print(s.change0(3, [2]))  # 0
print(s.change0(10, [10]))  # 1
