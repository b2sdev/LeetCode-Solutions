from typing import List
import pytest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] < 10:
                return digits
            digits[i] = 0
            carry = 1

        if carry == 1:
            digits.insert(0, 1)

        return digits

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return

    # 136 https://leetcode.com/problems/single-number/description/
    def singleNumber(self, nums: List[int]) -> int:
        pass

    # https://leetcode.com/problems/sum-of-two-integers/
    def getSum(self, a: int, b: int) -> int:

        pass


def test_39():
    solution = Solution()
    assert solution.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert solution.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert solution.combinationSum([2], 1) == []


def test_66():
    solution = Solution()
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]


def test_136():
    solution = Solution()
    assert solution.singleNumber([2, 2, 1]) == 1
    assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
    assert solution.singleNumber([1]) == 1


def test_371():
    pass
