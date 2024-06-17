from collections import Counter
class Solution:
    def findLonely(self, nums):
        num_counts = Counter(nums)
        result = []
        for num in nums:
            if num_counts[num] == 1 and num_counts.get(num - 1, 0) == 0 and num_counts.get(num +1, 0) == 0:
                result.append(num)
        return result
    
s = Solution()
assert s.findLonely([10,6,5,8]) == [10,8]
assert s.findLonely([1,3,5,3]) == [1,5]