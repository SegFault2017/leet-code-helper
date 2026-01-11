# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def stops_at_second_half(self, node):
        slow = fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, node):
        prev, curr = None, node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        second_half = self.stops_at_second_half(head)
        reversed = self.reverseList(second_half.next)

        curr = head
        while reversed:
            if curr.val != reversed.val:
                return False
            curr = curr.next
            reversed = reversed.next
        return True
        
        
        
