class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def paths_from_ij(i,j):
            if i == m-1 or j == n-1: return 1
            if (i,j) in dp: return dp[i,j]
            
            dp[(i,j)] = paths_from_ij(i+1,j) + paths_from_ij(i,j+1)
            return dp[(i,j)]
        
        dp = {}
        return paths_from_ij(0,0)