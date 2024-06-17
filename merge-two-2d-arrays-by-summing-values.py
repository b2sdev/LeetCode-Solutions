class Solution:
    def mergeArrays(self, nums1, nums2):
        def extract_nums(nums, nums_dict):
            for r in range(len(nums)):
                id, val = nums[r][0], nums[r][1]
                if id not in nums_dict:
                    nums_dict[id] = []
                nums_dict[id].append(val)
        nums_dict = {}
        extract_nums(nums1, nums_dict)
        extract_nums(nums2, nums_dict)
        result = []
        for id, vals in nums_dict.items():
            result.append([id, sum(vals)])
        return sorted(result, key=lambda x: x[0])
        

s = Solution()
assert s.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]) == [[1,6],[2,3],[3,2],[4,6]]
assert s.mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]) == [[1,3],[2,4],[3,6],[4,3],[5,5]]