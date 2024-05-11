def one(arr):
    sets = set()
    for row in arr:
        sets |= set(row)
    if len(sets) == 1:
        return 1
    return 0


def dnc(arr):
    if one(arr):
        return {arr[0][0]: 1}
    n = len(arr)
    if n == 2:
        cnt = {}
        for row in arr:
            for item in row:
                cnt[item] = cnt.get(item, 0) + 1
        return cnt
    
    cnt = {}
    for k, v in dnc([arr[r][:n//2] for r in range(n//2)]).items():
        cnt[k] = cnt.get(k, 0) + v
    for k, v in dnc([arr[r][n//2:] for r in range(n//2)]).items():
        cnt[k] = cnt.get(k, 0) + v
    for k, v in dnc([arr[r][:n//2] for r in range(n//2, n)]).items():
        cnt[k] = cnt.get(k, 0) + v
    for k, v in dnc([arr[r][n//2:] for r in range(n//2, n)]).items():
        cnt[k] = cnt.get(k, 0) + v
    
    if len(cnt) == 1:
        return {arr[0][0]: 1}
    return cnt


def solution(arr):
    res = dnc(arr)
    return [res.get(0, 0), res.get(1, 0)]