function comb(k, s, p) {
  if (k == N) {
    if (ans < s) {
      ans = s;
    }
    return;
  }
  for (let i = 0; i < N; i++) {
    if (visit[i]) continue;
    visit[i] = 1;
    comb(k + 1, s + Math.abs(p - arr[i]), arr[i]);
    visit[i] = 0;
  }
}

const input = require('fs').readFileSync(process.platform === 'linux' ? 0 : 'input.txt').toString().trim().split('\n');
const N = +input[0];
const arr = input[1].split(' ').map(Number);
const visit = Array(N).fill(0);

let ans = 0;
for (let i=0; i<N; i++) {
  visit[i] = 1
  comb(1, 0, arr[i]);
  visit[i] = 0
}
console.log(ans);