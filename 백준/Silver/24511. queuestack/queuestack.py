from collections import deque

N = int(input())
D = [*map(int, input().split())]
Q = deque()
for i, v in enumerate(map(int, input().split())):
    if not D[i]:
        Q.appendleft(v)
M = int(input())
for v in map(int, input().split()):
    Q.append(v)

print(*[*Q][:M])