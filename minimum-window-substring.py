from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counts = Counter(t)
        window_counts = {}
        required = len(target_counts)
        formed = 0
        min_length = float('inf')
        start = 0
        left = right = 0

        while right < len(s):
            char = s[right]

            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                window_counts[s[left]] -= 1
                if char in target_counts and window_counts[s[left]] < target_counts[s[left]]:
                    formed -= 1

                left += 1 

            right += 1
        
        return s[start:start + min_length] if min_length != float('inf') else ''
    
s = Solution()
assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert s.minWindow("a", "a") == "a"
assert s.minWindow("a", "aa") == ""