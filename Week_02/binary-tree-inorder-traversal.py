# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        return res