from collections import deque
def division(n):
    q = deque([(n, 0, str(n))])
    visited = [0] * (n+1)
    while q:
        n, cnt, track = q.popleft()
        a, b, c = n//3, n//2, n-1
        if n == 1: return cnt, track
        if not n%3 and not visited[a]: q.append((a, cnt+1, track + f' {str(a)}')); visited[a] = 1
        if not n%2 and not visited[b]: q.append((b, cnt+1, track + f' {str(b)}')); visited[b] = 1
        if not visited[c]: q.append((c, cnt+1, track + f' {str(c)}')); visited[c] = 1

cnt, track = division(int(input()))
print(cnt)
print(track)