from heapq import heappop, heappush
import sys
input = sys.stdin.readline

heap = []
l = 0
for _ in range(int(input())):
    x = int(input())
    if x:
        l += 1
        heappush(heap, (abs(x), x))
    else:
        if l:
            l -= 1
            print(heappop(heap)[1])
        else:
            print(0)
