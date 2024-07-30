for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d=(x2-x1)**2+(y2-y1)**2;p=(r1+r2)**2;m=(r1-r2)**2
    if d==0:print(-1 if m==0 else 0)
    elif d>p or d<m:print(0)
    elif d==p or d==m:print(1)
    else:print(2)