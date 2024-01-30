const [N, ...arr]: number[] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map((x: string)=>parseInt(x));
const stack: number[] = [];
const cnt: number[] = [];
let l = 0; // stack.length
let ans = 0;
let tmp = 0;

for (let i=0; i<N; i++) {
  while (l > 0 && arr[stack[l-1]] < arr[i]) {
    stack.pop();
    tmp = cnt.pop() as number;
    ans += (l > 1 ? tmp * 2: tmp) + (tmp * (tmp-1)) / 2;
    l -= 1;
  }
  if (l > 0 && arr[stack[l-1]] === arr[i]) {
    cnt[l-1] += 1;
  } else {
    stack.push(i);
    cnt.push(1);
    l += 1;
  }
}

while (l > 0) {
  tmp = cnt.pop() as number;
  ans += (l > 1 ? tmp : 0) + (tmp * (tmp-1)) / 2;
  l -= 1;
}

console.log(ans);