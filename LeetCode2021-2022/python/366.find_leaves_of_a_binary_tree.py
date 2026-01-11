# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def __init__(self):
        self.pairs = defaultdict(list)
        return

    def depthOfTree(self, node) -> int:
        if not node:
            return 0
        l_depth = self.depthOfTree(node.left)
        r_depth = self.depthOfTree(node.right)
        depth = max(l_depth, r_depth) + 1
        self.pairs[depth].append(node.val)
        return depth

    def dfs(self, root, parents, in_degrees) -> None:
        if not root:
            return 
        in_degrees[root] = 0
        if root.left:
            parents[root.left] = root
            in_degrees[root] +=1
            self.dfs(root.left, parents, in_degrees)
        if root.right:
            parents[root.right] = root
            in_degrees[root] +=1 
            self.dfs(root.right, parents, in_degrees)
        return

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        output =[]
        self.depthOfTree(root)
        
        for _, val in self.pairs.items():
            output.append(val)
        return output
        """
        parents = defaultdict(TreeNode)
        in_degrees = defaultdict(int)
        q = []
        output = []

        for node, val in in_degrees.items():
            if val == 0:
                q.append(node)
        while q:
            leaves = []
            n = len(q)
            for _ in range(n):
                at = q.pop(0)
                if at != root:
                    parent = parents[at]
                    in_degrees[parent] -=1
                    if in_degrees[parent] == 0:
                        q.append(parent)
                leaves.append(at)
            output.append(leaves)
        
        return output
        
