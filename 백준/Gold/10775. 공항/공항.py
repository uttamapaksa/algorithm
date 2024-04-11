def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def docking(x):
    root = find(x)
    parent[root] = find(root - 1)
    return root


G, P = int(input()), int(input())
parent = [i for i in range(G+1)]
answer = 0

planes = [int(input()) for _ in range(P)]
for plane in planes:
    if docking(plane):
        answer += 1
    else:
        break

print(answer)