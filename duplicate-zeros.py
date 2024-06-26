class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                for j in range(n - 1, i, -1):
                    arr[j] = arr[j - 1]
                if i + 1 < n:
                    arr[i + 1] = 0
                i += 1
            i += 1
        print(arr)

    def duplicateZeros0(arr):
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1
        print(arr)


s = Solution()
s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])  # [1, 0, 0, 2, 3, 0, 0, 4]
s.duplicateZeros([8, 5, 0, 9, 0, 3, 4, 7])  # [8, 5, 0, 0, 9, 0, 0, 3]
s.duplicateZeros([0, 0, 0, 0, 0, 0, 0])  # [0, 0, 0, 0, 0, 0, 0]
s.duplicateZeros([8, 4, 5, 0, 0, 0, 0, 7])  # [8, 4, 5, 0, 0, 0, 0, 0]
