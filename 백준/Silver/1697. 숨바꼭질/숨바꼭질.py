from collections import deque

n, k = map(int, input().split())
visit = [0] * 200000
if n == k:
    print(0)
else:
    q = deque([(n, 0)])
    while q:
        n, cnt = q.popleft()
        if visit[n]: continue
        visit[n] = 1
        if n * 2 == k or n + 1 == k or n - 1 == k:
            print(cnt + 1)
            break
        if n < k:
            q.append((n * 2, cnt + 1))
            q.append((n + 1, cnt + 1))
        if n:
            q.append((n - 1, cnt + 1))