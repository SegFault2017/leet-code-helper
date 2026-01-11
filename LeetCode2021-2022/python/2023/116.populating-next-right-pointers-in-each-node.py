#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


from typing import Optional


class Solution:
    def BFS(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """ Strategy 1: BFS
        Runtime: O(n), where n is the # of nodes in the tree
        Space:O(n)

        Returns:
            [Node]: the root of the connected tree
        """
        if not root:
            return root

        q = [root]

        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                if i < size - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
        return root

    def previousEstablishedNextPointer(self, root: 'Optional[Node]') \
            -> 'Optional[Node]':
        """Strategy 2: Using previousEstablishedNextPointer
        Runtime:O(n)
        Space:O(1)

        Returns:
            [type]: the connected root of the tree
        """
        if not root:
            return root

        left_most = root

        while left_most.left:
            head = left_most
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            left_most = left_most.left
        return root

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        return self.previousEstablishedNextPointer(root)
        # @lc code=end
