from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_len=len(grid)
        col_len=len(grid[0])

        queue=deque()
        fresh=0

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col]==2:
                    queue.append((row,col))
                elif grid[row][col]==1:
                    fresh+=1
        
        directions=[
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        minutes=0

        while queue and fresh > 0:
            for i in range(len(queue)):
                row,col=queue.popleft()

                for dr , dc in directions:
                    newrow = row+dr
                    newcol = col+dc

                    if newrow < 0 or newrow >= row_len:
                        continue
                    if newcol < 0 or newcol >= col_len:
                        continue
                    if grid[newrow][newcol] != 1:
                        continue            
                    
                    grid[newrow][newcol]=2
                    fresh-=1

                    queue.append((newrow,newcol))

            minutes+=1

        if fresh > 0 :
            return -1

        return minutes        