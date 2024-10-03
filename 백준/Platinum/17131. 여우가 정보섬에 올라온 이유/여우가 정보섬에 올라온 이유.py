MOD = 1000000007
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])
coo = {v: i+1 for i, v in enumerate(sorted({v[1] for v in arr}))}
M = len(coo)

tree = [0] * (M+1)
sames, same = [], 100001
count1 = [0] * N
for i in range(N):
    x, y = arr[i]
    if same == x:
        sames.append((y, i))
    else:
        total = 0
        idx = M
        while idx:
            total += tree[idx]
            idx -= idx & -idx
        for py, pi in sames:
            curr = total
            idx = coo[py]
            while idx:
                curr -= tree[idx]
                idx -= idx & -idx
            count1[pi] = curr % MOD
        for py, pi in sames:
            idx = coo[py]
            while idx <= M:
                tree[idx] += 1
                idx += idx & -idx
        same = x
        sames = [(y, i)]

tree = [0] * (M+1)
sames, same = [], 100001
ans = 0
for i in range(N-1, -1, -1):
    x, y = arr[i]
    if same == x:
        sames.append((y, i))
    else:
        total = 0
        idx = M
        while idx:
            total += tree[idx]
            idx -= idx & -idx
        for py, pi in sames:
            curr = total
            idx = coo[py]
            while idx:
                curr -= tree[idx]
                idx -= idx & -idx
            ans += ((curr % MOD) * count1[pi]) % MOD
            ans %= MOD
        for py, pi in sames:
            idx = coo[py]
            while idx <= M:
                tree[idx] += 1
                idx += idx & -idx
        same = x
        sames = [(y, i)]

print(ans)