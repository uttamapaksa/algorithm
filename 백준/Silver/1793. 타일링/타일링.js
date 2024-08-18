const arr = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map(x=>+x);
const mx = Math.max(...arr);
const dp = [1n, 1n];

for (let i=2; i<=mx; i++) {
  dp.push(dp[i-2] * 2n + dp[i-1]);
}

arr.forEach(v => {
  console.log(dp[v].toString())
})