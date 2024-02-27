# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # what is the distance between two nodes? -- the number of edges
        # when does the diameter not pass thru the root?
        # the distance from any node to its child, is the depth
        # the max at any node is max(left) + max(right)

        self.max_diameter = 0
        
        def dfs(node):
            if not node: 
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.max_diameter = max(self.max_diameter, left+right)
            return 1 + max(left, right)
            
        dfs(root)
        return self.max_diameter