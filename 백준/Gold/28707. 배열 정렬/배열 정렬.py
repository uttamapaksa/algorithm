from heapq import heappush, heappop


def init(n):
    return str(int(n) - 1)


def dijkstra(u):
    dist = {u: 0}
    heap = [(0, u)]

    while heap:
        d, u = heappop(heap)
        if dist[u] < d:
            continue
        for i in range(N):
            if u[i] > u[i+1]:
                break
        else:
            return d
        u = list(u)
        for l, r, c in mod:
            u[l], u[r] = u[r], u[l]
            v = ''.join(u)
            if v not in dist or dist[v] > d + c:
                dist[v] = d + c
                heappush(heap, (dist[v], v))
            u[l], u[r] = u[r], u[l]

    return -1


N = int(input())
arr = ['0'] + [*map(init, input().split())]
mod = tuple(tuple(map(int, input().split())) for _ in range(int(input())))

print(dijkstra(''.join(arr)))