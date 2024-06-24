class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        for word in s.split(" "):
            result += word[::-1] + " "
        return result[:-1]

    def reverseWords0(self, s):
        s = list(s)
        left = right = 0
        while right < len(s):
            while right < len(s) and s[right] != " ":
                right += 1
            right -= 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                right -= 1
                left += 1
            while left < len(s) and s[left] != " ":
                left += 1
            left += 1
            right = left + 1
        return "".join(s)


s = Solution()
assert s.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert s.reverseWords("Mr Ding") == "rM gniD"
