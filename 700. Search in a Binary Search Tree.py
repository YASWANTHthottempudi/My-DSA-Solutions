# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.res=None
        self.found=False
        def dfs(root):
            if not root:
                return None
            if root.val==val:
                self.res=root
            elif val>root.val:
                dfs(root.right)
            else:
                dfs(root.left)

        dfs(root)
        return self.res
        
