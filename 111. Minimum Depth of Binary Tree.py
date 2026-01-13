# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.mini=9999999
        def dfs(root,level):
            if not root:
                return 0

            if root.left is None and root.right is None:
                self.mini=min(self.mini, level)   


            lh= dfs(root.left, level+1)
            rh= dfs(root.right,level+1)


            return 1+min(lh,rh)
        dfs(root,1)
        return self.mini
        
