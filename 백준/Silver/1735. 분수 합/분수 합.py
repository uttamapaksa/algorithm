from math import gcd
n1,d1=map(int,input().split())
n2,d2=map(int,input().split())
n3,d3=n1*d2+n2*d1,d1*d2
g=gcd(n3,d3)
print(n3//g,d3//g)