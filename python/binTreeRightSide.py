class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        s = {}
        def rdfs(node,d):
            if not node: return
            if d not in s: s[d] = node.val
            rdfs(node.right,d+1)
            rdfs(node.left,d+1)
            
            
        rdfs(root,0)
        return [s[i] for i in range(max(s)+1)] if s else []