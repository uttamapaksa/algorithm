N = int(input())
A = [*map(int, input().split())]
S = A[:]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            S[i] = max(S[i], A[i] + S[j])

print(max(S))