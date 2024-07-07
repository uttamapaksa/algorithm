A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())

print(int(0 < P % (A+B) <= A) + int(0 < P % (C+D) <= C))
print(int(0 < M % (A+B) <= A) + int(0 < M % (C+D) <= C))
print(int(0 < N % (A+B) <= A) + int(0 < N % (C+D) <= C))