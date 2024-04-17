def solution(s):
    answer = [0, 0]
    
    while len(s) > 1:
        zeroCnt = s.count("0")
        s = bin(len(s) - zeroCnt)[2:]
        
        answer[0] += 1
        answer[1] += zeroCnt
        
    return answer