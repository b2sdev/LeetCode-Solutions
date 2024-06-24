class Solution:
    def coinChange(self, coins, amount):
        value = [0] * (amount + 1)
        first = [0] * (amount + 1) # 최적해가 어떻게 만들어지는 추적
        for x in range(1, amount + 1):
            value[x] = float("inf")
            for c in coins:
                if x - c >= 0 and value[x - c] + 1 < value[x]:
                    value[x] = value[x - c] + 1
                    first[x] = c # 선택한 동전을 저장

        print(value)
        print(first)

        # 최적해에 사용되는 동전을 출력
        while amount > 0:
            print(first[amount], end=" ")
            amount -= first[amount]

        return value[-1]

    def coinChange0(self, coins, amount):
        def solve(x):
            if x < 0:
                return float("inf")
            if x == 0:
                return 0
            if ready[x]:
                return value[x]
            best = min([solve(x - c) + 1 for c in coins])
            value[x] = best
            ready[x] = True
            return best

        ready = [False] * (amount + 1)
        value = [0] * (amount + 1)
        result = solve(amount)
        return result if result != float("inf") else -1


s = Solution()
assert s.coinChange([1, 3, 4], 10) == 3
