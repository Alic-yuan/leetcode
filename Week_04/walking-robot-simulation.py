class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(map(tuple, obstacles))

        max_res = 0
        dir_index = 0
        x = 0
        y = 0
        for command in commands:
            if 1 <= command <= 9:
                for _ in range(command):
                    if (x+directions[dir_index][0], y+directions[dir_index][1]) in obstacles:
                        break
                    x += directions[dir_index][0]
                    y += directions[dir_index][1]
                max_res = max(max_res, x*x+y*y)
            elif command == -1:
                dir_index = (dir_index+1) % 4
            else:
                dir_index = (dir_index-1) % 4
        return max_res
