class Solution:
    def countSubstrings(self, s: str) -> int:
        str_len = len(s)
        if str_len == 0 or s is None:
            return 0
        res = 0
        dp = [[False for _ in range(str_len)] for _ in range(str_len)]
        for i in range(str_len):
            dp[i][i] = True
        for j in range(str_len):
            for i in range(0, j):
                if j-i == 0:
                    dp[i][j] = True
                elif j-i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]

        for i in range(str_len):
            for j in range(str_len):
                if dp[i][j] == True:
                    res += 1
        return res