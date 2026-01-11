# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [(root, 0)]
        max_width = 0
        
        while q:
            n = len(q)
            _, first_idx = q[0]
            for _ in range(n):
                node, idx = q.pop(0)
                if node.left:
                    q.append((node.left,2 * idx))
                if node.right:
                    q.append((node.right, 2 * idx +1))
            max_width = max(max_width, (idx - first_idx)+1)
        return max_width

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        first_idx = {}
        max_width = 0
        
        def dfs(node:Optional[TreeNode], depth:int, idx:int) -> None:
            nonlocal max_width
            if not node:
                return

            if depth not in first_idx:
                first_idx[depth] = idx
            
            max_width = max(max_width, (idx - first_idx) +1)
            dfs(node.left, depth +1, 2 * idx)
            dfs(node.right, depth +1, 2 * idx +1)
            return
        dfs(root, 0,0)
        return max_width
        
