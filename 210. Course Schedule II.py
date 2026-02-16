class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(n)]
        indeg=[0]*n
        res=[]
        
        for val in prerequisites:
            course=val[0]
            prereq= val[1]
            adj[prereq].append(course)
            indeg[course]+=1
        
        queue=deque()
        for i in range(n):
            if indeg[i]==0:
                queue.append(i)

        while queue:
            cur=queue.popleft()
            res.append(cur)

            for nextcourse in adj[cur]:
                print(nextcourse)
                indeg[nextcourse]-=1
                if indeg[nextcourse]==0:
                    queue.append(nextcourse)

        if len(res)==n:
            return res
        else:
            return []
        
