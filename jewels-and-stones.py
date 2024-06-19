from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 for stone in stones if stone in set(jewels))

    def numJewelsInStones0(self, jewels: str, stones: str) -> int:
        freq = Counter(stones)
        return sum(freq[jewel] for jewel in jewels)
