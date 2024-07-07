N = int(input())
arr = [*map(int, input().split())]
pv = pi = nv = ni = 0
ans = cnt = 0

for i in range(N):
    if arr[i] != nv:
        if arr[i] == pv:
            pv, pi, nv, ni = nv, ni, pv, i
        else:
            pv, pi, nv, ni = nv, ni, arr[i], i
            cnt = i - pi
    cnt += 1
    if ans < cnt:
        ans = cnt

print(ans)