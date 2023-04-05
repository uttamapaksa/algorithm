from collections import deque

N, M = map(int, input().split())
board = {i: i for i in range(1, 101)}
visit = [0] * 101
for _ in range(N + M):
    a, b = map(int, input().split())
    board[a] = b

q = deque([(1, 0)])
while q:
    s, cnt = q.popleft()
    if visit[s]: continue
    visit[s] = 1
    if s == 100: print(cnt); break
    for i in range(1, 7):
        if s + i < 101:
            q.append((board[s + i], cnt + 1))
        else:
            q.append((board[s], cnt + 1))