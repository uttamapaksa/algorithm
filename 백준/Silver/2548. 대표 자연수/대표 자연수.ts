// input
const [[N], iarr]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(x=>+x));
const arr: number[] = iarr.sort((a,b) => a-b);
// init
let diff = arr.reduce((a,c) => a+c-arr[0], 0);
let ans = arr[0];
// calc
for (let i=1; i<N; i++) {
  const v = arr[i];
  if (arr[i-1] === v) continue;
  let tmpDiff = 0;
  for (let j=0; j<i; j++) {
    tmpDiff += v - arr[j]
  }
  for (let j=i+1; j<N; j++) {
    tmpDiff += arr[j] - v
  }
  if (diff > tmpDiff) {
    diff = tmpDiff;
    ans = v;
  };
}
// output
console.log(ans);