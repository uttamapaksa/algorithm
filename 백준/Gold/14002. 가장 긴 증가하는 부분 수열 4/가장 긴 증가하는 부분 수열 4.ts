// input
const [N, ...arr] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split(/\s+/).map(Number);
const dp: number[][] = Array(N).fill([1, -1]);

// update DP table
for (let i=N-1; i>=1; i--) {
  for (let j=i-1; j>=0; j--) {
    if (arr[j] < arr[i]) {
      if (dp[j][0] < dp[i][0] + 1) {
        dp[j] = [dp[i][0] + 1, i];
      }
    }
  }
}

// find the idx of max value
let ans1: number = 0;
let idx: number = 0;
for (let i=0; i<N; i++) {
  if (dp[i][0] > ans1) {
    ans1 = dp[i][0];
    idx = i;
  }
}

// trace and update
let ans2: string = `${arr[idx]} `;
while (dp[idx][1] !== -1) {
  idx = dp[idx][1];
  ans2 += `${arr[idx]} `;
}

// output
console.log(ans1);
console.log(ans2);