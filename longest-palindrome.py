class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        length = 0
        odd_present = False

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_present = True
        
        if odd_present:
            length += 1
        
        return length
    
s = Solution()
assert s.longestPalindrome("abccccdd") == 7
assert s.longestPalindrome("ccc") == 3
