class Solution:
    def numberOfLines(self, widths, s):
        row_count = 1
        pixels_wide = 0
        for c in s:
            pixel = widths[ord(c) - ord("a")]
            if pixel + pixels_wide <= 100:
                pixels_wide += pixel
            else:
                row_count += 1
                pixels_wide = pixel
        return [row_count, pixels_wide]


s = Solution()
assert s.numberOfLines(
    [
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
    ],
    "abcdefghijklmnopqrstuvwxyz",
) == [3, 60]
assert s.numberOfLines(
    [
        4,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
        10,
    ],
    "bbbcccdddaaa",
) == [2, 4]
