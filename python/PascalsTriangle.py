class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        dp = {0: [1],1: [1,1]}
        for i in range(numRows):
            if i in dp: 
                out.append(dp[i])
            else:
                c = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        c.append(1)
                    else:
                        c.append(dp[i-1][j-1]+ dp[i-1][j])
                dp[i] = c
                out.append(c)
        return out
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        dp = {0: [1],1: [1,1]}
        for i in range(numRows):
            if i not in dp: dp[i] = [1] + [dp[i-1][j-1]+dp[i-1][j] for j in range(1,i)] + [1]
            out.append(dp[i])
        return out