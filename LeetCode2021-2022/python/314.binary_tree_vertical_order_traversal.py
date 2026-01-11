# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        col_table = defaultdict(list)
        min_col = 0
        max_col = 0
        q = [(root, 0)]
        
        while q:
            node, index = q.pop(0)
            col_table[index].append(node.val)
            if node.left:
                min_col-=1
                q.append((node.left, index-1))
            if node.right:
                max_col+=1
                q.append((node.right, index+1))
        
        output = []
        for i in range(min_col, max_col+1):
            if i in col_table:
                output.append(col_table[i])
        return output
            
        
