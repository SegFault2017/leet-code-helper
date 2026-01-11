# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        prev, curr = None, head
        while left > 1:
            prev = curr
            curr = curr.next
            left -=1
            right-=1

        con, tail = prev, curr

        while right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            right-=1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr
        return tail


        
            
        
