n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
white = [] # bishops on white squares
black = [] # bishops on black squares
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            if (i+j) % 2:
                black.append((i, j))
            else:
                white.append((i, j))
W, B = len(white), len(black)
w_ans, b_ans = [0], [0]

def promising(r, c, put):
    for i, j in put:
        if abs(r - i) == abs(c - j):
            return False
    return True

def sol(bishops, ans, L):
    stack = [(set(), 0, 0)]
    while stack:
        put, k, v = stack.pop()
        if k == L:
            ans[0] = max(ans[0], v)
            continue
        r, c = bishops[k]

        if promising(r, c, put): # add
            stack.append((put | {(r, c)}, k+1, v+1))
        if (v+L-k-1) > ans[0]: # not add
            stack.append((put, k+1, v))

sol(white, w_ans, W)
sol(black, b_ans, B)

print(w_ans[0] + b_ans[0])