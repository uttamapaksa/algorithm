def dfs(v, k):
    for i in range(k-1, -1, -1):
        comb.append(int(v + str(i)))
        dfs(v + str(i), i)

comb = []
dfs('', 10)
comb.sort()

N = int(input())
if N > 1022:
    print(-1)
else:
    print(comb[N])