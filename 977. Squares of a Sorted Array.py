class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        index = n - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[index] = left_square
                left += 1
            else:
                result[index] = right_square
                right -= 1
            index -= 1
        return result


s = Solution()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
print(s.sortedSquares([-7, -3, 2, 3, 11]))
