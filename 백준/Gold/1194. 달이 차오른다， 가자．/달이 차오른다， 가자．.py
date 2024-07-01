from collections import deque

def bfs():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '0':
                start = (i, j, 0, 1)
                break
        else:
            continue
        break

    Q = deque()
    Q.append(start)
    visit[0] = [[0] * M for _ in range(N)]
    visit[0][i][j] = 1
    while Q:
        r, c, key, cnt = Q.popleft()
        for nr, nc in ((r, c+1), (r, c-1), (r+1, c), (r-1, c)):
            # index error | wall
            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] == '#': continue
            # visited
            if visit[key][nr][nc]: continue
            # exit
            if arr[nr][nc] == '1': return cnt
            # door
            if arr[nr][nc] in {'A', 'B', 'C', 'D', 'E', 'F'} and not bit[arr[nr][nc]] & key: continue
            # new key
            if arr[nr][nc] in {'a', 'b', 'c', 'd', 'e', 'f'} and not bit[arr[nr][nc]] & key:
                new_key = key | bit[arr[nr][nc]]
                if new_key not in visit:
                    visit[new_key] = [[0] * M for _ in range(N)]
                if not visit[new_key][nr][nc]:
                    Q.append((nr, nc, new_key, cnt+1))
                    visit[new_key][nr][nc] = 1
                continue
            # go
            Q.append((nr, nc, key, cnt+1))
            visit[key][nr][nc] = 1
    return -1

bit = {'A': 1, 'B': 2, 'C': 4, 'D': 8, 'E': 16, 'F': 32, 'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32}
visit = {}
N, M = map(int, input().split())
arr = [[*input()] for _ in range(N)]
print(bfs())