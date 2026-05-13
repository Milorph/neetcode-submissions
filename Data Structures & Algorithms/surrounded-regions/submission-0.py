class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col):
            if min(row, col) < 0 or row >= ROWS or col >= COLS or board[row][col] != "O":
                return
            
            board[row][col] = "T"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

        