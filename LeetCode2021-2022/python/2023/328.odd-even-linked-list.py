#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Strategy 1: 2 pointers
        Runtime: O(n), where n is the length of the linked list
        Space: O(1)

        Args:
            head (Optional[ListNode]): the head of the list

        Returns:
            Optional[ListNode]: the head of the modified linked list
        """
        if not head:
            return None
        odd, evenHead, even = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head

# @lc code=end
