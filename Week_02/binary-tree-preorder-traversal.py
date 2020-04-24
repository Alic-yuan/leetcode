# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            left_child = temp.left
            right_child = temp.right
            if right_child:
                stack.append(right_child)
            if left_child:
                stack.append(left_child)
        return res