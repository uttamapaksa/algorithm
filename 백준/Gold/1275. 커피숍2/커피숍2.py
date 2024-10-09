import sys; input=sys.stdin.readline
# input
N, Q = map(int, input().split())
arr = [*map(int, input().split())]
tree = [0] * (N+1)
# build
for i in range(N):
    idx = i+1
    while idx <= N:
        tree[idx] += arr[i]
        idx += idx & -idx

ans = []
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    # query y
    ry = 0
    while y:
        ry += tree[y] 
        y -= y & -y
    # query x
    x -= 1
    rx = 0
    while x:
        rx += tree[x] 
        x -= x & -x
    ans.append(ry - rx)
    # update
    arr[a-1], delta = b, b - arr[a-1]
    while a <= N:
        tree[a] += delta
        a += a & -a
# output
print('\n'.join(map(str, ans)))