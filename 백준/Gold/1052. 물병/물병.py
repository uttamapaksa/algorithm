N, K = map(int, input().split())
M = [0, *map(int, bin(N)[2:])]
if sum(M) <= K:
    print(0)
else:
    cnt, idx, L = 0, 0, len(M)-1
    for i in range(1, L):
        if M[i]:
            cnt += 1
            if cnt == K:
                break
        else:
            idx = i
    M = sum(1 << L-i for i in range(idx) if M[i]) + (1 << L-idx)
    print(M - N)