function addend(c: number, x: number) {
  if (!c) return 2;
  else if (c === x) return 1;
  else if (c+x === 4 || c+x === 6) return 4;
  else return 3;
}


function sol() {
  let dp: number[][] = Array.from({length: 5}, () => Array(5).fill(0));
  let dp2: number[][] = Array.from({length: 5}, () => Array(5).fill(0));
  // first step
  let x = arr[0];
  dp[x][0] = 2;
  dp[0][x] = 2;

  for (let i=1; i<N; i++) {
    x = arr[i]
    dp2 = Array.from({length: 5}, () => Array(5).fill(0));
    // DP
    for (let l=0; l<5; l++) {
      for (let r=0; r<5; r++) {
        if (!dp[l][r]) continue;
        // left
        if (!dp2[x][r]) dp2[x][r] = dp[l][r] + addend(l, x);
        else dp2[x][r] = Math.min(dp2[x][r], dp[l][r] + addend(l, x));
        // right
        if (!dp2[l][x]) dp2[l][x] = dp[l][r] + addend(r, x);
        else dp2[l][x] = Math.min(dp2[l][x], dp[l][r] + addend(r, x));
      }
    }
    dp = dp2;
  }

  let ans = 400000;
  for (const r of dp) {
    for (const c of r) {
      if (c) {
        ans = Math.min(ans, c);
      }
    }
  }
  return ans;
}


const arr: number[] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split(" ").map(Number);
arr.pop();
const N: number = arr.length;
console.log(N ? sol() : 0);