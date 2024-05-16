N, K = map(int, input().split())
arr = [*map(int, input().split())]
multitap = set()
ans = 0

for i in range(K):
    v = arr[i]
    if len(multitap) < N or v in multitap:
        multitap.add(v)
    else:
        next = set()
        for j in range(i+1, K):
            if len(next) == N-1:
                break
            if arr[j] in multitap:
                next.add(arr[j])
                
        next = list(multitap - next)
        multitap.remove(next[0])
        multitap.add(v)
        ans += 1

print(ans)