# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(root, left, right):
            if root is None:
                return True
            if root.val <= left or root.val >= right:
                return False
            return validBST(root.right, root.val, right) and validBST(root.left, left, root.val)
        return validBST(root, float('-inf'), float('inf'))

            