def comb(k, n):
    if n == 6:
        print(*peak)
    for i in range(k, l):
        peak.append(S[i])
        comb(i+1, n + 1)
        peak.pop()

while 1:
    S = input().split()
    l = int(S.pop(0))
    if not l: break
    peak = []
    comb(0, 0)
    print()