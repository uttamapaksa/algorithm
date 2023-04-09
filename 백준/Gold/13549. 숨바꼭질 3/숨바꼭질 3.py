from collections import deque

N, K = map(int, input().split())

if N >= K:
    cnt = N - K
else:
    visit = [0] * 100001
    visit[N] = 1
    q = deque([(0, N)])
    while q:
        cnt, s = q.popleft()
        if s == K:
            break
        if s < K:
            i = s * 2
            if 0 < i <= 100000 and not visit[i]:
                visit[i] = 1
                q.appendleft((cnt, i))
            i = s + 1
            if i <= 100000 and not visit[i]:
                visit[i] = 1
                q.append((cnt + 1, i))
        if s:
            i = s - 1
            if not visit[i]:
                visit[i] = 1
                q.append((cnt + 1, i))

print(cnt)