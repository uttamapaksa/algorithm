const [[N, M], ...arr] = require('fs').readFileSync(0).toString().trim().split('\n').map(x=>x.split(' ').map(Number));
for (let j=1; j<M; j++) {
    arr[0][j] += arr[0][j-1];
}
for (let i=1; i<N; i++) {
    const tmp1 = Array(M).fill(0);
    tmp1[0] = arr[i][0] + arr[i-1][0];
    for (let j=1; j<M; j++) {
        tmp1[j] = arr[i][j] + Math.max(tmp1[j-1], arr[i-1][j]);
    }
    const tmp2 = Array(M).fill(0);
    tmp2[M-1] = arr[i][M-1] + arr[i-1][M-1];
    for (let j=M-2; j>=0; j--) {
        tmp2[j] = arr[i][j] + Math.max(tmp2[j+1], arr[i-1][j]);
    }
    for (let j=0; j<M; j++) {
        arr[i][j] = Math.max(tmp1[j], tmp2[j]);
    }
}

console.log(arr[N-1][M-1]);