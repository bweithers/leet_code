class Solution(object):
    def minCameraCover(self, root):
        self.cameras = 0
        self.seen = {None}
        
        def dfs(node,p):
            if not node: return
            dfs(node.left,node)
            dfs(node.right,node)
            
            if node.left not in self.seen or node.right not in self.seen:
                self.seen.update({p,node,node.left,node.right})
                self.cameras += 1
        
        dfs(root,None)
        return self.cameras + (root not in self.seen)
    