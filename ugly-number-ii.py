class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = []
        k = 1
        while len(ugly_numbers) < n:
            num = k
            for prime in [2, 3, 5]:
                while num % prime == 0:
                    num //= prime
            if num == 1:
                ugly_numbers.append(k)
            k += 1
        return ugly_numbers[-1]

s = Solution()
s.nthUglyNumber(10)
s.nthUglyNumber(1)
s.nthUglyNumber(453)
# assert s.isUgly(6) == True
# assert s.isUgly(1) == True
# assert s.isUgly(14) == False