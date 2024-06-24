class Solution:
    def findErrorNums(self, nums):
        result = [None, None]
        seen = [0] * (len(nums) + 1)
        for num in nums:
            seen[num] += 1
        for i, freq in enumerate(seen):
            if i == 0:
                continue
            if freq > 1:
                result[0] = i
            if freq == 0:
                result[1] = i
        return result


s = Solution()
assert s.findErrorNums([1, 2, 2, 4]) == [2, 3]
assert s.findErrorNums([1, 1]) == [1, 2]
assert s.findErrorNums([2, 2]) == [2, 1]
assert s.findErrorNums([3, 2, 3, 4, 6, 5]) == [3, 1]
assert s.findErrorNums([1, 5, 3, 2, 2, 7, 6, 4, 8, 9]) == [2, 10]
