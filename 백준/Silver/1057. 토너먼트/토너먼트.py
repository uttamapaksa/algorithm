N, kim, im = map(int, input().split())
round = 0
while kim != im:
    kim = (kim + 1) >> 1
    im = (im + 1) >> 1
    round += 1
print(round)