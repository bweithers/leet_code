# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return
        lst = []
        #traverse the tree inorder and add it to an array
        def inorder(node):
            if not node: return
            if node.left: inorder(node.left)
            lst.append(node)
            if node.right: inorder(node.right)
            return node
        inorder(root)
        
        #print([x.val for x in lst])
        
        # Reconstruct the tree from our inorder array
        for i in range(len(lst)-1):
            curr = lst[i]
            curr.left = None
            curr.right = lst[i+1]
        # Make sure there are no cycles with old pointers
        lst[-1].left = None
        lst[-1].right = None
        return lst[0]
            