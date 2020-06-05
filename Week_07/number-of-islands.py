class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        def mark(i,j, nh, nl, grid):
            grid[i][j] = '0'
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for x,y in directions:
                nx = i+x
                ny = j+y
                if 0<=nx<nh and 0<=ny<nl and grid[nx][ny] !='0':
                    mark(nx,ny,nh,nl,grid)

        count = 0
        nh = len(grid)
        nl = len(grid[0])
        for i in range(nh):
            for j in range(nl):
                if grid[i][j] == '1':
                    mark(i,j,nh,nl,grid)
                    count +=1
        return count