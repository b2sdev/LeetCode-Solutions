from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        deq = deque([ch for ch in s.lower() if ch.isalnum()])
        while len(deq) > 1:
            if deq.popleft() != deq.pop():
                return False
        return True

s = Solution()
assert s.isPalindrome("A man, a plan, a canal: Panama") == True
assert s.isPalindrome("race a car") == False
assert s.isPalindrome(" ") == True