def solution(files):
    arr = []
    n = len(files)
    
    for i in range(n):
        file = files[i]
        j = 0
        while not file[j].isdigit():
            j += 1
        head = file[:j].lower()
        k = j
        while k < len(file) and file[k].isdigit():
            k += 1
        number = int(file[j:k])
        tail = file[k:].lower()
        arr.append([head, number, tail, i])
        
    arr.sort(key=lambda x: (x[0], x[1]))
    
    
    answer = []
    for _, _, _, idx in arr:
        answer.append(files[idx])
    return answer