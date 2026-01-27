from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        if rows==0:
            return -1
        cols=len(grid[0])

        fresh=0

        rotten=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1

        time = 0

        while rotten and fresh>0:
            time+=1
            for _ in range(len(rotten)):
                x,y = rotten.popleft()

                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx, yy = x+dx, y+dy
                    if xx<0 or xx==rows or yy<0 or yy==cols:
                        continue
                    if grid[xx][yy]==0 or grid[xx][yy]==2:
                        continue
                    fresh-=1
                    rotten.append((xx,yy))
                    grid[xx][yy]=2

        return time if fresh==0 else -1

        
