class Solution:
    def findMatrix(self, nums):
        result = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        while freq:
            group = []
            for key in freq.keys():
                group.append(key)
            for key in group:
                freq[key] -= 1
                if freq[key] == 0:
                    del freq[key]
            result.append(group)
        return result

s = Solution()
assert s.findMatrix([1,3,4,1,2,3,1]) == [[1,3,4,2],[1,3],[1]]
assert s.findMatrix([2,1,1]) == [[2,1],[1]]