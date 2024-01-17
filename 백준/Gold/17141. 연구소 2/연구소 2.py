from itertools import combinations
from collections import deque


def bfs():
    ans = N**2

    for comb in combinations(virus, M):
        group_set = {arr[x][y] for x, y in comb} # 이번 차례에 바이러스가 놓일 구역들
        if len(group_set) < group: # 바이러스가 모든 구역에 놓여있지 않음. 확산 불가
            continue

        queue = deque([(x, y, 0) for x, y in comb])
        visit = {x*N+y for x, y in comb}

        while queue:
            r, c, t = queue.popleft()
            if t >= ans: break
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and nr*N+nc not in visit:
                    queue.append((nr, nc, t+1))
                    visit.add(nr*N+nc)
        else:
            ans = min(ans, t)

    return ans
        
def is_possible():
    global group
    visit = set()

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1 or x*N+y in visit: continue
            group += 1
            virus_found = 0
            stack = [(x, y)]
            visit.add(x*N+y)

            while stack:
                r, c = stack.pop()
                if arr[r][c] == 2:
                    virus_found = 1
                    arr[r][c] = group + 1 # 구역 번호 갱신
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and nr*N+nc not in visit:
                        stack.append((nr, nc))
                        visit.add(nr*N+nc)
                        
            if not virus_found: # 바이러스 없는 구역. 확산 불가
                return 0

    if M < group: # 바이러스보다 구역이 많음. 확산 불가
        return 0
    else:
        return 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 2]
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
group = 0 # 연결된 구역 개수

if is_possible():
    print(bfs())
else:
    print(-1)