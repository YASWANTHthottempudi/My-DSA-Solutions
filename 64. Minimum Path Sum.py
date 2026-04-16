class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        m=len(grid)
        arr = [[-1 for _ in range(n)] for _ in range(m)]
        def dfs(i,j):
            if i>=len(grid) or j>=len(grid[0]):
                return float('inf')
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]
            if i<m-1 and arr[i+1][j]!=-1:
                down= arr[i+1][j]
            else:
                down = dfs(i+1,j)
            if j<n-1 and arr[i][j+1]!=-1:
                right = arr[i][j+1]
            else:
                right = dfs(i,j+1)
            arr[i][j]= grid[i][j]+min(down,right)
            return arr[i][j]

        return dfs(0,0)
