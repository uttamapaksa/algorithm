
from bisect import bisect_left

N, H = map(int,input().split())

석순, 종유석 = [], []
for i in range(N):
    if not i & 1:
        석순.append(int(input()))
    else:
        종유석.append(int(input()))
석순.sort()
종유석.sort()

최소파괴수 = 200001
구간수 = 1
for h in range(1,H+1):
    석순통과수, 종유석통과수 = bisect_left(석순, h), bisect_left(종유석, H + 1 - h)
    현재파괴수 = N - (석순통과수 + 종유석통과수)
    if 최소파괴수 > 현재파괴수:
        최소파괴수 = 현재파괴수
        구간수 = 1
    elif 최소파괴수 == 현재파괴수:
        구간수 += 1

print(최소파괴수, 구간수)