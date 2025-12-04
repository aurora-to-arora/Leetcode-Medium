# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def build(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            
            for root_val in range(start, end + 1):
                left_trees = build(start, root_val - 1)
                right_trees = build(root_val + 1, end)
                
                # Combine all left × right
                for L in left_trees:
                    for R in right_trees:
                        root = TreeNode(root_val)
                        root.left = L
                        root.right = R
                        all_trees.append(root)
            
            return all_trees

        return build(1, n)
