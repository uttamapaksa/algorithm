from collections import deque

F, S, G, U, D = map(int, input().split())
Q = deque()
Q.append((S, 0))
V = [0] * (F+1)

while Q:
    curr, ans = Q.popleft()
    if curr == G:
        print(ans)
        break
    up, down = curr + U, curr - D
    if 0 < up <= F and not V[up]:
        Q.append((up, ans+1))
        V[up] = 1
    if 0 < down <= F and not V[down]:
        Q.append((down, ans+1))
        V[down] = 1
else:
    print("use the stairs")