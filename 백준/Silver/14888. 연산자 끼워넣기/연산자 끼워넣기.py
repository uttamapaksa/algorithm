from itertools import permutations

N = int(input())
arr = [*map(int, input().split())]
calc = []
for i, c in enumerate([*map(int, input().split())]):
    for _ in range(c):
        calc.append(i)

def plus(x, y): return x + y
def minus(x, y): return x - y
def multi(x, y): return x * y
def divide(x, y): return x // y if x >= 0 else -(-(x) // y)
calc_map = {0: plus, 1: minus, 2: multi, 3: divide}

minv, maxv = 1000000000, -1000000000 
for perm in permutations(calc):
    tmp = arr[0]
    for i in range(N-1):
        tmp = calc_map[perm[i]](tmp, arr[i+1])
    minv = min(minv, tmp)
    maxv = max(maxv, tmp)

print(int(maxv))
print(int(minv))