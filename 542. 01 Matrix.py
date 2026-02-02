class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        row,col = len(mat),len(mat[0])
        q = collections.deque()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=float('inf')

        while q:
            rows,cols = q.popleft()

            for dr, dc in directions:
                nr, nc = rows+dr, cols+dc

                if nr>=0 and nr<row and nc>=0 and nc<col and mat[nr][nc]>mat[rows][cols]+1:
                    mat[nr][nc] = mat[rows][cols]+1
                    q.append((nr,nc))


        return mat

        
