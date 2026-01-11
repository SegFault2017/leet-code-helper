# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterative(self, root):
        node = root
        while node:
            if node.val < val:
                if not node:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if not node:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)
                
        return
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        
        return root
        
