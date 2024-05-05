n,x=map(int,input().split())
p=set(range(n,x+1))
for i in range(2,int(x**0.5)+1):
    s=i**2
    for d in range((n-1)//s+1,x//s+1):
        p.discard(s*d)
print(len(p))