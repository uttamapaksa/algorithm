from collections import deque

N, L = map(int, input().split())
arr = [*map(int, input().split())]
Q = deque()

ans = []
for i, v in enumerate(arr):
    while Q and Q[-1][1] >= v:
        Q.pop()
    Q.append((i, v))
    while Q[0][0] < i-L+1:
        Q.popleft()
    ans.append(Q[0][1])

print(*ans)