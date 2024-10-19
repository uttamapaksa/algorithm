from math import gcd

x, y = map(int, input().split())
g = gcd(x, y)
x //= g
y //= g
ans = x + y - 1 

print(ans * g)