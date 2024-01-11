N = int(input())
dp = [1, 1, 1]

for _ in range(N-1):
    a, b, c = dp
    dp = [(a+b+c) % 9901, (a+c) % 9901, (a+b) % 9901]

print(sum(dp) % 9901)