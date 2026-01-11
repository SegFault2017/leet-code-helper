# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node1, node2) -> bool:
        if not node1 and not node2:
            return True
        isSymmetric = node1.left == node2.right and node1.right == node2.left
        return isSymmetric and dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
    
    def bfs(self, root) -> bool:
        if not root:
            return True
        q = [roo.left, root.right]
        while q:
            node1 = q.pop(0)
            node2 = q.pop(0)
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)
        return True
            
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)
        """ 
        
        return self.bfs(root)
        
        
        
