N, M = map(int, input().split())
memory = [0] + [*map(int, input().split())]
cost = [0] + [*map(int, input().split())]
C = sum(cost)
dp = [0] * (C+1)

for i in range(1, N+1):  # 행: 앱의 종류
    w, v = memory[i], cost[i]
    for j in range(C, v-1, -1):  # 열: 비용
        dp[j] = max(dp[j], dp[j-v] + w)  # 비용 최댓값(활성화, 비활성화)

for i in range(C+1):
    if dp[i] >= M:  # 처음 M에 도달하는 비용 출력
        print(i)
        break