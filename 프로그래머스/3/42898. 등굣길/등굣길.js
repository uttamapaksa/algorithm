function solution(m, n, puddles) {
    const arr = Array.from({length: n+1}, () => Array(m+1).fill(0));
    for (const [x, y] of puddles) { arr[y][x] = -1; }
    arr[1][1] = 1;
    
    for (let r=1; r<=n; r++) {
        for (let c=1; c<=m; c++) {
            if (arr[r][c] === -1) continue;
            if (arr[r-1][c] !== -1) { arr[r][c] += arr[r-1][c]; }
            if (arr[r][c-1] !== -1) { arr[r][c] += arr[r][c-1]; }
            arr[r][c] %= 1000000007;
        }
    }
    
    return arr[n][m];
}