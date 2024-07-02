def check(strs):
    n = len(strs)
    i = 0
    while i < n:
        if strs[i] == '0':  # 01
            if i+1 == n or strs[i+1] != '1':
                return 'NO'
            i += 2
        else:  # 10
            if i+1 == n or strs[i+1] != '0':
                return 'NO'
            i += 2
            if i == n or strs[i] != '0':  # 0+
                return 'NO'
            i += 1
            while i < n and strs[i] == '0':
                i += 1
            if i == n or strs[i] != '1':  # 1+
                return 'NO'
            i += 1
            while i < n and strs[i] == '1':
                if i+1 < n and strs[i+1] == '0':  # 01 | 100+1+
                    if i+2 < n and strs[i+2] == '1':  # 01
                        i += 3
                    break
                i += 1
    return 'YES'


for _ in range(int(input())):
    print(check(input()))