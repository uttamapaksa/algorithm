from heapq import heappush, heappop

N = int(input())
classes = sorted(tuple(map(int, input().split())) for _ in range(N))
ends = []
count = 0

for start, end in classes:
    if not ends or start < ends[0]:
        count += 1
    else:
        heappop(ends)
    heappush(ends, end)

print(count)