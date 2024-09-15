import sys; input = sys.stdin.readline

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
        l, r, k = op[1]-1+size, op[2]-1+size, op[3]
        while l <= r:
            if l & 1:
                tree[l] += k
                l += 1
            if not r & 1:
                tree[r] += k
                r -= 1
            l >>= 1; r >>= 1
    else:
        x = op[1]-1+size
        res = arr[x-size]
        while x:
            res += tree[x]
            x >>= 1
        ans.append(str(res))

print('\n'.join(ans))