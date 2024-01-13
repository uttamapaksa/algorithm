def oper(x):
    global arr, n, m

    # turn 90 degrees
    if x =='C':
        arr = [*zip(*arr)]
        n, m = m, n

    new_arr = []
    new_max = m # max length
    for row in arr:
        cnt = {}
        for val in row: # counting
            if not val: # except zero
                continue
            if val not in cnt:
                cnt[val] = 1
            else:
                cnt[val] += 1
        new_max = max(new_max, len(cnt) * 2)
        cnt = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
        new_arr.append([val for row in cnt for val in row])
    
    # add zero
    for row in new_arr:
        new_max = min(new_max, 100)
        row.extend([0] * (new_max-len(row)))

    # return 90 degrees
    if x =='C':
        arr = [*zip(*new_arr)]
        n, m = new_max, n
    else:
        arr = new_arr
        m = new_max


def sol():
    time = 0
    while time <= 100:
        if r < n and c < m and arr[r][c] == k:
            return time
        if n >= m:
            oper('R')
        else:
            oper('C')
        time += 1
    return -1


r, c, k = map(int, input().split())
r, c = r-1, c-1
arr = [list(map(int, input().split())) for _ in range(3)]
n = m = 3
print(sol())