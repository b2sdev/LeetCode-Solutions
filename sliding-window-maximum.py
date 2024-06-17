from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        window = deque()
        for i in range(len(nums)):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()

            window.append(i)
            
            if i - window[0] >= k:
                window.popleft()

            if i >= k - 1:
                result.append(nums[window[0]])
        return result

s = Solution()
assert s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
assert s.maxSlidingWindow([1], 1) == [1]