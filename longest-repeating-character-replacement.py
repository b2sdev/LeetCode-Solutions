class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_count = 0
        left = 0
        window_counts = {}
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            max_count = max(max_count, window_counts[char])
            if right - left + 1 - max_count > k:
                window_counts[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length


s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("AAABBC", 2) == 5