class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        i, j, k = 1, 1, 1
        for m in range(2, n + 1):
            dp[m] = min(dp[i] * 2, dp[j] * 3, dp[k] * 5)
            if dp[m] == dp[i] * 2:
                i += 1
            if dp[m] == dp[j] * 3:
                j += 1
            if dp[m] == dp[k] * 5:
                k += 1
        return dp[-1]