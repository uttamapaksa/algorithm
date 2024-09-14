import sys; input=sys.stdin.readline


def update():
    tree[size+A], tree[size+B] = tree[size+B], tree[size+A]
    i = size+A
    while i:
        i >>= 1 
        left = tree[i*2]
        right = tree[i*2+1]
        tree[i] = [min(left[0], right[0]), max(left[1], right[1])]
    i = size+B
    while i:
        i >>= 1 
        left = tree[i*2]
        right = tree[i*2+1]
        tree[i] = [min(left[0], right[0]), max(left[1], right[1])]


def query():
    minv, maxv = B+1, A-1
    l, r = size+A, size+B
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
    ans.append('YES' if minv == A and maxv == B else 'NO')


ans = []
for _ in range(int(input())):
    # input
    N, K = map(int, input().split())

    # init
    size = 1
    while size < N:
        size <<= 1
    tree = [[0, 0] for _ in range(size*2)]  # min, max
    for i in range(N):
        tree[size+i] = [i, i]
    for i in range(size-1, 0, -1):
        left = tree[i*2]
        right = tree[i*2+1]
        tree[i] = [min(left[0], right[0]), max(left[1], right[1])]

    # operation
    for _ in range(K):
        Q, A, B = map(int, input().split())
        if Q:
            query()
        else:
            update()

# output
print('\n'.join(ans))