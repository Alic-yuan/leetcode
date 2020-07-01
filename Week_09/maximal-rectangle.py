class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        height = [0]* (cols+2)
        res = 0
        for i in range(rows):
            stack = []
            for j in range(cols):
                if matrix[i][j] == '1':
                    height[j+1] +=1
                else:
                    height[j+1] = 0
            for j in range(cols+2):
                while stack and height[j] < height[stack[-1]]:
                    temp = stack.pop()
                    res = max(res, (j-stack[-1] - 1)*height[temp])
                stack.append(j)
        return res