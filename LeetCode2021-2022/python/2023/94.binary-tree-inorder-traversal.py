#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self, root: 'Optional[Node]', res: List[int]) -> None:
        """Strategy1: DFS
        Runtime:O(h), where h is the height of the tree
        Space:O(h), where h is the height of the tree

        Args:
            root (Optional[Node]): the root of the tree
            res (List[int]):[]

        Returns:
            _type_: _description_
        """
        if not root:
            return None

        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
        return

    def iterative(self, root: 'Optional[Node]', res: List[int]) -> None:
        """ Strategy 1: BFS
        Space:O(h)
        Runtime:O(h), where h is the height of the tree

        Args:
            root (Optional[Node]): the root of the tree
            res (List[int]): in order traversal of the tree
        """
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr)
            curr = curr.right
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Strategy1: DFS
        Runtime:O(h), where h is the height of the tree
        Space:O(h), where h is the height of the tree

        Args:
            root (Optional[Node]): the root of the tree
            res (List[int]):[]

        Returns:
            _type_: _description_
        """
        res = []
        self.dfs(root, res)
        return res

        # @lc code=end
