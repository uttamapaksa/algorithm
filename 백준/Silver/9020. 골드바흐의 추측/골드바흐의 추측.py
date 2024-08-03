P = [1] * 10000
for i in range(2, 101):
    for j in range(i*i, 10000, i):
       if P[j]: P[j] = 0

for _ in range(int(input())):
    n = int(input())
    for i in range(n//2, 1, -1):
        if P[i] and P[n-i]:
            print(f'{i} {n-i}')
            break