from itertools import combinations
from collections import deque


def bfs():
    for comb in combinations(virus, M):
        queue = deque([(x, y, 0) for x, y in comb])
        visit = {x*N+y for x, y in comb}
        cnt = V

        while queue:
            r, c, t = queue.popleft()
            if t >= ans[0]: # 가지치기
                break
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and nr*N+nc not in visit:
                    queue.append((nr, nc, t+1))
                    visit.add(nr*N+nc)
                    if not arr[nr][nc]:
                        cnt += 1 # 0일 경우 cnt 추가
            if cnt >= total: # 전부 확산
                ans[0] = min(ans[0], t+1)
                break

        
def is_possible():
    group = 0
    visit = set()

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1 or x*N+y in visit: continue
            group += 1
            virus_found = 0
            zero_found = 0
            stack = [(x, y)]
            visit.add(x*N+y)

            while stack:
                r, c = stack.pop()
                if arr[r][c] == 2:
                    virus_found = 1
                else:
                    zero_found = 1
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and nr*N+nc not in visit:
                        stack.append((nr, nc))
                        visit.add(nr*N+nc)
                        
            if not virus_found: # 바이러스 없는 구역. 확산 불가
                return 0
            if not zero_found: # 바이러스로 가득찬 구역. 카운팅 불필요
                group -= 1

    if M < group: # 바이러스보다 구역이 많음. 확산 불가
        return 0
    else:
        return 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 2]
zero = [(i, j) for i in range(N) for j in range(N) if not arr[i][j]]
V = len(virus)
total = V + len(zero) # 확산 가능 칸 개수
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = [N*N]

if is_possible():
    if V == total: # 이미 전부 확산
        print(0)
    else:
        bfs()
        print(ans[0])
else:
    print(-1)