mxd = 0
mnv = 10**9
_ = input()
arr = [*map(int, input().split())]

res = []
for v in arr:
    if mnv > v:
        mnv = v
    elif mxd < v-mnv:
        mxd = v-mnv
    res.append(mxd)

print(' '.join(map(str, res)))