# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        curr = head
        
        while curr:
            k = m
            d = n
            while curr and curr.next and k>1:
                curr = curr.next
                k-=1
            next_temp = curr.next
            while next_temp and d:
                next_temp = next_temp.next
                d-=1
            curr.next = next_temp
            curr = next_temp
            k=m
            d=n
        return dummy.head
