N, M = map(int, input().split())
G = {i: [] for i in range(1, N+1)}
E = {i: 0 for i in range(1, N+1)}

for _ in range(M):
    arr = [*map(int, input().split())]
    l = arr[0]
    for i in range(1, l):
        G[arr[i]].append(arr[i+1])
        E[arr[i+1]] += 1

S = []
for v in E:
    if not E[v]:
        S.append(v)

ans = []
while S:
    v = S.pop()
    ans.append(v)
    for w in G[v]:
        E[w] -= 1
        if not E[w]:
            S.append(w)
            
if len(ans) != N:
    print(0)
else:
    for i in ans:
        print(i)