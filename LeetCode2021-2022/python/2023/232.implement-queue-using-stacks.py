#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            size = len(self.s1)
            while size > 0:
                self.s2.append(self.s1.pop())
                size -= 1
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            n = len(self.s2)
            return self.s2[n-1]
        return self.front

    def empty(self) -> bool:
        return not self.s1 and not self.s2

        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()
        # @lc code=end
