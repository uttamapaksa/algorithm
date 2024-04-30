delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
i = 0

while True:
    N = int(input())
    if not N:
        break

    arr = [[*map(int, input().split())] for _ in range(N)]
    dp = [[2500] * N for _ in range(N)]

    dp[0][0] = arr[0][0]
    stack = [(0, 0)]
    while stack:
        r, c = stack.pop()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue  # index
            if dp[-1][-1] <= dp[r][c] + arr[nr][nc]: continue  # smaller than goal
            if dp[nr][nc] <= dp[r][c] + arr[nr][nc]: continue  # smaller than next
            dp[nr][nc] = dp[r][c] + arr[nr][nc]
            stack.append((nr, nc))

    i += 1
    print(f'Problem {i}: {dp[-1][-1]}')
