def turnSubArr():
    global arr
    newArr = [[0] * N for _ in range(N)]
    for i in range(0, N, L):
        for j in range(0, N, L):
            for k in range(L):
                for l in range(L):
                    newArr[i+k][j+l] = arr[i+L-l-1][j+k]
    arr = newArr


def meltIce():
    melted = []
    for r in range(N):
        for c in range(N):
            if not arr[r][c]: continue
            cnt = 0
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                    cnt += 1
            if cnt < 3:
                melted.append((r,  c))
    for r, c in melted:
        arr[r][c] -= 1


def dfs(r, c):
    global iceSum, biggestIce
    S = [(r, c)]
    iceSum += arr[r][c]
    currIce = 1
    arr[r][c] = 0
    while S:
        r, c = S.pop()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                S.append((nr, nc))
                iceSum += arr[nr][nc]
                currIce += 1
                arr[nr][nc] = 0
    biggestIce = max(biggestIce, currIce)


N, Q = map(int, input().split())
N = 2**N
arr = [list(map(int, input().split())) for _ in range(N)]
Ls = list(map(lambda x: pow(2, int(x)), input().split()))
delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

for L in Ls:
    turnSubArr()
    meltIce()

iceSum = biggestIce = 0
for r in range(N):
    for c in range(N):
        if arr[r][c]:
            dfs(r, c)

print(iceSum)
print(biggestIce)