from itertools import combinations

N = int(input())
P = [0] + [*map(int, input().split())]
G = [0] + [[*map(int, input().split())][1:] for _ in range(N)]

# whether the target can be a separate district from other
def same_district(target, other):
    S = [target[0]]
    V = {target[0]}
    while S:
        u = S.pop()
        for v in G[u]:
            if v in other: continue
            if v in V: continue
            S.append(v)
            V.add(v)
    if len(V) != len(target):
        return False
    return True

# all combinations
all = [c for i in range(1, N) for c in combinations(range(1, N+1), i)]
T = len(all)
# combinations of two districts and distances between them
combs = [[abs(sum(P[e] for e in all[i]) - sum(P[e] for e in all[T-i-1])), all[i], all[T-i-1]] for i in range(T//2)]
combs.sort()

for comb in combs:
    d, e1, e2 = comb
    if same_district(e1, e2) and same_district(e2, e1):
        print(d)
        break
else:
    print(-1)