# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        q = [(root,0)]
        
        while q:
            n = len(q)
            _, lvl_idx = q[0]
            
            for _ in range(n):
                node, idx = q.pop(0)
                if node.left:
                    q.append((node.left, 2 * idx))
                if node.right:
                    q.append((node.right, (2 * idx) + 1))
            max_width = max(max_width, (idx - lvl_idx) + 1)
        return max_width
        
