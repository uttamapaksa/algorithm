const [N, arr]: number[][] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map((x: string)=>x.trim().split(/\s/).map((x:string)=>parseInt(x)));
const stack: number[] = [];
let l: number = 0; // stack.length
const ans: number[] = new Array(N[0]).fill(-1);

const cnt: Record<number, number> = {};
for (const x of arr) {
  if (cnt[x]) {
    cnt[x] += 1;
  } else {
    cnt[x] = 1;
  }
}

for (let i=0; i<N[0]; i++) {
  while (l > 0 && cnt[arr[stack[l-1]]] < cnt[arr[i]]) {
    ans[stack.pop() as number] = arr[i];
    l -= 1;
  }
  stack.push(i)
  l += 1;
}

console.log(ans.join(" "));