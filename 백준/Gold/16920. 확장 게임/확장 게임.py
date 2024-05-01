from collections import deque

# input
toInt = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, ".": 0, "#": -1}
N, M, P = map(int, input().split())
S = [0] + [*map(int, input().split())]
arr = [[*input()] for _ in range(N)]
starts = [[] for _ in range(P+1)]
ans = [0] * (P+1)

for i in range(N):
    for j in range(M):
        player = toInt[arr[i][j]]
        arr[i][j] = player  # convert to int
        if player > 0:
            starts[player].append((i, j, S[player]))  # initial queue
            ans[player] += 1  # answer

# bfs
while sum(len(start) for start in starts):
    for start in starts:
        curr = deque(start)
        start.clear()

        while curr:
            r, c, cnt = curr.popleft()
            # initial queue
            if not cnt:
                start.append((r, c, S[arr[r][c]]))
                continue
            # current queue
            for nr, nc in ((r+1, c), (r-1, c), (r, c-1), (r, c+1)):
                if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc]: continue
                arr[nr][nc] = arr[r][c]
                curr.append((nr, nc, cnt-1))
                ans[arr[nr][nc]] += 1

# output
print(*ans[1:])