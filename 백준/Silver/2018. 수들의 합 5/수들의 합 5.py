N = int(input())
arr = list(range(N+1))
ans = 0

s = e = 1
sums = arr[e]
while True:
    if sums > N:
        sums -= arr[s]
        s += 1
    else:
        if sums == N:
            ans += 1
        if e == N:
            break
        e += 1
        sums += arr[e]

print(ans)