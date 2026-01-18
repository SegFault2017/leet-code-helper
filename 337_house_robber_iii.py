# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob_house(self, node):
        if node is None:
            return (0,0)
        
        # rob the current node:
        rob_left, dont_rob_left = self.rob_house(node.left)
        rob_right, dont_rob_right = self.rob_house(node.right)

        rob_count = node.val + dont_rob_left + dont_rob_right
        
        dont_rob_count = max(rob_left, dont_rob_left) + max(rob_right, dont_rob_right)
        return rob_count, dont_rob_count

    def rob(self, root: Optional[TreeNode]) -> int:
        rob_count, dont_rob_count =self.rob_house(root)
        return max(rob_count, dont_rob_count)
