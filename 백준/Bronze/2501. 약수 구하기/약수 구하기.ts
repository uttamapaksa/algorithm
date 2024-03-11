const [N, K] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split(' ').map(Number);
let ans = 0, cnt = 0;
for (let i=1; i<=N; i++) {
  if (N/i === Math.trunc(N/i)) {
    if (++cnt === K) {
      ans = i;
      break;
    }
  }
}

console.log(ans);