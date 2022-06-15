class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        rv = 1
        for w in sorted(words, key=len):
            dp[w] = 1
            for i,c in enumerate(w):
                prev = w[:i] + w[i+1:]
                if prev in dp: 
                    dp[w] = dp[prev] + 1
                    rv = max(rv, dp[w])
        
        return rv