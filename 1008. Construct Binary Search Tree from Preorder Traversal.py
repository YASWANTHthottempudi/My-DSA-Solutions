# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, i, upper):
            if i[0]==len(preorder) or preorder[i[0]]>=upper:
                return None
            root = TreeNode(preorder[i[0]])
            i[0]+=1
            root.left = dfs(preorder, i, root.val)
            root.right = dfs(preorder, i, upper)
            return root

        i=[0]
        return dfs(preorder,i, float("inf"))
        
