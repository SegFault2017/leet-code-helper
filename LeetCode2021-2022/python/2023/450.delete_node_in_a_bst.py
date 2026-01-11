# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, node):
        curr = node.right
        while curr.right:
            curr = curr.right
        return curr.val
    
    def predescessor(self, node):
        curr = node.left
        while curr.left:
            curr = curr.left
        return curr.val
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if (not root.right) and (not root.left):
                root = None
            elif root.right:
               root.val = self.successor(root)
               root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            return root
        
