tc = int(input())
for _ in range(tc):
    abil = []
    for _ in range(11):
        tmp = [*map(int, input().split())]
        tmp = [(i, v) for i, v in enumerate(tmp) if v]
        abil.append(tmp)

    visit = [0] * 11
    ans = 0
    def sol(sumv, k):
        if k == 11:
            global ans
            ans = max(ans, sumv)
            return
        
        for i, v in abil[k]:
            if visit[i]: continue
            visit[i] = 1
            sol(sumv + v, k+1)
            visit[i] = 0
    sol(0, 0)

    print(ans)
