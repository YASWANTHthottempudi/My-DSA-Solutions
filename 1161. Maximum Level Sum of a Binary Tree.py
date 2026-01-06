# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=-999999999
        self.d={}
        self.ans=None
        def dfs(root,level):
            if not root:
                return 
            if level in self.d.keys():
                self.d[level]+=root.val
            else:
                self.d[level]=root.val
            if self.d[level]>self.maxi:
                self.maxi=self.d[level]
                self.ans=level
            
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        dfs(root,1)
        return self.ans
