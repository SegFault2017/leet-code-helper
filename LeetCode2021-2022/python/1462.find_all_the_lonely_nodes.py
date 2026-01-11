# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        q = [root]
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                count = 0
                for neigh in [node.left, node.right]:
                    count += (neigh != None)
                    if neigh:
                        q.append(neigh)
                if count == 1:
                     for neigh in [node.left, node.right]:
                            if neigh:
                                output.append(neigh.val)
        return output
