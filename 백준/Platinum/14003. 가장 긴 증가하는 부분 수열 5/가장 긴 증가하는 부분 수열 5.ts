function bisect_left(x: number) {
  s = 0, e = bs.length;
  while (s < e) {
    m = Math.trunc((s+e)/2);
    if (bs[m][0] < x) {
      s = m + 1;
    } else {
      e = m;
    }
  }
  return s;
}

// input
const [N, ...arr] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split(/\s+/).map(Number);
let bs: number[][] = [], bsl: number = 0, dp: number[][] = [] // bs = [val, curr][], dp = [cnt, prev][]
let s: number, m: number, e: number;

// update DP table by binary search left
for (let i=0; i<N; i++) {
  bsl = bisect_left(arr[i]);
  dp.push([bsl, bsl === 0 ? -1 : bs[bsl-1][1]])
  if (bsl < bs.length) {
    bs[bsl] = [arr[i], i];
  } else {
    bs.push([arr[i], i]);
  }
}

// find idx of max value
let idx: number = 0; 
for (let i=N-1; i>=0; i--) {
  if (dp[i][0] == bs.length - 1) {
    idx = i;
    break
  }
}

// trace and update
let path = `${arr[idx]} `;
while (dp[idx][1] !== -1) {
  idx = dp[idx][1];
  path = `${arr[idx]} ` + path;
} 

// output
console.log(bs.length)
console.log(path)