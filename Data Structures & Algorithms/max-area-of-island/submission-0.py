class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        islands = 0
        def explore(row, col, matrix, visited):
            
            if(row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] == 0 or visited[row][col] == True):
                return 0
            
            visited[row][col] = True
            area = 1
            area += explore(row + 1, col, matrix, visited)
            area += explore(row - 1, col, matrix, visited)
            area += explore(row, col + 1, matrix, visited)
            area += explore(row, col - 1, matrix, visited)
            
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == False:
                    islands = max(islands, explore(i,j,grid,visited))
        
        return islands