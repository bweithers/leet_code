class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ls = {}
        
        def dfs(node,l):
            if not node: return
            if l not in ls: ls[l] = []
            ls[l].append(node.val)
            dfs(node.left,l+1)
            dfs(node.right,l+1)
        dfs(root,0)
        return [ls[i] for i in range(max(ls)+1)] if ls else []
            