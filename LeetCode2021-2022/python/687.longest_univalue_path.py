# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node) -> int:
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            l, r = 0, 0 
            if node.left and node.val == node.left.val:
                l = left +1
            if node.right and node.val == node.right.val:
                r = right +1
            ans = max(ans, l + r)
            return max(l, r)
        dfs(root)
        return ans
            
                 
                
