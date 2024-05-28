def rotate(arr, r, c, s):
    newArr = [[*row] for row in arr]
    for i in range(1, s+1):
        sr, sc, er, ec = r-i, c-i, r+i, c+i
        init = newArr[sr][sc]
        # left
        for nr in range(sr, er):
            newArr[nr][sc] = newArr[nr+1][sc]
        # bot
        for nc in range(sc, ec):
            newArr[er][nc] = newArr[er][nc+1]
        # right
        for nr in range(er, sr, -1):
            newArr[nr][ec] = newArr[nr-1][ec]
        # top
        for nc in range(ec, sc, -1):
            newArr[sr][nc] = newArr[sr][nc-1]
        newArr[sr][sc+1] = init

    return newArr


def perm(arr, c):
    if c == K:
        global ans
        for row in arr:
            ans = min(ans, sum(row))
        return
    for i in range(K):
        if visit[i]: continue
        visit[i] = 1
        newArr = rotate(arr, *rotates[i])
        perm(newArr, c+1)
        visit[i] = 0


N, M, K = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
visit = [0] * K

rotates = []
for _ in range(K):
    r, c, s = map(int, input().split())
    rotates.append((r-1, c-1, s))

ans = 10000
perm(arr, 0)
print(ans)