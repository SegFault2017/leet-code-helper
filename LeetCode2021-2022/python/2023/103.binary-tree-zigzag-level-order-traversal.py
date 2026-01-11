#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from re import A


class Solution:
    from collections import deque

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Strategy 1: BFS
        Runtime: O(n), where n is the number of nodes in the tree
        space:O(n), 

        Args:
            root (Optional[TreeNode]): the root of the tree

        Returns:
            List[List[int]]:  level traversal in zig zap order
        """
        if not root:
            return []

        queue = [root, None]
        result = []
        isLeft = True
        
        lvl_lst = deque([])

        while queue:
            node = queue.pop(0)
            if node:
                if isLeft:
                    lvl_lst.append(node.val)
                else:
                    lvl_lst.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                result.append(lvl_lst)
                lvl_lst = deque([])
                if queue:
                    queue.append(None)
                isLeft = not isLeft
        return result
# @lc code=end
