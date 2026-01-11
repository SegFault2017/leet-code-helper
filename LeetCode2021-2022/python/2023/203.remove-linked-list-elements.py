#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """Strategy 1: One pass
        Runtime: O(n)
        Space:O(1)

        Args:
            head (Optional[ListNode]): the head of the linked list
            val (int): the node with the same value are removed

        Returns:
            Optional[ListNode]: the head of the linked list.
        """
        dummy = ListNode(-1, head)
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next

# @lc code=end
