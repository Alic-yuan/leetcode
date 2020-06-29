class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        queue = [(0,0,1)]
        visited = set()
        while queue:
            i,j,step = queue.pop(0)
            if i==n-1 and j==n-1:
                return step
            directions = [(-1,-1), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]
            for x,y in directions:
                nx = i+x
                ny = j+y
                if (nx,ny) in visited:
                    continue
                visited.add((nx,ny))
                if 0<=nx<n and 0<=ny<n and grid[nx][ny] !=1:
                    queue.append((nx,ny,step+1))
        return -1