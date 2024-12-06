import sys; sys.setrecursionlimit(100000)

def turn(i):
    for j in (i-1, i, i+1):
        if 0 <= j < n:
            s[j] ^= 1

def check():
    for j in range(n):
        if s[j] != e[j]:
            return 0
    return 1

def sol(i, k):
    global a
    if k >= a:
        return
    if i >= 2 and s[i-2] != e[i-2]:
        return
    if i == n:
        if check():
            a = k
        return
    sol(i+1, k)
    turn(i)
    sol(i+1, k+1)
    turn(i)

n = int(input())
s = [*map(int, input())]
e = [*map(int, input())]
a = 300000
sol(0, 0)

print(-1 if a == 300000 else a)