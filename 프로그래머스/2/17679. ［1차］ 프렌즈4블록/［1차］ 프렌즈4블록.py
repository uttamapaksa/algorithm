
def solution(n, m, board):
    
    def explode() -> bool:
        nonlocal board, ans
        square = set()
        for r in range(n-1):
            for c in range(m-1):
                if board[r][c] == '.': continue
                if len({board[r][c], board[r+1][c], board[r][c+1], board[r+1][c+1]}) == 1:
                    square |= {(r, c), (r+1, c), (r, c+1), (r+1, c+1)}
        
        if square:
            for r, c in square:
                board[r][c] = "."
            ans += len(square)
            return True
        return False


    def gravity() -> None:
        for c in range(m):
            for r in range(n-2, -1, -1):
                if board[r][c] == '.': continue
                nr = r
                for tmpr in range(r+1, n):
                    if board[tmpr][c] == '.':
                        nr = tmpr
                    else:
                        break
                if r != nr:
                    board[nr][c], board[r][c] = board[r][c], '.'


    board = [[*row] for row in board]
    ans = 0
    while explode():
        gravity()
    
    return ans
