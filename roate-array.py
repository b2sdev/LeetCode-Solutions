class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k %= n
        print(k)
        nums.reverse()
        print(nums)
        nums[:k] = reversed(nums[:k])
        print(nums)
        nums[k:] = reversed(nums[k:])
        print(nums)

s = Solution()
s.rotate([1,2,3,4,5,6,7], 3)