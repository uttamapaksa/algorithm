N, S = map(int, input().split())
arr = list(map(int, input().split()))
visit = [0] * N
ans = 0


def dfs(sumv, k):
    global ans 
    if sumv == S and k > 0: # 처음부터 같을 경우를 배제(k > 0)
        ans += 1 # 뒤에서 또 성립될 수 있으므로 return 하지 않음
    if k == N: return
    
    for i in range(k, N):
        if visit[i]: continue
        visit[i] = 1
        dfs(sumv + arr[i], i+1)
        visit[i] = 0
    

dfs(0, 0)
print(ans)