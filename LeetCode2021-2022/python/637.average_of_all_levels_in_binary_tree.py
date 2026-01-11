# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        output = []
        while q:
            n = len(q)
            total = 0
            for i in range(n):
                node = q.pop(0)
                total += float(node.val)
                for neigh in [node.left, node.right]:
                    if neigh:
                        q.append(neigh)
            output.append(total/n)
        return output
