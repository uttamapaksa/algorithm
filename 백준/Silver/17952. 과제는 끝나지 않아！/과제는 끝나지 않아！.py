a=0;s=[[0,-1]];t=int;i=input
for _ in range(t(i())):
    p=i().split()
    if p[0]=='0':s[-1][1]-=1
    else:s+=[[t(p[1]),t(p[2])-1]]
    if s[-1][1]==0:a+=s.pop()[0]
print(a)