#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
from collections import defaultdict


class Node:
    def __init__(self) -> None:
        self.end = False
        self.children = defaultdict(Node)


class Trie:
    def __init__(self) -> None:
        self.root = Node()
        return

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
        node.end = True

    def getPrefix(self, word: str) -> str:
        node = self.root
        result = ""
        for c in word:
            node = node.children.get(c)
            if not node:
                return word
            result += c
            if node.end:
                return result
        return result


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """ Strategy1: trie
        RunTime:O(n m), where n is length of a word with max length, m is the 
        length of max(dictionary, sentence)
        Space(n m)

        Args:
            dictionary (List[str]): list of root words
            sentence (str): the sentence to replace

        Returns:
            str: mofified sentence
        """
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = sentence.split(" ")
        result = []
        for word in words:
            result.append(trie.getPrefix(word))
        return " ".join(result)
        # @lc code=end
