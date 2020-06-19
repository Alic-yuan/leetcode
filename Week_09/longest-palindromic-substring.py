class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        max_length = 1
        start = 0

        dp = [[False]*size for _ in range(size)]

        for j in range(1, size):
            for i in range(j):
                if s[i] == s[j]:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    temp = j-i+1
                    if temp > max_length:
                        max_length = temp
                        start = i

        return s[start:start+max_length]