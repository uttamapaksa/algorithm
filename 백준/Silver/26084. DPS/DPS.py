from math import comb

smap = {}
for c in input():
    smap[c] = smap.get(c, 0) + 1
nmap = {}
for c in (input()[0] for _ in range(int(input()))):
    nmap[c] = nmap.get(c, 0) + 1

ans = 1
for k in smap:
    ans *= comb(nmap.get(k, 0), smap[k])
print(ans)