from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        remainder_dict  = {}

        for t in time:
            if t % 60 == 0:
                count += remainder_dict.get(0, 0)
            else:
                count += remainder_dict.get(60 - t % 60, 0)
            remainder_dict[t % 60] = remainder_dict.get(t % 60, 0) + 1

        return count

    def numPairsDivisibleBy60_(self, time: List[int]) -> int:
        count = 0
        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count
    

s = Solution()
assert s.numPairsDivisibleBy60([30,20,150,100,40]) == 3
assert s.numPairsDivisibleBy60([60,60,60]) == 3
assert s.numPairsDivisibleBy60_([30,20,150,100,40]) == 3
assert s.numPairsDivisibleBy60_([60,60,60]) == 3