N, M = map(int, input().split())
ipts = sorted([input().split() for _ in range(M)], key=lambda x: (int(x[1]), int(x[0])))
print(''.join(x[2] for x in ipts))