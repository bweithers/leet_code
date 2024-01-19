class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        dp = matrix[-1]

        for i in range(n-2,-1,-1):
            new = [0]*n

            # set last and first entries separately to avoid if checks in every iteration
            new[0] = matrix[i][0] + min(dp[0],dp[1])
            new[n-1] = matrix[i][n-1] + min(dp[n-1],dp[n-2])

            for j in range(1,n-1):
                new[j] = matrix[i][j]+ min([dp[j+os] for os in range(-1,2)])
            dp = new
        return min(dp)