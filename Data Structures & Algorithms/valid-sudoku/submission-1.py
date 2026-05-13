class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashSet = set()
        def valid(board, curVal, row, col, hashSet):
            checkRow = "row" + str(row) + "value" + curVal
            checkCol = "col" + str(col) + "value" + curVal
            checkBox = "rowbox" + str(i//3) + "colbox" + str(j//3) + "value" + curVal
            if checkRow in hashSet or checkCol in hashSet or checkBox in hashSet:
                return False
            hashSet.add("row" + str(row) + "value" + curVal)
            hashSet.add("col" + str(col) + "value" + curVal)
            hashSet.add("rowbox" + str(i//3) + "colbox" + str(j//3) + "value" + curVal)
            return True


        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if not valid(board, board[i][j], i, j, hashSet):
                        return False
        
        return True
    
    
