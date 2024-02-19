import sys; input=sys.stdin.readline

S = 0; ans = ''; N = int(input())
for _ in range(N):
    ipt = input().split()
    if ipt[0] == 'add': S |= 1 << (int(ipt[1]) - 1)
    elif ipt[0] == 'remove': S &= ~(1 << (int(ipt[1]) - 1))
    elif ipt[0] == 'check': print(1 if S & (1 << (int(ipt[1]) - 1)) else 0)
    elif ipt[0] == 'toggle': S ^= 1 << (int(ipt[1]) - 1)
    elif ipt[0] == 'all': S = (1 << 20) - 1
    else: S = 0