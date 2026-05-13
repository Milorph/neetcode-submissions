class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        def addCell(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == -1 or (row, col) in visited:
                return
            q.append([row, col])
            visited.add((row, col))
        
        distance = 0

        while q:

            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = distance
                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)
            
            distance += 1





            
           

