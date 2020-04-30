class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_res = 0
        stack = [-1]
        for i in range(len(heights)):
            while len(stack) > 1 and heights[i] < heights[stack[-1]]:
                max_res = max(max_res, heights[stack.pop()] * (i-stack[-1]-1))
            stack.append(i)
        for _ in range(len(stack)-1):
            max_res = max(max_res, heights[stack.pop()] * (len(heights)-1-stack[-1]))
        return max_res