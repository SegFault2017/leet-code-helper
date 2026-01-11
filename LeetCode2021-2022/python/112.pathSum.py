# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node, target:int) -> bool:
        if not node:
            return False
        target -= node.val

            if not node.left and not node.right:
                return target == 0
            return dfs(node.left, target) or dfs(node.right, target)
        return dfs(root, targetSum)
    
    def bfs(node, targetSum:int) -> bool:
        if not node:
            return False
        stack = []
        curr = root
        target = targetSum

        while True:
            while curr:
                target-=curr.val
                stack.append((curr, target))
                curr = curr.left
            
            if not stack:
                break
            
            curr, target = stack.pop()
            if target == 0 and not curr.left and not curr.right:
                return True
            curr = curr.right
            
        return False 

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
       return self.dfs(root, targetSum) 
