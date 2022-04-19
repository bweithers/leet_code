# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        a = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            a.append(node)
            inorder(node.right)
        
        inorder(root)
        for n1,n2 in zip(a, sorted(a, key=lambda x: x.val)):
            if n1.val != n2.val: 
                n1.val, n2.val = n2.val, n1.val
                break
        return root
                