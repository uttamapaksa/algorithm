a = 0
for _ in range(int(input())):
    w = input()
    for i in range(1, len(w)):
        if w[i] != w[i-1] and w[i] in w[:i]: break
    else: a += 1
print(a)