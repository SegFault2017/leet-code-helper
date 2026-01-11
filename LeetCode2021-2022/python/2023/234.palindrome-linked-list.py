#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseLL(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, node
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """Strategy 1: 2 pointers
        Runtime: O(n)
        Space: O(n)

        Args:
            head (Optional[ListNode]): the head of the linked list

        Returns:
            bool: whether the linked list is a palindrome
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverse = self.reverseLL(slow)
        curr = head
        while curr and reverse:
            if curr.val != reverse.val:
                return False
            curr = curr.next
            reverse = reverse.next
        return True
        # @lc code=end
