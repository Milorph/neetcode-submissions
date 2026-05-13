class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        hashSet = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if not self.isValid(board, i, j, board[i][j], hashSet):
                        return False
        return True

    def isValid(self, board, row, col, value, hashSet):
            
            rowCheck = 'row' + str(row) + 'value' + value
            colCheck = 'col' + str(col) + 'value' + value
            rowColCheck = 'rowBox' + str(row//3) + 'colbox' + str(col//3) + 'value' + value

            print(hashSet)
            checking = rowCheck in hashSet or colCheck in hashSet or rowColCheck in hashSet

            if (checking):
                return False
            
            hashSet.add(rowCheck)
            hashSet.add(colCheck)
            hashSet.add(rowColCheck)

            return True
        