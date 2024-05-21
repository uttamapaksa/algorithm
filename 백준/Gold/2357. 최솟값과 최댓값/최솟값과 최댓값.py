n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

size = 1
while size < n:
    size <<= 1

tree = [[0, 0] for _ in range(size * 2)]  # min, max
for i in range(n):
    tree[size+i] = [arr[i], arr[i]]
for i in range(size * 2 - 2, 0, -2):
    tree[i//2] = [min(tree[i][0], tree[i+1][0]), max(tree[i][1], tree[i+1][1])]
size -= 1

ans = []
for _ in range(m):
    l, r = map(int, input().split())
    l += size; r += size
    minv = 1000000000; maxv = 1
    while l <= r:
        if l % 2:
            minv = min(minv, tree[l][0])
            maxv = max(maxv, tree[l][1])
            l += 1
        if not r % 2:
            minv = min(minv, tree[r][0])
            maxv = max(maxv, tree[r][1])
            r -= 1
        l //= 2; r //= 2
    ans.append(f'{minv} {maxv}')

print("\n".join(ans))