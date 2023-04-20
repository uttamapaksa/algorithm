T = int(input())
n, narr = int(input()), [*map(int, input().split())]
m, marr = int(input()), [*map(int, input().split())]

nsum = {}  # {부배열의 합: 개수}
for i in range(n):
    cursum = 0
    for j in range(i, n):
        cursum += narr[j]
        if cursum not in nsum: nsum[cursum] = 1
        else: nsum[cursum] += 1

ans = 0
for i in range(m):
    cursum = 0
    for j in range(i, m):
        cursum += marr[j]
        nkey = T - cursum  # 합쳐서 T가 되는 부배열의 합
        if nkey in nsum:
            ans += nsum[nkey]

print(ans)