from collections import deque

A, B = map(int, input().split())
visit = {B: 1}
q = deque([B])
found = 0
while q:
    s = q.popleft()
    if s == A:
        print(visit[A]);
        found = 1;
        break
    if not s % 2:
        e = s // 2
        if e >= A and e not in visit:
            visit[e] = visit[s] + 1
            q.append(e)
    elif s % 10 == 1:
        e = s // 10
        if e >= A and e not in visit:
            visit[e] = visit[s] + 1
            q.append(e)
if not found: print(-1)