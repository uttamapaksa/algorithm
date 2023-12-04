R, C, T = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(R)]
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
spread = []

def find_a():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                arr[i][j] = 0
                arr[i+1][j] = 0
                return i, j

def dust():
    for r in range(R):
        for c in range(C):
            val = arr[r][c]
            if val and val != -1:
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or (nr, nc) in [(ar, ac), (ar+1, ac)]: continue
                    arr[r][c] -= val // 5
                    spread.append((nr, nc, val // 5))

    while spread:
        nr, nc, val = spread.pop()
        arr[nr][nc] += val


def circulate():
    # left
    for i in range(ar-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    for i in range(ar+2, R-1):
        arr[i][0] = arr[i+1][0]
    # <--
    for j in range(0, C-1):
        arr[0][j] = arr[0][j+1]
        arr[R-1][j] = arr[R-1][j+1]
    # rigth
    for i in range(0, ar):
        arr[i][C-1] = arr[i+1][C-1]
    for i in range(R-1, ar+1, -1):
        arr[i][C-1] = arr[i-1][C-1]
    # -->
    for j in range(C-1, 0, -1):
        arr[ar][j] = arr[ar][j-1]
        arr[ar+1][j] = arr[ar+1][j-1]

ar, ac = find_a()
for _ in range(T):
    dust()
    circulate()

ans = sum([sum(l) for l in arr])
print(ans)