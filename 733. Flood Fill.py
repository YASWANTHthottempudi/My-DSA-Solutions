class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row=len(image)
        col = len(image[0])
        start = image[sr][sc]
        if start == color:
            return image
        
        q=deque([(sr,sc)])
        image[sr][sc]=color

        while q:
            r,c = q.popleft()

            for dc, dr in ((-1,0), (1,0), (0,-1),(0,1)):
                nr, nc = r+dr , c+dc

                if 0<=nr<row and 0<=nc<col and image[nr][nc]==start:
                    image[nr][nc]=color
                    q.append((nr,nc))

        return image
        
