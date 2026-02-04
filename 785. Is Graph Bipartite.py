class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [-1] * len(graph)

        def dfs(node, color):
            visited[node] = color
            for adj in graph[node]:
                if visited[adj] == -1:
                    dfs(adj, 1 - color)

        # handle disconnected graphs
        for i in range(len(graph)):
            if visited[i] == -1:
                dfs(i, 0)

        # final validation
        for i in range(len(graph)):
            for j in graph[i]:
                if visited[i] == visited[j]:
                    return False

        return True
