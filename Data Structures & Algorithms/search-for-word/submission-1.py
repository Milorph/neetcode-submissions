class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == word[0]:
                    if self.dfs(visited, i, j, 0, word, board):
                        return True
        
        return False
    
    def dfs(self, visited, row, col, index, word, board):
        if index == len(word):
            return True
        
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
            return
        
        
        if (row, col) in visited:
            return False

        visited.add((row,col))
        if(
        self.dfs(visited, row + 1, col, index + 1, word, board) or
        self.dfs(visited, row, col + 1, index + 1, word, board) or
        self.dfs(visited, row - 1, col, index + 1, word, board) or
        self.dfs(visited, row, col - 1, index + 1, word, board)):

            return True

        visited.remove((row,col))

        return False
        

            
            