import sys; input=sys.stdin.readline


def update():
    tree[size+A], tree[size+B] = tree[size+B], tree[size+A]
    i = (size+A) >> 1
    while i:
        tree[i] = [min(tree[i*2][0], tree[i*2+1][0]), max(tree[i*2][1], tree[i*2+1][1])]
        i >>= 1
    i = (size+B) >> 1
    while i:
        tree[i] = [min(tree[i*2][0], tree[i*2+1][0]), max(tree[i*2][1], tree[i*2+1][1])]
        i >>= 1


def query():
    l, r = size+A, size+B
    minv, maxv = B+1, A-1
    while l <= r:
        if l & 1:
            minv = min(minv, tree[l][0])
            maxv = max(maxv, tree[l][1])
            l += 1
        if not r & 1:
            minv = min(minv, tree[r][0])
            maxv = max(maxv, tree[r][1])
            r -= 1
        l >>= 1; r >>= 1
    print('YES' if minv == A and maxv == B else 'NO')


for _ in range(int(input())):
    N, K = map(int, input().split())

    size = 1
    while size < N:
        size <<= 1
    tree = [[0, 0] for _ in range(size*2)]  # min, max
    for i in range(N):
        tree[size+i] = [i, i]
    for i in range(size*2-2, 0, -2):
        tree[i>>1] = [min(tree[i][0], tree[i+1][0]), max(tree[i][1], tree[i+1][1])]

    for _ in range(K):
        Q, A, B = map(int, input().split())
        if Q:
            query()
        else:
            update()