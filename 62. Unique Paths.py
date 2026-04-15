class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[-1 for _ in range(n)] for _ in range(m)]
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if arr[i][j]!=-1:
                return arr[i][j]
            down=dfs(i+1,j)
            right= dfs(i,j+1)
            arr[i][j]=down+right
            return arr[i][j]


        return dfs(0,0)
        
