class Solution:
    def countSubstrings(self, s: str) -> int:
        str_len = len(s)
        if str_len == 0 or s is None:
            return 0
        # 定义变量储存结果
        res = 0
        # 定义和初始化dp数组
        dp = [[False for _ in range(str_len)] for _ in range(str_len)]
        # 直接先给对角线赋值为True，防止出现 dp[i][j] = dp[i + 1][j - 1] 时，前值没有，例如，i=0，j=2的时候
        for i in range(str_len):
            dp[i][i] = True
        for j in range(str_len):
            # 因为对角线已经赋初始值，所以直接从i+1开始遍历
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