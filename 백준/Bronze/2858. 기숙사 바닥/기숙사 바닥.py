R, B = map(int, input().split())
S = (R-4) // 2
L = (int((S**2 - B*4) ** 0.5) + S) // 2 + 2
W = (R+B) // L
print(L, W)