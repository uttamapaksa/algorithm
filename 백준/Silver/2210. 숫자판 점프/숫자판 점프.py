delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arr = [input().split() for _ in range(5)]
ans = set()
    
def sol(v, r, c):
    if len(v) == 6:
        ans.add(v)
        return
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= 5 or nc < 0 or nc >=5: continue
        sol(v + arr[nr][nc], nr, nc)

for i in range(5):
    for j in range(5):
        sol(arr[i][j], i, j)

print(len(ans))