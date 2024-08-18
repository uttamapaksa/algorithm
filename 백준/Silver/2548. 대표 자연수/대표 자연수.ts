// input
const [[N], iarr]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(x=>+x));
// init
const arr: number[] = iarr.sort((a,b) => a-b);
let total = arr.reduce((a,c) => a+c, 0) - N*arr[0];
let ans = arr[0];
// calc
for (let i=1; i<N; i++) {
  const diff = arr[i] - arr[i-1]
  if (diff === 0) continue;
  const delta = i*diff - (N-i)*diff 
  total += delta;
  if (delta >= 0) continue;
  ans = arr[i];
}
// output
console.log(ans);