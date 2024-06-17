class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = ['' for _ in range(numRows)]
        row = 0
        step = 1

        for char in s:
            rows[row] += char
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
            print(char, rows)
        
        return ''.join(rows)

s = Solution()
s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
s.convert("AB", 1) == ""