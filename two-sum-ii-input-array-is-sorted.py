class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []

    def twoSum0(self, numbers, target):
        for i in range(len(numbers)):
            left, right = i+1, len(numbers) - 1
            expected = target - numbers[i]
            print(left, right, expected)
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == expected:

                    return [i + 1, mid + 1]
                elif numbers[mid] < target:
                    left += 1
                else:
                    right -= 1
        return []

s = Solution()
assert s.twoSum0([2,7,11,15], 9) == [1,2]
assert s.twoSum0([2,3,4], 6) == [1,3]
assert s.twoSum0([-1,0], -1) == [1,2]