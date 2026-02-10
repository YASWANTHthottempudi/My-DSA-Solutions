# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        def build(l,r):
            if l>r:
                return None
            mid=(l+r)//2
            L=build(l,mid-1)
            R = build(mid+1, r)
            Node= TreeNode(arr[mid])
            Node.left = L
            Node.right = R
            return Node

        dfs(root)
        return build(0,len(arr)-1)

        
