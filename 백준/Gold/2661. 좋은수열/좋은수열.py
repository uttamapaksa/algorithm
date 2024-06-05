def sol(v, k):
    global find
    if k == n:
        print(v[1:])
        find = 1
        return
    for a in ("1", "2", "3"):
        nv = v + a
        for l in range(1, len(nv)//2+1):
            if nv[-l:] == nv[-(2*l):-l]:
                break
        else:
            sol(nv, k+1)
            if find:
                return


n = int(input())
find = 0
sol("0", 0)