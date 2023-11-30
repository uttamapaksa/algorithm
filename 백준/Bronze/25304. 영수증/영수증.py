total = int(input())
products = int(input())
ret = 0

for _ in range(products):
    cost, count = map(int, input().split())
    ret += cost * count

print((ret == total and 'Yes') or 'No')