class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        def mark(grid, i, j, nh, nl):
            if i < 0 or i > nh-1 or j<0 or j > nl-1 or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            mark(grid, i+1, j, nh, nl)
            mark(grid, i-1, j, nh, nl)
            mark(grid, i, j+1, nh, nl)
            mark(grid, i, j-1, nh, nl)
        nh = len(grid)
        nl = len(grid[0])
        land = 0
        for i in range(nh):
            for j in range(nl):
                if grid[i][j] == '1':
                    mark(grid, i, j, nh, nl)
                    land +=1
        return land