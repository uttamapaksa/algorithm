n = int(input())
m = n * 2 - 1
arr =[[' '] * m for _ in range(n)]

def small_star(r, c):
    for dr, dc in ((0, 0), (1, -1), (1, 1)):
        arr[r+dr][c+dc] = '*'
    for dc in range(-2, 3):
        arr[r+2][c+dc] = '*'

def draw(r, c, k):
    if not k:
        small_star(r, c)
        return
    d = 3 * k
    draw(r, c, k//2)
    draw(r+d, c-d, k//2)
    draw(r+d, c+d, k//2)
    
k = (n // 3) // 2 
draw(0, m // 2, k)

for l in arr:
    print(''.join(l))
