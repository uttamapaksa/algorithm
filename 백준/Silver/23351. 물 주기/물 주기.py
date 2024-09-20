N, K, A, B=map(int,input().split())
N = N // A

ans = 0
while K:
    for _ in range(N-1):
        K -= 1
        ans += 1
        if not K: break
    else:
        K += B
        K -= 1
        ans += 1
        if not K: break
        continue
    break

print(ans)