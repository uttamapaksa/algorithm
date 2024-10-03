MOD = 1000000007
N = int(input())
arr = [(*map(int, input().split()), i) for i in range(N)]
coo = {v: i for i, v in enumerate(sorted({v[1] for v in arr}))}
M = len(coo)
size = 1
while size < M:
    size <<= 1
ans = 0

arr.sort(key=lambda x: (x[0], -x[1]))
tree = [0] * (2 * size)
count = [0] * N
sames, same = [], 200000
for x, y, i in arr:
    if same == x:
        sames.append((y, i))
    else:
        for py, pi in sames:
            if coo[py] == M-1: continue
            l = size + coo[py]+1
            r = 2 * size - 1
            while l <= r:
                if l & 1:
                    count[pi] += tree[l]
                    l += 1
                if not r & 1:
                    count[pi] += tree[r]
                    r -= 1
                l >>= 1; r >>= 1
            count[pi] %= MOD
        for py, pi in sames:
            l = size + coo[py]
            while l:
                tree[l] += 1
                l >>= 1
        same = x
        sames = [(y, i)]

arr.sort(key=lambda x: (-x[0], -x[1]))
tree = [0] * (2 * size)
sames, same = [], 200000
for x, y, i in arr:
    if same == x:
        sames.append((y, i))
    else:
        for py, pi in sames:
            pv = 0
            if coo[py] == M-1: continue
            l = size + coo[py]+1
            r = 2 * size - 1
            while l <= r:
                if l & 1:
                    pv += tree[l]
                    l += 1
                if not r & 1:
                    pv += tree[r]
                    r -= 1
                l >>= 1; r >>= 1
            pv %= MOD
            ans = (ans + (pv * count[pi]) % MOD) % MOD
        for py, pi in sames:
            l = size + coo[py]
            while l:
                tree[l] += 1
                l >>= 1
        same = x
        sames = [(y, i)]

print(ans)