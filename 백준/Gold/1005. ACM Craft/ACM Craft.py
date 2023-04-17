from collections import deque

def find(x):
    visit = set()
    start = set()
    q = deque([x])
    while q:
        s = q.popleft()
        if not condition[s]:
            visit.add(s)
            start.add(s)
            continue
        for e in condition[s]:
            if e not in visit:
                visit.add(e)
                q.append(e)
    return start

for _ in range(int(input().rstrip())):

    N, K = map(int, input().split())
    T = [0] + [*map(int, input().split())]
    T = {i: T[i] for i in range(1, N+1)}
    graph = {i: [] for i in range(1, N+1)}
    condition = {i: [] for i in range(1, N+1)}
    P = [i for i in range(N+1)]

    for _ in range(K):
        a, b = map(int, input().split())
        P[b] = a
        graph[a].append(b)
        condition[b].append(a)
    W = int(input().rstrip())

    start = find(W)
    new_start = set()
    end = set()
    cnt = 0

    while 1:
        if W in start:
            cnt += T[W]
            print(cnt)
            break

        minv = []
        for v in start:
            minv.append(T[v])
        minv = min(minv)

        for v in T:
            if v not in start: continue
            T[v] -= minv
            if not T[v]:
                start.remove(v)
                end.add(v)

                for w in graph[v]:
                    if w in end or w in start: continue
                    for c in condition[w]:
                        if c not in end: break
                    else:
                        new_start.add(w)

        if new_start:
            start = start.union(new_start)
            new_start = set()
        cnt += minv