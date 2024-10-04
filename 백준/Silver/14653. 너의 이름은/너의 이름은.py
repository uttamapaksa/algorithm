N, K, Q = map(int, input().split())
msg = []
for _ in range(K):
    R, P = input().split()
    R = int(R)
    msg.append((R, P))
num = msg[Q-1][0]

if not num:
    print(-1)
else:
    total = {chr(65+i) for i in range(N)}
    read = {P for R, P in msg if R >= num}
    print(*(sorted(total - read - {'A'})))