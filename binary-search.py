class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        return -1
    
s = Solution()
assert s.search([-1,0,3,5,9,12], 9) == 4
assert s.search([-1,0,3,5,9,12], -2) == -1 