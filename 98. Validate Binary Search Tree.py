# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.check=True
        self.l=[]
        def dfs( root):
            if not root or not self.check:
                return
            
            dfs(root.left)
            if self.l and self.l[-1]>=root.val:
                self.check = False
            else:
                self.l.append(root.val)
            dfs(root.right)

        dfs(root)
        return self.check
        
