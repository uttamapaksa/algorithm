def rotate():
    for sr, sc, er, ec in idxs:
        init = arr[sr][sc]
        # top
        for nc in range(sc, ec):
            arr[sr][nc] = arr[sr][nc+1]
        # right
        for nr in range(sr, er):
            arr[nr][ec] = arr[nr+1][ec]
        # bot
        for nc in range(ec, sc, -1):
            arr[er][nc] = arr[er][nc-1]
        # left
        for nr in range(er, sr, -1):
            arr[nr][sc] = arr[nr-1][sc]
        arr[sr+1][sc] = init


N, M, R = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]

K = min(N, M) // 2
idxs = [[i, i, N-1-i, M-1-i] for i in range(K)]
for _ in range(R):
    rotate()

for line in arr:
    print(*line)