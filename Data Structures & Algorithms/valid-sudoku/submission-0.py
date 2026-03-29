class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rh, ch, sh = [{} for i in range(9)], [{} for i in range(9)], [[{} for i in range(3)] for j in range (3)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rh[i] or board[i][j] in ch[j]  or board[i][j] in sh[i//3][j//3]:
                    return False
                else:
                    rh[i][board[i][j]]=1
                    ch[j][board[i][j]]=1
                    sh[i//3][j//3][board[i][j]]=1
        return True                