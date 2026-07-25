# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        if root.left and root.right:
            returned_left = self.levelOrder(root.left)
            returned_right = self.levelOrder(root.right)
            max_len = max(len(returned_left), len(returned_right))
            list_to_return = [[root.val]]
            for i in range(max_len):
                level = []
                if i < len(returned_left):
                    level += returned_left[i]
                if i < len(returned_right):
                    level += returned_right[i]
                list_to_return.append(level)
            return list_to_return
        if root.left:
            returned_left = self.levelOrder(root.left)
            return [[root.val]] + returned_left
        if root.right:
            returned_right = self.levelOrder(root.right)
            return [[root.val]] + returned_right
        return [[root.val]]