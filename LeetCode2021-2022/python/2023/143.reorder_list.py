# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, node):
        prev, curr = None, node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return None
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        first, second = head, self.reverseLL(slow)
        
        while second.next:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp
            
        return
            

        

