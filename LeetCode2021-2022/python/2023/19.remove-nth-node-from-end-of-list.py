#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def twoPass(self, head: Optional[ListNode], n: int) -> optional[ListNode]:
        count = 0
        dummy = ListNode(0, head)
        current = head
        size = 0
        while current:
            size += 1
            current = current.next

        size -= n
        current = dummy
        while size > 0:
            current = current.next
            size -= 1
        current.next = current.next.next
        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Strategy 1: 2 passes 
        Runtime:O(n) 
        Space:O(1)

        Args:
            head (Optional[ListNode]): the head of the linked list.
            n (int): the nth node from the end of the list.

        Returns:
            Optional[ListNode]: a linked list without the nth node from the 
            end of the list
        """
        return self.twoPass(head, n)
# @lc code=end
