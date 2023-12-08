hobits = sorted([int(input()) for _ in range(9)])
key = sum(hobits) - 100

def find_two():
    for i in range(8):
        for j in range(i+1, 9):
            if hobits[i] + hobits[j] == key:
                return i, j
f1, f2 = find_two()

for i in range(9):
    if i in {f1, f2}: continue
    print(hobits[i])
