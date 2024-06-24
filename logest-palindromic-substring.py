class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s) - 1):
            result = max(
                result,
                expand_around_center(i, i),
                expand_around_center(i, i + 1),
                key=len,
            )

        return result

    def longestPalindrome0(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if substring == substring[::-1] and len(substring) > len(result):
                    result = substring
        return result


s = Solution()
print(s.longestPalindrome("babad"))  # "bab" or "aba"
print(s.longestPalindrome("cbbd"))  # "bb"
print(s.longestPalindrome("abb"))  # "bb"
