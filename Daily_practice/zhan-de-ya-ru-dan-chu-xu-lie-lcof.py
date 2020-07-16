class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for j in pushed:
            stack.append(j)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack