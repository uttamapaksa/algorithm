import sys; input = sys.stdin.readline

def update(num):
    idx = num + size - 1
    while idx:
        tree[idx] += 1
        idx >>= 1

def query(num):
    idx = 1
    tree[idx] -= 1
    while idx < size:
        left = idx * 2
        right = idx * 2 + 1
        if num > tree[left]:
            num -= tree[left]
            idx = right
        else:
            idx = left
        tree[idx] -= 1
    ans.append(str(idx - size + 1))

size = 2097152
tree = [0] * (size * 2)
ans = []

for _ in range(int(input())):
    T, X = map(int, input().split())
    if T == 1:
        update(X)
    else:
        query(X)

sys.stdout.write('\n'.join(ans))