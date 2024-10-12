def cal_diff(arr, re):
    global res, diff
    for j in (range(10), range(9, -1, -1))[re]:
        if j not in arr:
            arr.append(j)
        if len(arr) == L:
            break
    if len(arr) != len(set(arr)):
        return
    tmpres = int(''.join(map(str, arr)))
    tmpdiff = abs(N - tmpres)
    if diff > tmpdiff:
        diff = tmpdiff
        res = tmpres
    elif diff == tmpdiff:
        res = min(res, tmpres)

N = input()
L = len(N)
if L > 10:
    print(9876543210)
elif L == len(set(N)):
    print(N)
else:
    res = 9876543210
    diff = 1000000000000
    cand = list(map(int, N))
    N = int(N)
    for i in range(L-1):
        tmp = cand[:i+1]
        tmpres = [*tmp]
        cal_diff(tmpres, 0)
        tmpres = [*tmp]
        cal_diff(tmpres, 1)
        tmpres = [*tmp]
        if tmpres[i] < 9:
            tmpres[i] += 1
            cal_diff(tmpres, 0)
        tmpres = [*tmp]
        if tmpres[i] > 0:
            tmpres[i] -= 1
            cal_diff(tmpres, 1)
    for j in (range(10)):
        cand[-1] = j
        tmpres = int(''.join(map(str, cand)))
        if len(cand) != len(set(cand)): continue
        if tmpres == N: continue
        tmpdiff = abs(N - tmpres)
        if diff > tmpdiff:
            diff = tmpdiff
            res = tmpres
    print(res)