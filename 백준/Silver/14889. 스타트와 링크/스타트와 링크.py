from itertools import combinations

N = int(input())
ans = 10001
power = [list(map(int, input().split())) for _ in range(N)]
team_power = [sum(power[i][j] for i in comb for j in comb) for comb in combinations(range(N), N//2)]
M = len(team_power)
for i in range(M//2): ans = min(ans, abs(team_power[i] - team_power[M-i-1]))

print(ans)