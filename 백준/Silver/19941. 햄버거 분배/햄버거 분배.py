N, K = map(int, input().split())
arr = list(input())
eat = [0] * N

for i in range(N):
    if arr[i] == 'P': continue
    for j in range(max(0, i-K), min(i+K+1, N)):
        if arr[j] == 'H' or eat[j]: continue
        eat[j] = 1
        break

print(sum(eat))