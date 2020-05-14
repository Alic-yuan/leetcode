class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        satisfy = 0
        i, j =0, 0
        while j < len(g) and i< len(s):
            if s[i] >= g[j]:
                i +=1
                j +=1
                satisfy +=1
            else:
                i +=1
        return satisfy