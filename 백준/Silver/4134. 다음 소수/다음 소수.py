t=int;i=input
for _ in range(t(i())):
    n=t(i())
    if n < 3:
        print(2)
        continue
    while 1:
        for k in range(2, t(n**0.5)+1):
            if not n%k:
                break
        else:
            print(n)
            break
        n+=1