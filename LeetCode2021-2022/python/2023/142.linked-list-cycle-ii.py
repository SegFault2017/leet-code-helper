#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Strategy 1: Tortoise and hare
        Runtime:O(n), where n is the length of the linked list
        Space: O(1)


        Args:
            head (Optional[ListNode]): the head of the linked list

        Returns:
            Optional[ListNode]: the intersected node
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast

        # @lc code=end
