# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def search_node(node):
            if not node:
                return None
            if node.val == val:
                return node

            left = search_node(node.left)
            if left:
                return left
            # search_node(node.right)
            right = search_node(node.right)
            if right:
                return right

            return None
            
        return search_node(root)