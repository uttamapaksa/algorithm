from heapq import heappush, heappop

N = int(input())
heap = []
for _ in range(N):
    heappush(heap, int(input()))

answer = 0
if N > 1:
    while len(heap) > 2:
        sumv = heappop(heap) + heappop(heap)
        answer += sumv
        heappush(heap, sumv)

    answer += sum(heap)

print(answer)