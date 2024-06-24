class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = set(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"))
        s = list(s)
        vowels_chars = []
        vowels_indices = []
        for i, c in enumerate(s):
            if c in VOWELS:
                vowels_chars.append(c)
                vowels_indices.append(i)
        vowels_chars.sort()
        for i in range(len(vowels_chars)):
            s[vowels_indices[i]] = vowels_chars[i]
        return "".join(s)


s = Solution()
assert s.sortVowels("lEetcOde") == "lEOtcede"
assert s.sortVowels("lYmpH") == "lYmpH"
