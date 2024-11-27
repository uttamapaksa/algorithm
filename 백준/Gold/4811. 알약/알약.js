const arr = require('fs').readFileSync(0).toString().trim().split('\n').map(Number);
const dp = [1];
for (let i=0; i<30; i++) {
    dp.push(dp.reduce((a,c,i) => a+c*dp[dp.length-1-i], 0));
}
const ans = [];
for (let i=0; i<arr.length-1; i++) {
    ans.push(dp[arr[i]]);
}
console.log(ans.join('\n'));