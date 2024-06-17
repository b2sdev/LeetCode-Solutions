from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = Counter(stones)
        return sum(freq[jewel] for jewel in jewels)