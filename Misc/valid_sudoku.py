import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
    
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        sudoku_matrix = [[set() for j in range(3)] for i in range(3)]
        sudoku_set_row = [set() for i in range(9)]
        sudoku_set_col = [set() for i in range(9)]
        for row in range(9):
            for col in range(row, 9):
                element = board[row][col]
                element_transpose = board[col][row]
                sudoku_row = row//3 
                sudoku_col = col//3

                if row == 4:
                    print('pr')

                if element != '.':
                    if element in sudoku_set_row[row]:
                        return False
                    else:
                        sudoku_set_row[row].add(element)
                    
                    if element in sudoku_set_col[col]:
                        return False
                    else:
                        sudoku_set_col[col].add(element)
                    
                    if element in sudoku_matrix[sudoku_row][sudoku_col]:
                        return False
                    else:
                        sudoku_matrix[sudoku_row][sudoku_col].add(element)
                
                if element_transpose != '.' and element_transpose!= element:
                    if element_transpose in sudoku_set_col[row]:
                        return False
                    else:
                        sudoku_set_col[row].add(element_transpose)
                    
                    if element_transpose in sudoku_set_row[col]:
                        return False
                    else:
                        sudoku_set_row[col].add(element_transpose)


                    if element_transpose in sudoku_matrix[sudoku_col][sudoku_row]:
                        return False
                    else:
                        sudoku_matrix[sudoku_col][sudoku_row].add(element_transpose)
            
        return True

dd= Solution()
board = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".","6",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".","8",".",".",".","."],["9",".",".",".","7","5",".",".","."],[".",".",".",".","5",".",".","8","."],[".",".","9",".",".",".",".",".","."],["2",".","6",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

print("VIM in use")
print(dd.isValidSudoku(board))
