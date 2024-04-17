def solution(n):
    arr = list(range(n+1))
    i, j, sumv, answer = 1, 1, 0, 1
    
    while j <= n:
        if sumv > n:
            sumv -= arr[i]
            i += 1
        else:
            if sumv == n:
                answer += 1
            sumv += arr[j]
            j += 1
            
    return answer