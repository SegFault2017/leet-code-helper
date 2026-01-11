#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """ Strategy 1: two pointers
        Runtime: O(n + m), where n is the length of a and b is the length of b
        Space: O(1)

        Args:
            headA (ListNode): the head of headA
            headB (ListNode): the head of headB

        Returns:
            Optional[ListNode]: the intersected node
        """
        a, b = headA, headB

        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next

        return a

# @lc code=end
