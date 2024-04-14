N, S = map(int, input().split())
M = N >> 1
arr = [*map(int, input().split())]

comb1 = {}
stack = [(0, 0)]
while stack:
    v, k = stack.pop()
    for i in range(k, M):
        nv = v + arr[i]
        comb1[nv] = comb1.get(nv, 0) + 1
        stack.append((nv, i + 1))

comb2 = {}
stack = [(0, M)]
while stack:
    v, k = stack.pop()
    for i in range(k, N):
        nv = v + arr[i]
        comb2[nv] = comb2.get(nv, 0) + 1
        stack.append((nv, i + 1))

answer = 0
answer += comb1.get(S, 0) # comb1
answer += comb2.get(S, 0) # comb2
answer += sum([v * comb2.get(S - k, 0) for k, v in comb1.items()]) # comb1 * comb2
print(answer)