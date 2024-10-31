tc = 0
while True:
    N = int(input())
    if N == 0: break
    
    graph = {}
    for _ in range(N):
        giver, taker = input().split()
        graph[giver] = taker

    cnt = 0
    visit = set()
    for giver in graph:
        if giver in visit: continue
        while giver not in visit:
            visit.add(giver)
            giver = graph[giver]
        cnt += 1

    tc += 1
    print(tc, cnt)