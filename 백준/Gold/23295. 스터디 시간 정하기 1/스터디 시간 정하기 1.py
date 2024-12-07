import sys;input=sys.stdin.readline

N, T = map(int, input().split())
tree = [0] * 100001
for _ in range(N):
    for _ in range(int(input())):
        s, e = map(int, input().split())
        tree[e] += 1
        tree[s] -= 1
for i in range(99999, -1, -1):
    tree[i] += tree[i+1]

cur = sum(tree[i] for i in range(T+1))
mxv = cur
idx = 0
for i in range(T+1, 100001):
    cur += tree[i] - tree[i-T]
    if mxv < cur:
        mxv = cur                                                                                                                                                                                                                                                                                                                                                                                                           
        idx = i-T

print(idx, idx+T)
