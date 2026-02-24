# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(root,s):
            if not root:
                return
            s+=str(root.val)
            if not root.left and not root.right:
                self.ans+=int(s,2)
                return
            dfs(root.left,s)
            dfs(root.right,s)

        s=""
        dfs(root,s)
        return self.ans
 
