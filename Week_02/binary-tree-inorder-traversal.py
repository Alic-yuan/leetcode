# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(root, 'white')]
        while stack:
            node, clolor = stack.pop()
            if not node:
                continue
            if clolor == 'white':
                stack.append((node.right, 'white'))
                stack.append((node, 'gray'))
                stack.append((node.left, 'white'))
            else:
                res.append(node.val)
        return res