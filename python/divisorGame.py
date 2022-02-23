def divisorGame(n):
    # game always end at 1? all integers have quotients, primes have 1 which is greater than 0 and less than all positive ints
    dp = {1: False, 2: True}
    def dfs(n: int) -> bool:
        if n in dp: return dp[n]

        for x in range(1,n//2):
            if n%x==0 and not dfs(n-x):
                dp[n] = True
                return True
        dp[n] = False
        return False
    return dfs(n)
