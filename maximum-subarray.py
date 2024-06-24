# https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    # Time complexity: O(nlogn)
    # Space complexity: O(logn)
    def maxSubArray(self, nums):
        def max_subarray(arr, lo, hi):
            if lo == hi:
                return arr[lo]
            mid = (lo + hi) // 2
            left_sum = max_subarray(arr, lo, mid)
            right_sum = max_subarray(arr, mid + 1, hi)
            cross_sum = max_crossing_subarray(arr, lo, mid, hi)
            print(lo, mid, hi, left_sum, cross_sum, right_sum)
            return max(left_sum, right_sum, cross_sum)

        def max_crossing_subarray(arr, lo, mid, hi):
            left_sum = float("-inf")
            curr_sum = 0
            for i in range(mid, lo - 1, -1):
                curr_sum += arr[i]
                left_sum = max(left_sum, curr_sum)
            right_sum = float("-inf")
            curr_sum = 0
            for i in range(mid + 1, hi + 1):
                curr_sum += arr[i]
                right_sum = max(right_sum, curr_sum)
            return left_sum + right_sum

        return max_subarray(nums, 0, len(nums) - 1)

    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxSubArray0(self, nums):
        best_sum = float("-inf")
        curr_sum = 0
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            best_sum = max(best_sum, curr_sum)
        return best_sum


s = Solution()
assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
# assert s.maxSubArray([1]) == 1
# assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
