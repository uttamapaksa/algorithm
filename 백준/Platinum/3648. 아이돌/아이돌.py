import sys; sys.setrecursionlimit(1000); input=sys.stdin.readline

while 1:
    try:
        # input
        N, M = map(int, input().split())
        L = 2*(N+1)
        G = [set() for _ in range(L)]
        for _ in range(M):
            a, b = map(int, input().split())
            G[-a].add(b)
            G[-b].add(a)
        G[-1].add(1)

        # SCC
        def tarjan(u):
            global id
            id += 1
            ids[u] = par = id
            stack.append(u)
            for v in G[u]:
                if not ids[v]:
                    par = min(par, tarjan(v))
                    if not par:
                        return 0
                elif not finished[v]:
                    par = min(par, ids[v])
            if par == ids[u]:
                curr = set()
                while 1:
                    v = stack.pop()
                    if -v in curr:
                        return 0
                    finished[v] = True
                    curr.add(v)
                    if u == v:
                        break
            return par

        id = 0
        ids = [0] * L
        finished = [False] * L
        stack = []

        # output
        for u in range(1, L):
            if not ids[u]:
                if not tarjan(u):
                    print('no')
                    break
        else:
            print('yes')
    except:
        break