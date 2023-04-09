from collections import deque

N, K = map(int, input().split())
visit = [0] * 100001
visit[N] = 1
q = deque([(0, N)])

while q:
    cnt, s = q.popleft()
    if s == K:
        break
    if s < K:
        i = s * 2
        if 0 < i <= 100000 and (not visit[i] or visit[i] == cnt):
            visit[i] = cnt
            q.append((cnt + 1, i))
        i = s + 1
        if i <= 100000 and (not visit[i] or visit[i] == cnt):
            visit[i] = cnt
            q.append((cnt + 1, i))
    if s > 0:
        i = s - 1
        if not visit[i] or visit[i] == cnt:
            visit[i] = cnt
            q.append((cnt + 1, i))

print(cnt)
print(1 + q.count((cnt, K)))