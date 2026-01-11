#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """returns the middle node of the given linked list head
        Runtime:O(n) 
        Space:O(1)

        Args:
            head (Optional[ListNode]): the head of the linked list

        Returns:
            Optional[ListNode]: the middle node
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# @lc code=end
