class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        diffs = set()
        
        def dfs(node):
            if not node: return False
            if node.val in diffs: return True
            diffs.add(k-node.val)
            return dfs(node.right) or dfs(node.left)
        
        return dfs(root)