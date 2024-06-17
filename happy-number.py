class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            
            # n = sum(int(digit) ** 2 for digit in str(n))

            new_n = 0
            while n > 0:
                digit = n % 10
                new_n += digit ** 2
                n //= 10
            n = new_n
            
        return True

s = Solution()
assert s.isHappy(19) == True
assert s.isHappy(2) == False