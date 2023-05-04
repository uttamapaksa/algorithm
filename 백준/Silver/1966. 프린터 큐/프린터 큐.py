test_case = int(input())

for i in range(test_case):
    N, M = tuple(map(int, input().split()))
    papers = list(map(int, input().split()))
    my_paper = papers[:]
    my_paper[M] += 0.1
    ans = my_paper[M]

    cnt = 1
    while True:
        if max(papers) == papers[0]:
            if my_paper[0] == ans:
                break
            else:
                papers.pop(0)
                my_paper.pop(0)
                cnt += 1
        else:
            papers.append(papers.pop(0))
            my_paper.append(my_paper.pop(0))
    print(cnt)