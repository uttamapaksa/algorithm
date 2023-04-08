N = int(input())
L, R = {}, {}
preo = ino = posto = ''

for _ in range(N):
    p, l, r = input().split()
    L[p] = l if l.isalpha() else 0
    R[p] = r if r.isalpha() else 0

def traversal(k):
    global preo, ino, posto
    if not k: return
    preo += k
    traversal(L[k])
    ino += k
    traversal(R[k])
    posto += k
traversal('A')

print(preo)
print(ino)
print(posto)