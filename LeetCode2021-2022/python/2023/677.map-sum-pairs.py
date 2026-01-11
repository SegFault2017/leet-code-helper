#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#

# @lc code=start
from collections import defaultdict


class Node:
    def __init__(self) -> None:
        self.val = 0
        self.children = defaultdict(Node)


class MapSum:

    def __init__(self):
        self.root = Node()
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        """
       Runtime:O(n), where n is the length of key
       Space:O(1)

        Args:
            key (str): key to be inserted to trie
            val (int): the value assocaite to the key
        """
        delta = val - self.map[key]
        node = self.root
        self.map[key] = val
        for c in key:
            node = node.children[c]
            node.val += delta

    def sum(self, prefix: str) -> int:
        """
        Runtime:O(n) where n is the length of key
        Space:O(1)

        Args:
            prefix (str): the prefix

        Returns:
            int: summation of all value of keys that starts with prefix
        """
        node = self.root
        for c in prefix:
            node = node.children[c]
            if not node:
                return 0
        return node.val

        # Your MapSum object will be instantiated and called as such:
        # obj = MapSum()
        # obj.insert(key,val)
        # param_2 = obj.sum(prefix)
        # @lc code=end
