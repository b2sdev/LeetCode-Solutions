from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return next(
            [i, j + (i + 1)]
            for i, x in enumerate(nums)
            for j, y in enumerate(nums[i + 1 :])
            if x + y == target
        )

    def twoSum0(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return None


s = Solution()
assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert s.twoSum([3, 2, 4], 6) == [1, 2]
assert s.twoSum([3, 3], 6) == [0, 1]
