#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
from collections import defaultdict


class Node:
    def __init__(self):
        self.end = False
        self.children = defaultdict(Node)
        return


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """ insert a word into the trie
        Runtime:O(n)
        Space:O(1)

        Args:
            word (str): the word to be inserted
        """
        node = self.root
        for c in word:
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        """Determines whether word is in the trie or not
        Runtime:O(n)
        Space:O(1)

        Args:
            word (str): the word to look up

        Returns:
            bool: is word in the trie
        """
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return False
        return node.end

    def startsWith(self, prefix: str) -> bool:
        """Determines whether prefix is in the trie
        Runtime: O(n)
        Space: O(1)

        Args:
            prefix (str): the prefix to look for

        Returns:
            bool: is the prefix in the trie
        """
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if not node:
                return False
        return True

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
        # @lc code=end
