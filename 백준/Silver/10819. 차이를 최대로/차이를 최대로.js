function comb(k) {
  if (k == N) {
    tmpAns = 0;
    for (let i = 0; i < N - 1; i++) {
      tmpAns += Math.abs(tmpArr[i + 1] - tmpArr[i]);
    }
    ans = Math.max(ans, tmpAns);
    return;
  }
  for (let i = 0; i < N; i++) {
    if (visit[i]) continue;
    visit[i] = 1;
    tmpArr[k] = arr[i];
    comb(k + 1);
    tmpArr[k] = arr[i];
    visit[i] = 0;
  }
}

const input = require('fs').readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const arr = input[1].split(' ').map(Number);
const tmpArr = Array(N).fill(0);
const visit = Array(N).fill(0);
let ans = 0;
let tmpAns = 0;

comb(0);
console.log(ans);
