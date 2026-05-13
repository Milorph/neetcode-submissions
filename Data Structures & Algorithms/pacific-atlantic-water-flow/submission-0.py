class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        
        def explore(row, col, visited, prevHeight):
            if min(row,col) < 0 or row >= ROWS or col >= COLS or ((row,col)) in visited or heights[row][col] < prevHeight:
                return
            
            visited.add((row, col))
            explore(row + 1, col, visited, heights[row][col])
            explore(row - 1, col, visited, heights[row][col])
            explore(row, col + 1, visited, heights[row][col])
            explore(row, col - 1, visited, heights[row][col])
            
        for row in range(ROWS):
            explore(row, 0, pacific, heights[row][0])
            explore(row, COLS - 1, atlantic, heights[row][COLS - 1])
        
        for col in range(COLS):
            explore(0, col, pacific, heights[0][col])
            explore(ROWS - 1, col, atlantic, heights[ROWS - 1][col])
        
        res = []

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row,col])
        
        return res
