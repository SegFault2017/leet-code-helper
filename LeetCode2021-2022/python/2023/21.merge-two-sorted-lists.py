#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from re import A
from typing import Optional


class Solution:
    def recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Strategy 2: Recursive
        Runtime: O(n)
        Space:O(n)

        Args:
            list1 (Optional[ListNode]): the head of list1
            list2 (Optional[ListNode]): the head of list2

        Returns:
            Optional[ListNode]: the head of the merged list
        """
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def iterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Strategy 1: Iterative
        Runtime:O(n)
        Space: O(n)

        Args:
            list1 (Optional[ListNode]): the head of list1
            list2 (Optional[ListNode]): the head of list2

        Returns:
            Optional[ListNode]: the head of the merged list
        """
        dummy = ListNode(-1)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursive(list1, list2)
        # @lc code=end
