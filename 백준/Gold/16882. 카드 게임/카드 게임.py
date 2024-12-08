import sys;input=sys.stdin.readline

def sol():
    _ = input()
    A = sorted(map(int, input().split()))

    while A:
        pre = A[-1]
        cnt = 0
        while A and A[-1] == pre:
            A.pop()
            cnt += 1
        if cnt & 1:
            return "koosaga"
    return "cubelover"

print(sol())
        