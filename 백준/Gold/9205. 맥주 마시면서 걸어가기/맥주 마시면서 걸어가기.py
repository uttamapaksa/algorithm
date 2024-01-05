def canGo(r, c, nr, nc):
    if abs(nr-r) + abs(nc-c) <= 1000:
        return 1
    return 0


def bfs():
    q = deque()
    q.append((sr, sc))
    v = [0] * n

    while q:
        r, c = q.popleft()
        if canGo(r, c, er, ec):
            return 'happy'
        for i in range(n):
            if v[i]: continue
            nr, nc = stores[i]
            if canGo(r, c, nr, nc):
                q.append((nr, nc))
                v[i] = 1

    return 'sad'


from collections import deque

for _ in range(int(input())):
    n = int(input())
    sr, sc = map(int, input().split())
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    er, ec = tuple(map(int, input().split()))

    print(bfs())