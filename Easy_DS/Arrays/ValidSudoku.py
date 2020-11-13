class ValidSudoku:
    def __init__(self):
        return

    def isValidSudoku(self, board):
        for i in range(len(board)):
            rowMap, colMap, gridMap = {}, {}, {}
            for j in range(len(board)):

                # row validations
                rowMap[board[i][j]] = rowMap.get(board[i][j], None)
                if board[i][j] != "." and rowMap[board[i][j]]:
                    return False
                else:
                    rowMap[board[i][j]] = True
                    
                # column validationss
                colMap[board[j][i]] = colMap.get(board[j][i], None)
                if board[j][i] != "." and colMap[board[j][i]]:
                    return False
                else:
                    colMap[board[j][i]] = True
                    
                # 3x3 grid validations
                rowIndex = 3 * (i//3)
                colIndex = 3 * (i%3)

                gridMap[board[rowIndex + j//3][colIndex + j%3]] = gridMap.get(board[rowIndex + j//3][colIndex + j%3], None)

                if board[rowIndex + j//3][colIndex + j%3] != "." and gridMap[board[rowIndex + j//3][colIndex + j%3]]:
                    return False
                else:
                    gridMap[board[rowIndex + j//3][colIndex + j%3]] = True
                    
        return True

    def valid_sudoku_refined(self, board):
        setData = set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] + ' in row' + str(i) in setData or board[i][j] + ' in col' + str(j) in setData or board[i][j] + ' in box' + str(i//3) + ' and' + str(j//3) in setData:
                        return False
                    else:
                        setData.add(board[i][j] + ' in row' + str(i))
                        setData.add(board[i][j] + ' in col' + str(j))
                        setData.add(board[i][j] + ' in box' + str(i//3) + ' and' + str(j//3))


        return True
                    
                    

# arr = [["5","3",".",".","7",".",".",".","."],
#         ["6",".",".","1","9","5",".",".","."],
#         [".","9","8",".",".",".",".","6","."],
#         ["8",".",".",".","6",".",".",".","3"],
#         ["4",".",".","8",".","3",".",".","1"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".","6",".",".",".",".","2","8","."],
#         [".",".",".","4","1","9",".",".","5"],
#         [".",".",".",".","8",".",".","7","9"]]

# arr = [[".",".",".",".",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],["9","3",".",".","2",".","4",".","."],[".",".","7",".",".",".","3",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3","4",".",".",".","."],[".",".",".",".",".","3",".",".","."],[".",".",".",".",".","5","2",".","."]]

arr = [[".",".",".", ".","8",".", ".",".","."],
        [".",".",".", ".",".",".", "5",".","."],
        [".",".",".", ".","4",".", ".","2","."],

        [".",".",".", "3",".","9", ".",".","."],
        [".",".","1", "8",".",".", "9",".","."],
        [".",".",".", ".",".","5", "1",".","."],

        [".",".","3", ".",".","8", ".",".","."],
        [".","1","2", ".","3",".", ".",".","."],
        [".",".",".", ".",".","7", ".",".","1"]]  

# print(arr[8][8])
# print(ValidSudoku().isValidSudoku(arr))
print(ValidSudoku().valid_sudoku_refined(arr))
