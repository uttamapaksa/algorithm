for _ in range(int(input())):
    n, m = map(int, input().split())
    score = [[0, 0] for _ in range(n+1)]
    
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        score[a][0] += p
        score[a][1] += q
        score[b][0] += q
        score[b][1] += p
    
    exp = []
    for i in range(1, n+1):
        s, a = score[i]
        if not s and not a:
            exp.append(0)
        else:
            exp.append(int((s**2 / (s**2 + a**2)) * 1000))
    
    print(max(exp))
    print(min(exp))