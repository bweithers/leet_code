# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = []
        heapify(h)
        def dfs(node):
            if not node: return
            heappush(h, node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return nsmallest(k,h)[-1]