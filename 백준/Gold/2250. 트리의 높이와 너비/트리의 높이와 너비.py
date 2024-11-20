import sys; input=sys.stdin.readline

def inorder(n, l):
    global idx
    if not n:
        return
    inorder(left[n], l+1)
    idx += 1
    if l in level: level[l][1] = idx
    else: level[l] = [idx, idx]
    inorder(right[n], l+1)

N = int(input())
par = list(range(N+1))
left = [0] * (N+1)
right = [0] * (N+1)
for _ in range(N):
    n, l ,r = map(int, input().split())
    if l != -1:
        left[n] = l; par[l] = n
    if r != -1:
        right[n] = r; par[r] = n

idx = 0
level = {}
for i in range(1, N+1):
    if i == par[i]:
        inorder(i, 1)
        break

ans = (10001, 0)
for k in sorted(level.keys()):
    if ans[1] < level[k][1] - level[k][0] + 1:
        ans = (k, level[k][1] - level[k][0] + 1)
print(*ans)