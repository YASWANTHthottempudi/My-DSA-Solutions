class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0
        queue=[root]
        height=0
        while queue:
            n=len(queue)
            for i in range(n):
                ele=queue.pop(0)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                
            height+=1
        return height
