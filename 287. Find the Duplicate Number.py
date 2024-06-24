class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Detect if there's a cycle
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: Find the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


s = Solution()
assert s.findDuplicate([1, 3, 4, 2, 2]) == 2
assert s.findDuplicate([3, 1, 3, 4, 2]) == 3
assert s.findDuplicate([3, 3, 3, 3, 3]) == 3


# https://keithschwarz.com/interesting/code/?dir=find-duplicate
