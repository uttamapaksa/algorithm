function solution(m, n, puddles) {
    const arr = Array.from({length: n}, () => Array(m).fill(0));
    for (const [x, y] of puddles) {
        arr[y-1][x-1] = -1;
    }
    
    for (let r=0; r<n; r++) {
        if (arr[r][0] === -1) break;
        arr[r][0] = 1;
    }
    for (let c=0; c<m; c++) {
        if (arr[0][c] === -1) break;
        arr[0][c] = 1;
    }
    
    for (let r=1; r<n; r++) {
        for (let c=1; c<m; c++) {
            if (arr[r][c] === -1) continue;
            if (arr[r-1][c] !== -1) {
                arr[r][c] += arr[r-1][c];
            }
            if (arr[r][c-1] !== -1) {
                arr[r][c] += arr[r][c-1];
            }
            arr[r][c] %= 1000000007;
        }
    }
    
    return arr[n-1][m-1];
}