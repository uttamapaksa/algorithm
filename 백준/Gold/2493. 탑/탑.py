from heapq import heappush, heappop

N = int(input())
arr = [*map(int, input().split())]
answer = [0] * N

heap = []
for i in range(N-1, -1, -1):
    while heap and arr[i] > heap[0][0]:
        answer[heappop(heap)[1]] = i+1
    heappush(heap, (arr[i], i))

print(*answer)