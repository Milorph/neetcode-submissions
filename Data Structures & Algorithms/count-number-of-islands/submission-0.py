class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        count = 0

        def explore( matrix, row, col, visited):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] == '0' or visited[row][col] == True:
                return

            visited[row][col] = True
            explore(matrix,row + 1, col, visited)
            explore(matrix,row, col + 1, visited)
            explore(matrix,row - 1, col, visited)
            explore(matrix,row, col - 1, visited)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] == False:
                    count += 1
                    explore(grid, i , j, visited)
        
        return count
        
        
        