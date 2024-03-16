function solution(begin, target, words) {
    const M = begin.length;
    const used = new Set([begin]);
    const queue = [[begin, 0]];
    let front = 0;
    let answer = 0;
    
    while (front < queue.length) {
        const [node, time] = queue[front++]
        if (node === target) {
            answer = time;
            break;
        }
        
        for (const word of words) {
            if (used.has(word)) continue;
            let diff = 0;
            for (let i = 0; i < M; i++) {
                if (node[i] !== word[i]) {
                    diff++;
                }
            }
            if (diff === 1) {
                used.add(word);
                queue.push([word, time + 1]);
            }
        }
    }
    
    return answer;
}