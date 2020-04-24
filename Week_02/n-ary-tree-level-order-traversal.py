"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        # res = []
        # queue = [root]
        # while queue:
        #     temp = []
        #     temp2 = []
        #     for q in queue:
        #         temp2.append(q.val)
        #         childs = q.children
        #         if childs:
        #             for c in childs:
        #                 temp.append(c)
        #     res.append(temp2)
        #     queue = temp
        # return res

        res = []
        def helper(node,depth):
            if not node:
                return res
            if len(res) <= depth:
                res.append([])
            res[depth].append(node.val)
            childs = node.children
            for c in childs:
                helper(c,depth+1)
        helper(root,0)
        return res