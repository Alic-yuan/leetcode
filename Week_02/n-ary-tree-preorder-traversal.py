"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            childrens = temp.children
            if childrens:
                for c in childrens[::-1]:
                    stack.append(c)
        return res