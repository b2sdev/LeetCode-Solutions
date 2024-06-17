class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime
        
        return n == 1

s = Solution()
assert s.isUgly(6) == True
assert s.isUgly(1) == True
assert s.isUgly(14) == False