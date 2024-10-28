strs = input()
total = len(strs)
cursor = total
node = {-1: -1, 0: '', 1: -1}
for char in strs:
    node[1] = {-1: node, 0: char, 1: -1}
    node = node[1]

for _ in range(int(input())):
    ipt = input()
    if ipt == 'L':
        if cursor > 0:
            cursor -= 1
            node = node[-1]
    elif ipt == 'D':
        if cursor < total:
            cursor += 1
            node = node[1]
    elif ipt == 'B':
        if cursor > 0:
            cursor -= 1
            total -= 1
            parent = node[-1]
            child = node[1]
            parent[1] = child
            if child != -1:
                child[-1] = parent
            node = parent
    else:
        cursor += 1
        total += 1
        char = ipt.split()[1]
        child = node[1]
        node[1] = {-1: node, 0: char, 1: child}
        if child != -1:
            child[-1] = node[1]
        node = node[1]

ans = []
while node[-1] != -1:
    node = node[-1]
while node[1] != -1:
    node = node[1]
    ans.append(node[0])
print(''.join(ans))