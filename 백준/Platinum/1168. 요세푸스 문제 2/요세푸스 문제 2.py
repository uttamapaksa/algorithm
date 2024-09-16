import sys; input=sys.stdin.readline

N, K = map(int, input().split())
size = 1 << 17
tree = [0] * (size * 2)
for i in range(N):
    tree[size+i] = 1
for i in range(size-1, 0, -1):
    tree[i] = tree[i*2] + tree[i*2+1]

ans = []
total = N
offset = K - 1

for _ in range(N):
    idx = 1
    tree[idx] -= 1
    k = offset + 1
    while idx < size:
        left = idx * 2
        right = idx * 2 + 1
        if k > tree[left]:
            k -= tree[left]
            idx = right
        else:
            idx = left
        tree[idx] -= 1

    ans.append(idx - size + 1)
    total -= 1
    offset = (offset + K - 1) % (total or 1)

print(f'<{", ".join(map(str, ans))}>')