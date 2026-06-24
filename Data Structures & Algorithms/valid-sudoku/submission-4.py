class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            m = {}
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in m:
                        return False
                    m[board[i][j]] = 1
        for j in range(9):
            m = {}
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in m:
                        return False
                    m[board[i][j]] = 1
        for z in range(3):
            for k in range(3):
                m = {}
                for i in range(3):
                    for j in range(3):
                        if board[i + 3*z][j + 3*k] != ".":
                            if board[i + 3*z][j + 3*k] in m:
                                return False
                            m[board[i + 3*z][j + 3*k]] = 1
        return True
