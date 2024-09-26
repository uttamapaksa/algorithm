from collections import deque

N = int(input())
A = [0] * (N+1)
D = (1, 2, 5, 7)

Q = deque([0])
while Q:
    u = Q.popleft()
    for v in (u+7, u+5, u+2, u+1):
        if v <= N and not A[v]:
            A[v] = A[u] + 1
            Q.append(v)
            if v == N:
                break
    else:
        continue
    break

print(A[N])