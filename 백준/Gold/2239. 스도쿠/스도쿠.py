import sys; input = sys.stdin.readline


def next_idx(r, c):
    for j in range(c+1, 9):
        if not arr[r][j]:
            return r, j
    for i in range(r+1, 9):
        for j in range(9):
            if not arr[i][j]:
                return i, j
    return 0


def sudoku(r, c):
    P = next_idx(r, c)
    R = arr_row[r]
    C = arr_col[c]
    S = arr_33[(r//3) * 3 + (c//3)]
    
    for n in range(1, 10):
        if n in R or n in C or n in S: continue
        arr[r][c] = n; R.add(n); C.add(n); S.add(n)
        if not next_idx(r, c): return
        sudoku(P[0], P[1])
        if not next_idx(r, c): return
        arr[r][c] = 0; R.remove(n); C.remove(n); S.remove(n)


arr = [[*map(int, input().rstrip())] for _ in range(9)]
arr_row = [{arr[i][j] for j in range(9)} for i in range(9)]
arr_col = [{arr[i][j] for i in range(9)} for j in range(9)]
arr_33 = [{arr[i][j], arr[i][j+1], arr[i][j+2], arr[i+1][j], arr[i+1][j+1], arr[i+1][j+2], arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]} for i in range(0, 9, 3) for j in range(0, 9, 3)]

sudoku(*next_idx(0, -1))

for i in arr:
    for j in i:
        print(j, end='')
    print()