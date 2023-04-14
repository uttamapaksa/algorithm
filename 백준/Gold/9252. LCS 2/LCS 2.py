A, B = [0] + [*input()], [0] + [*input()]
a, b = len(A), len(B)
LCS = [[[0, ''] for _ in range(b+1)] for _ in range(a+1)]

for i in range(1, a):
    for j in range(1, b):
        if A[i] == B[j]: LCS[i][j] = [LCS[i-1][j-1][0] + 1, LCS[i-1][j-1][1] + A[i]]
        elif LCS[i-1][j][0] >= LCS[i][j-1][0]: LCS[i][j] = LCS[i-1][j]
        else: LCS[i][j] = LCS[i][j-1]

for ele in LCS[a-1][b-1]:
    print(ele)