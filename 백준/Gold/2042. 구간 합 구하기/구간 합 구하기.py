def build():
    for i in range(n):
        tree[size+i] = arr[i]
    for i in range(size * 2 - 2, 0, -2):
        tree[i//2] = tree[i] + tree[i+1]

def update(b, c):
    b += size
    delta = c - tree[b]
    while b > 0:
        tree[b] += delta
        b //= 2

def sum(left, right):
    left += size
    right += size
    res = 0
    while left <= right:
        if left % 2 == 1: res += tree[left]; left += 1
        if right % 2 == 0: res += tree[right]; right -= 1
        left //= 2; right //= 2
    return str(res)


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

size = 1
while size < n:
    size <<= 1
tree = [0] * (size * 2)
build()

ans = []
size -= 1
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        ans.append(sum(b, c))
print("\n".join(ans))