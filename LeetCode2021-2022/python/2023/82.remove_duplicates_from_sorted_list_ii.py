# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(-101, head)
        pred = dummy
        curr = head

        while curr:
            if curr.next and curr.next.val == curr.val:
                while curr.next and curr.next.val == curr.val:
                    curr = curr.next
                pred.next = curr.next
            else:
                pred = pred.next
            curr = curr.next
        return dummy.next
