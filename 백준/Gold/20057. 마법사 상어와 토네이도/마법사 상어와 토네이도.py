def go():
    global ci, cj, d
    di, dj = delta[d]
    ci, cj = ci + di, cj + dj
    y = arr[ci][cj]

    # delta: left, right
    if not di:
        # every index except 'a'
        for ni, nj, p in ((ci, cj+2*dj, 0.05), (ci-1, cj+dj, 0.1), (ci+1, cj+dj, 0.1), (ci-1, cj, 0.07), (ci+1, cj, 0.07), (ci-2, cj, 0.02), (ci+2, cj, 0.02), (ci-1, cj-dj, 0.01), (ci+1, cj-dj, 0.01)):
            dust = int(y * p)
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += dust
            else:
                ans[0] += dust
            arr[ci][cj] -= dust
        # 'a'
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += arr[ci][cj]
        else:
            ans[0] += arr[ci][cj]
        arr[ci][cj] = 0

    # delta: up, down
    else:
        # every index except 'a'
        for ni, nj, p in ((ci+2*di, cj, 0.05), (ci+di, cj-1, 0.1), (ci+di, cj+1, 0.1), (ci, cj-1, 0.07), (ci, cj+1, 0.07), (ci, cj-2, 0.02), (ci, cj+2, 0.02), (ci-di, cj-1, 0.01), (ci-di, cj+1, 0.01)):
            dust = int(y * p)
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += dust
            else:
                ans[0] += dust
            arr[ci][cj] -= dust
        # 'a'
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += arr[ci][cj]
        else:
            ans[0] += arr[ci][cj]
        arr[ci][cj] = 0


delta = ((0, -1), (1, 0), (0, 1), (-1, 0))
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ci, cj, d = N//2, N//2, 0
ans = [0]

for i in range(1, N):
    for _ in range(2): # go i and turn
        for _ in range(i):
            go()
        d = (d+1) % 4
for _ in range(N-1): # last line
    go()

print(ans[0])