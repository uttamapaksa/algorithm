N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
delta = [0, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


for _ in range(M):
    direction, space = map(int, input().split())
    
    # move cloud & rain
    rain = set()
    for r, c in cloud:
        dr, dc = delta[direction]
        r, c = (r + dr*space) % N, (c + dc*space) % N
        rain.add((r, c))
        arr[r][c] += 1

    # duplicate water
    for r, c in rain:
        cnt = 0
        for nr, nc in ((r-1, c-1), (r-1, c+1), (r+1, c+1), (r+1, c-1)):
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                cnt += 1
        arr[r][c] += cnt
    
    # make cloud
    cloud = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] >= 2 and (r, c) not in rain:
                cloud.append((r, c))
                arr[r][c] -= 2


ans = 0
for r in range(N):
    for c in range(N):
        ans += arr[r][c]
print(ans)