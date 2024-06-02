pre = {'1 2':'1 3', '1 3':'1 2', '2 1':'3 1', '2 3':'3 2', '3 1':'2 1', '3 2':'2 3'}
post = {'1 2':'2 1', '1 3':'2 3', '2 1':'1 2', '2 3':'1 3', '3 1':'3 2', '3 2':'3 1'}

n = int(input())
print(2 ** n - 1)

if n <= 20:
    dp = []
    for _ in range(n):
        dp = [pre[v] for v in dp] + ['1 3'] + [post[v] for v in dp]
    print("\n".join(dp))