import sys; input = sys.stdin.readline

R, C = map(int, input().split())
arr = [[*input().rstrip()] for _ in range(R)]
ans = 0

q = {(0, 0, arr[0][0])}
while q:
    r, c, visit = q.pop()
    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in visit:
            q.add((nr, nc, visit + arr[nr][nc]))
    ans = max(ans, len(visit))

print(ans)