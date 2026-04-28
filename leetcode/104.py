# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # left = 0
        # right = 0
        def next_node(node):
            if not node:
                return 0
            left = next_node(node.left)
            right = next_node(node.right)

            return 1 + max(left, right)
        # print(root.val)

        return next_node(root)