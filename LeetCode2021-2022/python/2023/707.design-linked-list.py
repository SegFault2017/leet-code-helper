#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List


# @lc code=start

#
class Node:
    def __init__(self, val: int, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        string = str(self.val) + " -> "
        curr = self.next
        while curr and curr.next:
            string += str(curr.val) + " -> "
            curr = curr.next
        return string + str(curr.val)


# Doubly linked list
class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1, self.head)
        self.head.next = self.tail
        self.size = 0
        return

    def get(self, index: int) -> int:
        """
        Startegy: Doubly-linked list
        Runtime: O(min(k, n - k)), where k is the length from start to index
        Space:O(1)

        Args:
            index (int): the index

        Returns:
            int: value of node at index
        """
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        if index < self.size - index - 1:
            for _ in range(index+1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        """
        Startegy: Doubly-linked list
        Runtime: O(1)
        Space:O(1)

        Args:
            val (int): the insert value
        """
        pred, succ = self.head, self.head.next
        to_add = Node(val, pred, succ)
        pred.next = to_add
        succ.prev = to_add
        self.size += 1
        return

    def addAtTail(self, val: int) -> None:
        """
        Startegy: Doubly-linked list
        Runtime:  O(1)
        Space:O(1)

        Args:
            val (int): _description_
        """
        succ, pred = self.tail, self.tail.prev
        to_add = Node(val, pred, succ)
        pred.next = to_add
        succ.prev = to_add
        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Startegy: Doubly-linked list
        Runtime: O(min(k, n - k)), where k is the length from start to index
        Space:O(1)

        Args:
            index (int): positioin to insert value
            val (int): the value to be inserted

        Returns:
            _type_: _description_
        """
        if index < 0 or index > self.size:
            return -1
        elif index == 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return

        pred, succ = self.head, self.tail
        if index < self.size - index:
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        to_add = Node(val, pred, succ)
        pred.next = to_add
        succ.prev = to_add
        self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        """
        Startegy: Doubly-linked list
        Runtime: O(min(k, n - k)), where k is the length from start to index
        Space:O(1)

        Args:
            index (int): position to delete
        """
        if index < 0 or index >= self.size:
            return

        pred, succ = self.head, self.tail
        if index < self.size - index:
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        return

        # Your MyLinkedList object will be instantiated and called as such:
        # obj = MyLinkedList()
        # param_1 = obj.get(index)
        # obj.addAtHead(val)
        # obj.addAtTail(val)
        # obj.addAtIndex(index,val)
        # obj.deleteAtIndex(index)
        # @lc code=end
