from collections import Counter


class Solution:
    def deleteAndEarn(self, nums):
        def solve(x):
            if x == 0:
                return float("inf")
            if x == 1:
                return arr[1]
            if x == 2:
                return max(arr[1], arr[2])
            if x in memo:
                return memo[x]
            memo[x] = max(solve(x - 2) + arr[x], solve(x - 1))
            return memo[x]

        max_num = max(nums)
        arr = [0] * (max_num + 1)
        for num in nums:
            arr[num] += num

        memo = {}
        return solve(max_num)

    def deleteAndEarn0(self, nums):
        max_num = max(nums)
        points = [0] * (max_num + 1)

        for num in nums:
            points[num] += num

        prev = 0
        curr = 0

        for point in points:
            prev, curr = curr, max(curr, prev + point)

        print(curr)
        return curr

    def deleteAndEarn00(self, nums):
        def pick(x, cards):
            if x not in cards:
                return 0

            if (x, tuple(cards.items())) in memo:
                return memo[(x, tuple(cards.items()))]

            cards[x] -= 1

            deck = {}
            for k, v in cards.items():
                if k != x - 1 and k != x + 1 and v > 0:
                    deck[k] = v

            cards[x] += 1

            result = max([pick(k, deck) for k in cards.keys()]) + x
            memo[(x, tuple(cards.items()))] = result

            return result

        memo = {}
        return max(pick(x, Counter(nums)) for x in set(nums))


s = Solution()
assert s.deleteAndEarn([3, 4, 2]) == 6
assert s.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
assert s.deleteAndEarn([8, 7, 3, 8, 1, 4, 10, 10, 10, 2]) == 52
assert (
    s.deleteAndEarn([3, 7, 10, 5, 2, 4, 8, 9, 9, 4, 9, 2, 6, 4, 6, 5, 4, 7, 6, 10])
    == 66
)
assert (
    s.deleteAndEarn(
        [
            1,
            8,
            5,
            9,
            6,
            9,
            4,
            1,
            7,
            3,
            3,
            6,
            3,
            3,
            8,
            2,
            6,
            3,
            2,
            2,
            1,
            2,
            9,
            8,
            7,
            1,
            1,
            10,
            6,
            7,
            3,
            9,
            6,
            10,
            5,
            4,
            10,
            1,
            6,
            7,
            4,
            7,
            4,
            1,
            9,
            5,
            1,
            5,
            7,
            5,
        ]
    )
    == 138
)
assert (
    s.deleteAndEarn(
        [
            10,
            8,
            4,
            2,
            1,
            3,
            4,
            8,
            2,
            9,
            10,
            4,
            8,
            5,
            9,
            1,
            5,
            1,
            6,
            8,
            1,
            1,
            6,
            7,
            8,
            9,
            1,
            7,
            6,
            8,
            4,
            5,
            4,
            1,
            5,
            9,
            8,
            6,
            10,
            6,
            4,
            3,
            8,
            4,
            10,
            8,
            8,
            10,
            6,
            4,
            4,
            4,
            9,
            6,
            9,
            10,
            7,
            1,
            5,
            3,
            4,
            4,
            8,
            1,
            1,
            2,
            1,
            4,
            1,
            1,
            4,
            9,
            4,
            7,
            1,
            5,
            1,
            10,
            3,
            5,
            10,
            3,
            10,
            2,
            1,
            10,
            4,
            1,
            1,
            4,
            1,
            2,
            10,
            9,
            7,
            10,
            1,
            2,
            7,
            5,
        ]
    )
    == 338
)

# Boredom
