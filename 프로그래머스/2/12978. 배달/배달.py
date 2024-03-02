from heapq import heappush, heappop
MAX = 500001

def solution(N, road, K):
    G = [[MAX] * (N+1) for _ in range(N+1)]
    for u, v, w in road:
        G[u][v] = min(G[u][v], w)
        G[v][u] = min(G[v][u], w)
    
    D = [MAX] * (N+1)
    D[1] = 0
    heap = []
    print(heap)
    heappush(heap, ((D[1], 1))
    
    print(heap)
#     while heap:
#         d, u = heappop(heap)
#         if D[u] < d: continue
             
#         for v in range(1, 50):
#             if G[u][v] == MAX: continue
#             if D[v] > d + G[u][v]:
#                 D[v] = d + G[u][v]
#                 heappush((D[v], v))
    
#     print(D)
            


    return 0