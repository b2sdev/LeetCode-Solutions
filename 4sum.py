from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        if N < 4:
            return []
        nums.sort()
        result = set()
  
        for i in range(N - 3):
            for j in range(i + 1, N - 2):
                left = j + 1
                right = N - 1
    
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        print(result)
        return list(result)

    def fourSum0(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        if N < 4:
            return []
        result = set()
        for i in range(N-3):
            for j in range(i+1,N-2):
                for k in range(j+1,N-1):
                    for l in range(k+1,N):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            result.add(tuple(sorted([nums[i] , nums[j] , nums[k] , nums[l]])))
        return result


solution = Solution()
print(solution.fourSum([1,0,-1,0,-2,2], 0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(solution.fourSum([2,2,2,2,2], 8)) # [[2,2,2,2]]
print(solution.fourSum([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90], 200)) 
