class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        res = s[0]
        num_min = 1

        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True

        for j in range(1, len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] == True:
                    if j-i+1 > num_min:
                        num_min = j-i+1
                        res = s[i:j+1]

        return res