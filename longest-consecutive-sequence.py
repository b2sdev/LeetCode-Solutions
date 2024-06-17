from typing import List

class Solution:
    # Time complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in S:
                len_seq = 1
                while num + len_seq in S:
                    len_seq += 1
                longest = max(longest, len_seq)
        return longest


    # Time complexity: O(nlogn)
    def longestConsecutive1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        longest = 0
        stack = [nums[0]]
        for num in nums[1:]:
            if stack[-1] == num:
                continue
            elif (stack[-1] + 1) == num:
                stack.append(num)
            else:
                while stack:
                    stack.pop()
                stack.append(num)
            longest = max(longest, len(stack))
        return longest
    
    # Time complexity: O(nlogn)
    def longestConsecutive0(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0
        len_seq = 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                len_seq += 1
                longest = max(longest, len_seq)
            else:
                len_seq = 1
        return longest

    
s = Solution()
assert s.longestConsecutive1([100,4,200,1,3,2]) == 4
assert s.longestConsecutive1([0,3,7,2,5,8,4,6,0,1]) == 9