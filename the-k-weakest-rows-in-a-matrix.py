from collections import Counter


class Solution:
    def kWeakestRows(self, mat, k):
        return list(
            map(
                lambda x: x[1],
                sorted(
                    zip(
                        map(lambda x: x[1], map(Counter, mat)),
                        [i for i in range(len(mat))],
                    )
                )[:k],
            )
        )


s = Solution()
assert s.kWeakestRows(
    [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ],
    3,
) == [2, 0, 3]
assert s.kWeakestRows([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2) == [
    0,
    2,
]
