N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0


def dfs(sumv, k, c):
    global ans 
    if k == N: # 끝까지 모든 경우 완전탐색
        if sumv == S and c > 0: # 부분집합이 공집합인 경우를 배제(c > 0)
            ans += 1
        return
    
    dfs(sumv + arr[k], k+1, c+1)
    dfs(sumv, k+1, c)


dfs(0, 0, 0)
print(ans)