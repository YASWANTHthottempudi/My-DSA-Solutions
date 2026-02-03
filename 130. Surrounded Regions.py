class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row,col,board,visited):
            visited[row][col]=1
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            
            for nr, nc in directions:
                dr,dc = nr+row, nc+col
                if 0<=dr<=len(board)-1 and 0<=dc<=len(board[0])-1 and visited[dr][dc]==0 and board[row][col]=="O":
                    dfs(dr,dc,board,visited)
        row=len(board)
        col = len(board[0])
        visited=[]

        for i in range(row):
            visited.append([0]*col)

        for j in range(col):
            if board[0][j]=="O" and visited[0][j]==0:
                dfs(0,j,board,visited)
            if board[row-1][j]=="O" and visited[row-1][j]==0:
                dfs(row-1,j,board,visited)
        
        for i in range(row):
            if board[i][0]=="O" and visited[i][0]==0:
                dfs(i,0,board,visited)
            if board[i][col-1]=="O" and visited[i][col-1]==0:
                dfs(i,col-1,board,visited)
        print(visited)
        for i in range(row):
            for j in range(col):
                if board[i][j]=="O" and visited[i][j]==0:
                    board[i][j]="X"


        
