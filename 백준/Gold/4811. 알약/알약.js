const arr = require('fs').readFileSync(process.platform === 'linux' ? 0 : 'input.txt').toString().trim().split('\n').map(Number);
const dp = [1];
for (let i=0; i<30; i++) {
    dp.push(dp.reduce((a,c,i) => a+c*dp[dp.length-1-i], 0));
}
arr.pop();
arr.forEach(v => {
    console.log(dp[v]);
})