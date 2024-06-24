class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        reverse = 1
        for i in range(0, len(s), k):
            j = i + k
            if j >= len(s):
                j = len(s)
            if reverse > 0:
                result.append(s[i:j][::-1])
            else:
                result.append(s[i:j])
            reverse *= -1
        return "".join(result)


s = Solution()
assert s.reverseStr("abcdefg", 2) == "bacdfeg"
assert s.reverseStr("abcd", 2) == "bacd"
