class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
#         I need acess every value in the board
#         I need to track repetitive digits
#         Also, in a 3x 3 box
#         2 hashes where key is the the row, and the value is a set and we ask if the value at every position is in our hashset
# hash where the key (r //3, c//3) and value is a set

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.' or board[r][c] == ',':
                    continue
                elif (board[r][c] in rows[r] or
                  board[r][c] in cols[c] or
                  board[r][c] in squares[(r//3,c//3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])
        return True