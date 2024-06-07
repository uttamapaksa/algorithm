def solution(memory, musicinfos):
    idx = 0
    tmps = []
    m = len(memory)
    while idx < m:
        tmp = memory[idx]
        idx += 1
        if idx < m and memory[idx] == "#":
            tmps.append(tmp.lower())
            idx += 1
        else:
            tmps.append(tmp)
    memory = "".join(tmps)
    
    arr = []
    n = len(musicinfos)
    for i in range(n):
        s, e, title, song = musicinfos[i].split(",")
        sh, sm = map(int, s.split(":"))
        eh, em = map(int, e.split(":"))
        time = (eh * 60 + em) - (sh * 60 + sm)
        
        idx = 0
        tmps = []
        m = len(song)
        while idx < m:
            tmp = song[idx]
            idx += 1
            if idx < m and song[idx] == "#":
                tmps.append(tmp.lower())
                idx += 1
            else:
                tmps.append(tmp)
        m = len(tmps)
        div, mod = time // m, time % m
        song = ""
        song += "".join(tmps) * div
        song += "".join(tmps[:mod])
        arr.append((time, n-i, title, song))       
    
    arr.sort(reverse=True)
    answer = "(None)"
    for _, _, title, song in arr:
        if memory in song:
            answer = title
            break
            
    return answer