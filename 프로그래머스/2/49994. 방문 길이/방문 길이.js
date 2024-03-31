function solution(dirs) {
    const delta = {'U': [-1, 0], 'D': [1, 0], 'R': [0, -1], 'L': [0, 1]};
    const visit = new Set();
    let r = 0, c = 0;
    
    for (const dir of dirs) {
        const [dr, dc] = delta[dir];
        const [nr, nc] = [r + dr, c + dc];
        if (Math.abs(nr) > 5 || Math.abs(nc) > 5) continue;
        visit.add(`${(nr + r) / 2},${(c + nc) / 2}`); 
        r = nr, c = nc;
    }
    
    const ansewr = visit.size;
    return visit.size;
}