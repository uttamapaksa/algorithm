x = int(input())
s, e = 1, 10000000
while s <= e:
    m = (s+e) // 2
    a = ((m-1) * m) // 2
    b = (m * (m+1)) // 2
    if a < x <= b:
        break
    if b < x:
        s = m + 1
    else:
        e = m - 1
        
y = m * (m+1) // 2
y = y - x
if not m % 2:
    print(f'{m-y}/{y+1}')
else:
    print(f'{y+1}/{m-y}')