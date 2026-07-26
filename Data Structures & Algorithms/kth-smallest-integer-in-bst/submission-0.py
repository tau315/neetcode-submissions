# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root, ans):
            if root is None:
                return []
            return inorder(root.left, ans) + [root] + inorder(root.right, ans)

        inordertrav = inorder(root, [])
        return inordertrav[k - 1].val
