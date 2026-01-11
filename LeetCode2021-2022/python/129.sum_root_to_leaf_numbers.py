# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, p:str) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return int(p + str(node.val))
            
            return dfs(node.left, p + str(node.val)) + dfs(node.right, p+str(node.val))
        return dfs(root, "")
            
            
