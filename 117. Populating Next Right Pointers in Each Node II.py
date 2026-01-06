class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = deque([root])

        while q:
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                
                # Connect current node to next node in same level
                if i < size - 1:
                    node.next = q[0]  # Next node is at front of queue
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root

