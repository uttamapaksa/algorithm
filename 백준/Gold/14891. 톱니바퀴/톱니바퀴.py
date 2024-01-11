gear = [list(map(int, input())) for _ in range(4)]
rot = [0, 0, 0, 0] # rotation index


for _ in range(int(input())):
    i, d = map(int, input().split()) # number, direction
    i, d = i-1, -d # index, delta
    turn = [(i, d)]

    # right part
    nd = d
    for ni in range(i+1, 4):
        nd = -nd
        if gear[ni-1][rot[ni-1]-6] != gear[ni][rot[ni]-2]:
            turn.append((ni, nd))
        else:
            break

    # left part
    nd = d
    for ni in range(i-1, -1, -1):
        nd = -nd
        if gear[ni+1][rot[ni+1]-2] != gear[ni][rot[ni]-6]:
            turn.append((ni, nd))
        else:
            break
        
    # turn
    for i, d in turn:
        rot[i] = (rot[i] + 8 + d) % 8


ans = 0
for i in range(4):
    ans += gear[i][rot[i]] * 2**i
print(ans)