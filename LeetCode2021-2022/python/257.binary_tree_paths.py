# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        output = []
        def dfs(node, p:str) -> None:
            if not node.left and not node.right:
                output.append(p)
                return
            if node.left:
                dfs(node.left, p + "->" + str(node.left.val))
            if node.right:
                dfs(node.right, p+ "->" +str(node.right.val))
            return
        dfs(root, str(root.val))
        return output
        
                
        
