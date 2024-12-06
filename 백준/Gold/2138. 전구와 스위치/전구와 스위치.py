def turn(s,i):
    for j in (i-1,i,i+1):
        if 0<=j<n:
            s[j]^=1

def sol(k):
    global a
    ns = [*s]
    for i in range(2,n):
        if ns[i-1]!=e[i-1]:
            turn(ns,i)
            k+=1
    if ns[n-1]==e[n-1]:
        a=min(a,k)

n,s,e,a=int(input()),[*map(int,input())],[*map(int,input())],100001
if s[0]==e[0]: sol(0);turn(s,0);turn(s,1);sol(2);turn(s,1);turn(s,0)
else: turn(s,0);sol(1);turn(s,0);turn(s,1);sol(1);turn(s,1)
print(-1 if a == 100001 else a)