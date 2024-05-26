def toInt(x):
    if x == '.': 
        return 0
    return 1

N, M = map(int, input().split())
arr = [[*map(toInt, [*input()])] for _ in range(N)]
ans = 0

for r in range(N):
    stack = [(r, 0)]
    while stack:
        r, c = stack.pop()
        arr[r][c] = 1
        if c == M-1:
            ans += 1
            break
        # (r-1, c+1) comes last in the greedy algorithm
        for nr, nc in ((r+1, c+1), (r, c+1), (r-1, c+1)):
            if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc]:
                stack.append((nr, nc))

print(ans)