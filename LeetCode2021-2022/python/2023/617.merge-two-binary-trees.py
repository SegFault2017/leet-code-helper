#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def DFS(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Stratehy 2: DFS
        Runtime:O(max(n,m)), where n is the # of nodes in root1, m is the # of
        nodes in root2
        Space:O(max(n,m))

        Args:
            root1 (Optional[TreeNode]): root of tree1
            root2 (Optional[TreeNode]): root of tree2

        Returns:
            Optional[TreeNode]: merged binary tree
        """

        if not root1:
            return root2
        elif not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

    def BFS(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        q = [(root1, root2)]
        while q:
            node1, node2 = q.pop(0)
            if not node1 or not node2:
                continue

            node1.val += node2.val
            if not node1.left:
                node1.left = node2.left
            else:
                q.append((node1.left, node2.left))

            if not node1.right:
                node1.right = node2.right
            else:
                q.append((node1.right, node2.right))
        return root1

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.BFS(root1, root2)


# @lc code=end
