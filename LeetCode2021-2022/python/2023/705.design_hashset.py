class MyHashSet:

    def __init__(self):
        self.num_buckets = 769
        self.buckets = [Buckets() for _ i in range(self.num_buckets)]

    def _hash(self, key:int) -> int:
        return key % self.num_buckets
    
    def add(self, key: int) -> None:
        self.buckets[self._hash(key)].add2Front(key)
        return

    def remove(self, key: int) -> None:
        self.buckets[self._hash(key)].remove(key)
        return

    def contains(self, key: int) -> bool:
        self.buckets[self._hash(key)].exists(key)
        return

class LNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Bucket:
    def __init__(self):
        self.head = LNode(0)

    def add2Front(self, val):
        if not self.exists(val):
            newNode = LNode(val, self.head.next)
            self.head.next = newNode
        return
    
    def remove(self, val):
        prev = self.head
        curr = self.head.next

        while curr:
            if curr.val == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        return

    def exists(self, val):
        curr = self.head.next
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
