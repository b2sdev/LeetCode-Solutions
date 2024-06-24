class Solution:
    def wordBreak(self, s, wordDict):
        def dfs(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and dfs(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        memo = {}
        return dfs(0)

    def wordBreak0(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for end in range(1, n + 1):
            for start in range(end):
                if dp[start] and s[start:end] in wordDict:
                    dp[end] = True
                    break

        print(dp)
        return dp[n]

    # Not working with greedy
    def wordBreak0(self, s, wordDict):
        word_set = set(wordDict)
        word_len = sorted(list(set(map(lambda x: len(x), word_set))), reverse=True)
        print(word_len)
        i = 0
        while i < len(s):
            segmented = False
            for k in word_len:
                j = i + k
                print(i, j)
                if j <= len(s) and s[i:j] in word_set:
                    print(s[i:j])
                    i = j
                    segmented = True
                    break

            if not segmented:
                return False

        return True


s = Solution()
assert s.wordBreak("leetcode", ["leet", "code"]) == True
assert s.wordBreak("applepenapple", ["apple", "pen"]) == True
assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
assert s.wordBreak("aaaaaaa", ["aaaa", "aaa"]) == True
assert s.wordBreak("abcd", ["a", "abc", "b", "cd"]) == True
