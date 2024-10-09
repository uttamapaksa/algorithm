def query(idx):
    res = 0
    while idx:
        res += tree[idx] 
        idx -= idx & -idx
    return res

def update(idx, val):
    while idx <= N:
        tree[idx] += val
        idx += idx & -idx

N, Q = map(int, input().split())
arr = [*map(int, input().split())]
tree = [0] * (N+1)
for i in range(N):
    update(i+1, arr[i])

ans = []
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y: x, y = y, x
    ans.append(query(y) - query(x-1))
    delta = b - arr[a-1]
    arr[a-1] += delta
    update(a, delta)

print('\n'.join(map(str, ans)))