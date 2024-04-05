const[[N], arr] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map(x=>x.split(' ').map(Number));
let max1 = 0, min1 = 51, min2 = 101, min3 = 151;

// min1
max1 = Math.max(...arr);
min1 = Math.min(...arr);
// min2
for (let i = 1; i < 5; i++) {
    min2 = Math.min(min2, arr[0] + arr[i], arr[5] + arr[i]);
}
for (const [i, j] of [[1, 2], [1, 3], [4, 2], [4, 3]]) {
    // min2
    min2 = Math.min(min2, arr[i] + arr[j]);
    // min3
    min3 = Math.min(min3, arr[i] + arr[j] + arr[0], arr[i] + arr[j] + arr[5]);
}

let answer = 0;
if (N === 1) {
    answer += arr.reduce((a, c) => a + c) - max1;
} else {
    answer += ((5 * N * N) - (16 * N) + 12) * min1;
    answer += (2 * N - 3) * 4 * min2;
    answer += 4 * min3;
}

console.log(answer);