from bisect import bisect_left

N, M = map(int,input().split())
Q = list(range(1, N+1))

ans = 0
curr = 0
for v in map(int, input().split()):
    next = bisect_left(Q, v)
    diff = abs(curr - next)
    ans += min(len(Q) - diff, diff)
    curr = next if next != N-1 else 0
    Q.remove(v)

print(ans)