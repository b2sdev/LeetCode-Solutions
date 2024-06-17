class Solution:
    def minSubArrayLen(self, target: int, nums):
        min_length = float('inf')
        left = 0
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0
    
s = Solution()
assert s.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
assert s.minSubArrayLen(4, [1,4,4]) == 1
assert s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0