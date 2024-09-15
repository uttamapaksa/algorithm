import sys; input = sys.stdin.readline


def update(i, j, k):
    l, r = i+size, j+size
    while l <= r:
        if l & 1:
            tree[l] += k
            l += 1
        if not r & 1:
            tree[r] += k
            r -= 1
        l >>= 1; r >>= 1


def query(x):
    res = arr[x]
    x += size
    while x:
        res += tree[x]
        x >>= 1
    ans.append(str(res))


N = int(input())
arr = tuple(map(int, input().split()))
M = int(input())

size = 1
while size < N:
    size <<= 1
tree = [0] * (size*2)

ans = []
for _ in range(M):
    op = tuple(map(int, input().split()))
    if op[0] == 1:
        update(op[1]-1, op[2]-1, op[3])
    else:
        query(op[1]-1)

print('\n'.join(ans))