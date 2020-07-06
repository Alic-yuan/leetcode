# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [(root, 0)]
        while queue:
            level = queue[0][1]
            temp = []
            temp2 = []
            for node, level in queue:
                temp.append(node.val)
                if node.left:
                    temp2.append((node.left, level+1))
                if node.right:
                    temp2.append((node.right, level+1))
            if level % 2 == 0:
                res.append(temp)
            else:
                res.append(temp[::-1])
            queue = temp2
        return res