from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums_map = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                current_sum = nums[i] + nums[j]
                if current_sum not in nums_map:
                    nums_map[current_sum] = []
                nums_map[current_sum].append((i, j))

        print(nums_map)
        for k in range(len(nums)):
            target= -nums[k]
            if target in nums_map:
                for pair in nums_map[target]:
                    if i != k and j != k:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)

        print(sorted(result))
        return list(map(list, result))


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return list(result)

    # Time complexity: O(n^3)
    def threeSum0(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return list(result)
    
s = Solution()
# assert s.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert s.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]) == [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
