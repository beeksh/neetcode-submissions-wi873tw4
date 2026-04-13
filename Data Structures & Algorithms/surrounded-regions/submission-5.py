class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def cap(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols or
                board[r][c]!="O"):
                return
            board[r][c] = "T"
            cap(r+1,c)
            cap(r-1,c)
            cap(r,c+1)
            cap(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if ((r in [0, rows-1] or c in [0, cols-1]) and
                    board[r][c]=="O"):
                    cap(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"