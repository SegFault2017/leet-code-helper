# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def dfs(node, parent:int) -> bool:
            nonlocal count
            if not node:
                return True

            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            if (not (left and right)):
                return False

            count +=1
            return node.val == parent
        dfs(root, 0)
        return count
