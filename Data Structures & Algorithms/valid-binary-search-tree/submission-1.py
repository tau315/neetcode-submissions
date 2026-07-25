# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        def isValid(node, left, right):
            if node is None:
                return True
            if left < node.val < right:
                return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
            return False
        return isValid(root, float("-inf"), float("inf"))
            