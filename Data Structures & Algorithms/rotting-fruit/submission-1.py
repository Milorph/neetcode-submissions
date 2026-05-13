class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
        
        
        def addFruit(r,c):
            nonlocal fresh
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 2 or grid[r][c] == 0 or (r,c) in visited:
                return
            fresh -= 1
            q.append([r,c])
            visited.add((r,c))

        if fresh == 0:
            return 0
        
        time = -1
        while q:

            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = 2
                addFruit(row + 1, col)
                addFruit(row - 1, col)
                addFruit(row, col + 1)
                addFruit(row, col - 1)
            time += 1

        if fresh > 0:
            return - 1
        return time
