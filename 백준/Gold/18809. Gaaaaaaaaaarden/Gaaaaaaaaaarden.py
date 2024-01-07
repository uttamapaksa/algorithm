from itertools import combinations
from collections import deque

N, M, G, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
new_arr = [[c for c in r] for r in arr]
yellow = {(i, j) for i in range(N) for j in range(M) if arr[i][j] == 2}
white = [(i, j) for i in range(N) for j in range(M) if arr[i][j]]
d = ((-1, 0), (0, -1), (1, 0), (0, 1))
ans = 0


for green in combinations(yellow, G):
    green = set(green)
    for red in combinations(yellow-green, R):
        for i, j in white: # reset
            new_arr[i][j] = (0, 0)
        q = deque()
        for i, j in green: # set green
            new_arr[i][j] = (1, 2)
            q.append((i, j))
        for i, j in red: # set red
            new_arr[i][j] = (1, 3)
            q.append((i, j))
        total = 0
    
        while q:
            r, c = q.popleft()
            time, color = new_arr[r][c][0]+1, new_arr[r][c][1]
            if color == 5: continue # already flower
            for dr, dc in d:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and new_arr[nr][nc]:
                    if new_arr[nr][nc][0] == 0: # first
                        new_arr[nr][nc] = (time, color) 
                        q.append((nr, nc))
                    elif new_arr[nr][nc] == (time, 5-color): # flower
                        new_arr[nr][nc] = (time, 5)
                        total += 1
        ans = max(ans, total)

print(ans)