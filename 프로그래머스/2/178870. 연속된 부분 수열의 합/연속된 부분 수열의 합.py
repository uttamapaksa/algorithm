def solution(sequence, k):
    n = len(sequence)
    i = j = 0
    sums = sequence[0]
    answer = [0, 1000000]   

    while True:
        if sums > k:
            sums -= sequence[i]
            i += 1
        else:
            if sums == k:
                if answer[1] - answer[0] > j - i:
                    answer = [i, j]
            j += 1
            if j == n:
                break
            sums += sequence[j]
        
    return answer