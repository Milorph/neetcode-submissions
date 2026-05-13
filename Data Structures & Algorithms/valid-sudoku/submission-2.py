class Solution:

    def valid(self, row, col, hashSet, board):
        rowCheck = str(row) + "row" + str(board[row][col])
        colCheck = str(col) + "col" + str(board[row][col])
        boxCheck = "row" + str(row//3) + "col" + str(col//3) + "value" + str(board[row][col])

        if rowCheck in hashSet or colCheck in hashSet or boxCheck in hashSet:
            return False
        hashSet.add(rowCheck)
        hashSet.add(colCheck)
        hashSet.add(boxCheck)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashSet = set()

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] != '.':
                    if self.valid(i,j, hashSet, board):
                        continue
                    else:
                        return False
        return True
        
        

