class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nh = len(grid)
        nl = len(grid[0])
        dp = grid
        for i in range(1,nh):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1,nl):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1,nh):
            for j in range(1,nl):
                dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])

        return dp[-1][-1]