def build():
    for i in range(n):
        tree[size+i] = arr[i]
    for i in range(size * 2 - 2, 0, -2):
        tree[i//2] = min(tree[i], tree[i+1])


def max(left, right):
    left += size
    right += size
    res = 1000000000
    while left <= right:
        if left % 2 == 1: res = min(res, tree[left]); left += 1
        if right % 2 == 0: res = min(res, tree[right]); right -= 1
        left //= 2; right //= 2
    return res

# input
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# init
size = 1
while size < n:
    size <<= 1
tree = [0] * (size * 2)
# build tree
build()

# find max
ans = []
size -= 1
for _ in range(m):
    a, b = map(int, input().split())
    ans.append(max(a, b))

# output
print("\n".join(map(str, ans)))