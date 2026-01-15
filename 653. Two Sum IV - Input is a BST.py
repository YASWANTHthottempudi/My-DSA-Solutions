# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.d={}
        self.i=0
        self.check=False
        def dfs(root):
            if not root or self.check:
                return
            if k-root.val in self.d:
                self.check=True
                return
            else:
                self.d[root.val]=1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.check
        
