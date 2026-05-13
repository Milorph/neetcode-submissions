class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowCol = 0
        highCol = len(matrix) - 1
        lowRow = 0
        highRow = len(matrix[0]) - 1

        # main logic to find which "column" -> its actually the row
        while lowCol <= highCol:
            midCol = (lowCol + highCol)//2

            if (midCol < len(matrix) - 1) and (target >= matrix[midCol][0] and target < matrix[midCol + 1][0]):
                break;
            elif target < matrix[highCol][0]:
                highCol = midCol - 1
            else:
                lowCol = midCol + 1

        # Normal binary search
        while lowRow <= highRow:
            midRow = (lowRow + highRow)//2
            if matrix[midCol][midRow] == target:
                return True
            elif target > matrix[midCol][lowRow]:
                lowRow = midRow + 1
            else:
                highRow = midRow - 1
        return False
