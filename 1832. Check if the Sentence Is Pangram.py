class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

    def checkIfPangram0(self, sentence: str) -> bool:
        freq = [0] * 26
        for ch in sentence:
            freq[ord(ch) - ord("a")] += 1
        i = 0
        while i < len(freq):
            if freq[i] < 1:
                return False
            i += 1
        return True
