"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        diameter = 0
        visited = set()
        
        def dfs(node) -> int:
            if not node:
                return 0
            nonlocal diameter
            visited.add(node)
            
            longest1, longest2, distance =0,0,0
            
            for child in node.children:
                if child not in visited:
                    distance = dfs(child) + 1
                
                if longest1 < distance:
                    longest1, longest2 = distance, longest1
                elif longest2 < distance:
                    longest2 = distance
                
                diameter = max(diameter, longest1 + longest2)
            return longest1
        dfs(root)
        return diameter
