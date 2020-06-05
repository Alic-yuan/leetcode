class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(cur, left, right, n):
            if len(cur) == 2*n:
                res.append(cur)
                return
            if left < n:
                helper(cur+'(', left+1, right, n)
            if right < left:
                helper(cur+')', left, right+1, n)
        helper('', 0, 0, n)
        return res