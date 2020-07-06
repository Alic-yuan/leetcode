class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        heights = [0] + heights + [0]
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                high = stack.pop()
                res = max(res, heights[high] * (i - stack[-1] - 1))
            stack.append(i)
        return res