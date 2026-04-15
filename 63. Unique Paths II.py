class Solution:
    def uniquePathsWithObstacles(self, l: List[List[int]]) -> int:
        m=len(l)
        n=len(l[0])
        arr=[[-1 for _ in range(n)] for _ in range(m)]
        if l[m-1][n-1]==1:
            return 0
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n or l[i][j]==1:
                return 0
            if arr[i][j]!=-1:
                return arr[i][j]

            down=dfs(i,j+1)
            right=dfs(i+1,j)
            arr[i][j]=down+right
            return arr[i][j]
        return dfs(0,0)
        
