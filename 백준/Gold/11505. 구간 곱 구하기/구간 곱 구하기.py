def update(b, c):
    b += size
    tree[b] = c
    while b > 1:
        if b % 2: tree[b//2] = (tree[b-1] * tree[b]) % MOD
        else: tree[b//2] = (tree[b] * tree[b+1]) % MOD
        b //= 2


def multi(left, right):
    left += size; right += size
    res = 1
    while left <= right:
        if left % 2:
            res = (res * tree[left]) % MOD
            left += 1;
        if not right % 2:
            res = (res * tree[right]) % MOD
            right -= 1;
        left //= 2; right //= 2
    ans.append(res)


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
MOD = 1000000007

size = 1
while size < n:
    size <<= 1
tree = [1] * (size * 2)
for i in range(n):
    tree[size+i] = arr[i]
for i in range(size * 2 - 2, 0, -2):
    tree[i//2] = (tree[i] * tree[i+1]) % MOD

ans = []
size -= 1
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        multi(b, c)

print("\n".join(map(str, ans)))