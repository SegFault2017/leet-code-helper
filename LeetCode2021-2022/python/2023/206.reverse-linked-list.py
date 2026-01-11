#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Strategy 1: Iterative
        Runtime:O(n)
        Space:O(n)

        Args:
            head (Optional[ListNode]): the head of the linked list

        Returns:
            Optional[ListNode]: the head of the reversed linked list
        """
        prev, curr = None, head
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
        return prev

    def reverseListRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Strategy 2: Recurrsive
        Runtime:O(n)
        Space:O(n)

        Args:
            head (Optional[ListNode]): the head of the linked list

        Returns:
            Optional[ListNode]: the head of the reversed linked list
        """
        if not head or not head.next:
            return head

        next_tmp = self.reverseListRec(head.next)
        head.next.next = head
        head.next = None
        return next_tmp

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListRec(head)

# @lc code=end
