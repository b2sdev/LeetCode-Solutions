class Solution:
    def groupThePeople(self, groupSizes):
        groups = {}
        result = []

        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            
            groups[size].append(i)

            if len(groups[size])  == size:
                result.append(groups[size])
                groups[size] = []

        return sorted(result, key=len)

s = Solution()
assert s.groupThePeople([3,3,3,3,3,1,3]) == [[5],[0,1,2],[3,4,6]]
assert s.groupThePeople([2,1,3,3,3,2]) == [[1],[0,5],[2,3,4]]
assert s.groupThePeople([2,2,1,1,1,1,1,1]) == [[2],[3],[4],[5],[6],[7],[0,1]]