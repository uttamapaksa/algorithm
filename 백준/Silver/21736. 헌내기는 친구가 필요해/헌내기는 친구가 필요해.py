from collections import deque

n, m = map(int, input().split())
A = []
V = [[0] * m for _ in range(n)]

for i in range(n):
    string = input()
    for j in range(m):
        if string[j] == 'I':
            # doyeon = [i, j]
            Q = deque()
            Q.append((i, j))
            V[i][j] = 1
    A.append(string)


ans = 0
while Q:
    r, c = Q.popleft()
    for (dr, dc) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= n or nc < 0 or nc >= m or V[nr][nc] or A[nr][nc] == 'X': continue
        if A[nr][nc] == 'P':
            ans += 1
        Q.append((nr, nc))
        V[nr][nc] = 1

print(ans or 'TT')
