index = [0] * 26
for v in input():
    index[ord(v)-97] += 1

print(*index)