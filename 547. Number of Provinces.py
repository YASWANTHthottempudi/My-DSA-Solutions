class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        
        if not M:
            return 0
        
        n = len(M)
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(i)

        visited= [0]*n

        def dfs(u):
            for v in graph[u]:
                if visited[v]==0:
                    visited[v]=1
                    dfs(v)

        count=0

        for i in range(n):
            if visited[i]==0:
                count+=1
                visited[i]=1
                dfs(i)

        return count
