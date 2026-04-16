class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = []
        for i in range(m):
            dp.append([None] * len(triangle[i]))

        def dfs(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]

            if dp[i][j] is not None:
                return dp[i][j]

            down = triangle[i][j] + dfs(i + 1, j)
            dright = triangle[i][j] + dfs(i + 1, j + 1)

            dp[i][j] = min(down, dright)
            return dp[i][j]

        return dfs(0, 0)
