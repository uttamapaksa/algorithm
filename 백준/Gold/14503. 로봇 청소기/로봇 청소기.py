N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0

def clean(r, c):
    if not arr[r][c]:
        global ans
        arr[r][c] = 2
        ans += 1

def promising(r, c, d):
    # to clean
    for i in range(3, -1, -1):
        nd = (d+i) % 4
        dr, dc = dir[nd]
        nr, nc = r + dr, c + dc
        if not arr[nr][nc]:
            return nr, nc, nd
    # not to clean
    dr, dc = dir[d]
    nr, nc = r - dr, c - dc
    # is not wall
    if arr[nr][nc] != 1:
        return nr, nc, d
    # is wall
    return False

while True:
    clean(r, c)
    tmp = promising(r, c, d)
    if tmp:
        r, c, d = tmp
    else:
        break

print(ans)