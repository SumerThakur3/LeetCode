from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):

        rows = len(maze)
        cols = len(maze[0])

        queue = deque()

        # row, column, steps
        queue.append((entrance[0], entrance[1], 0))

        # Keep track of visited cells
        visited = set()
        visited.add((entrance[0], entrance[1]))

        directions = [
            (1, 0),    # down
            (-1, 0),   # up
            (0, 1),    # right
            (0, -1)    # left
        ]

        while queue:

            row, col, steps = queue.popleft()

            for dr, dc in directions:

                newRow = row + dr
                newCol = col + dc

                # 1. Is it inside the maze?
                if newRow < 0 or newRow >= rows:
                    continue

                if newCol < 0 or newCol >= cols:
                    continue

                # 2. Is it a wall?
                if maze[newRow][newCol] == '+':
                    continue

                # 3. Have we already visited it?
                if (newRow, newCol) in visited:
                    continue

                # Mark visited
                visited.add((newRow, newCol))

                # 4. Is it an exit?
                if (newRow == 0 or 
                    newRow == rows - 1 or
                    newCol == 0 or
                    newCol == cols - 1):

                    return steps + 1

                # 5. Otherwise add it to queue
                queue.append((newRow, newCol, steps + 1))

        return -1