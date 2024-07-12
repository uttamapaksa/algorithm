from collections import deque
t=int;i=input;_=i();Q=deque()
for s,v in zip(map(t,i().split()),map(t,i().split())):
    if not s:Q.appendleft(v)
M=t(i())
for v in map(t,i().split()):Q.append(v)
print(*[*Q][:M])