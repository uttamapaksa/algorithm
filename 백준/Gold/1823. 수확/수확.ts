const [N, ...arr]: number[] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map(Number);
const dp = Array.from({length: N}, ()=>Array(N).fill(0));

for (let k=1; k<N; k++) {
  dp[0][N-k-1] = dp[0][N-k] + arr[N-k] * k;
}

for (let k=1; k<N; k++) {
  dp[k][N-1] = dp[k-1][N-1] + arr[k-1] * k;
}

for (let i=N-2; i>=0; i--) { // distance
  let k = N-i-1;
  for (let j=1; j<N-i-1; j++) {
    dp[j][j+i] = Math.max(dp[j-1][j+i] + arr[j-1] * k, dp[j][j+i+1] + arr[j+i+1] * k);
  }
}

let answer = 0;
for (let i=0; i<N; i++) {
  answer = Math.max(answer, dp[i][i] + arr[i] * N);
}
console.log(answer);