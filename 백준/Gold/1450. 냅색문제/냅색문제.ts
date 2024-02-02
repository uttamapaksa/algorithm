function sol() {
  const M = Math.trunc(N/2);
  const left: number[] = weights.slice(0, M);
  const right: number[] = weights.slice(M, N);
  
  let leftSum: number[] = [0];
  let rightSum: number[] = [0];
  let tmp: number[] = [];
  for (const x of left) {
    tmp = [];
    for (const y of leftSum) {
      tmp.push(x+y);
    }
    for (const y of tmp) {
      leftSum.push(y);
    }
  }

  for (const x of right) {
    tmp = [];
    for (const y of rightSum) {
      tmp.push(x+y);
    }
    for (const y of tmp) {
      rightSum.push(y);
    }
  }
  rightSum = rightSum.sort((a,b)=>a-b);

  const end: number = rightSum.length;
  let ans: number = 0, idx: number;
  let s: number, e: number, m: number, target: number;
  for (let x of leftSum) {
    s = 0;
    e = end;
    target = C-x;
    idx = end;
    m = Math.trunc((s+e)/2);
    while (s <= e) {
      m = Math.trunc((s+e)/2);
      if (rightSum[m] > target) { // the first position exceeding the target
        idx = m;
        e = m-1;
      } else {
        s = m+1;
      }
    }
    ans += idx;
  }

  return ans;
}


const [[N, C], weights]: number[][] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map((x:string)=>x.trim().split(" ").map(Number));
console.log(sol());