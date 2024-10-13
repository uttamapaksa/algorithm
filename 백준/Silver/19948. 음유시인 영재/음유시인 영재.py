def sol():
    space = int(input())
    char = list(map(int, input().split()))
    pi = 32
    title = []
    # content
    for ci in ipt:
        ci = ord(ci)
        if pi == ci: continue
        if ci == 32:
            if not space: return -1
            space -= 1
        else:
            ti = ci if ci < 91 else ci-32
            if pi == 32: title.append(ti)
            if not char[ti-65]: return - 1
            char[ti-65] -= 1
        pi = ci
    # title
    for ti in title:
        if pi == ti: continue
        if not char[ti-65]: return - 1
        char[ti-65] -= 1
        pi = ti

    return ''.join(map(chr, title))

ipt = list(input())
print(sol())