N = int(input())
print(0 if N==1 else (N**2>>1) + (N&1))