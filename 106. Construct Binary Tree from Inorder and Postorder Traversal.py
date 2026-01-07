# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inmap={}
        for i in range(len(inorder)):
            inmap[inorder[i]]=i

        def build(instart,inend, poststart,postend):
            if instart>inend:
                return None

            rootval=postorder[postend]
            index=inmap[rootval]
            leftsize=index-instart

            root=TreeNode(rootval)
            root.left= build(instart,index-1,poststart, poststart+leftsize-1)
            root.right = build(index+1, inend, poststart+leftsize, postend-1 )
            return root
        
        return build(0,len(inorder)-1,0, len(postorder)-1)

            
        
