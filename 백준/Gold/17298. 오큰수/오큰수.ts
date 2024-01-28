const [N, arr]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x: string)=>x.trim().split(/\s/).map((x:string)=>parseInt(x)));
const stack: number[] = [];
const ans: number[] = new Array(N[0]).fill(-1);
let l: number = 0 // stack.length

for (let i=0; i<N[0]; i++) {
  while (l > 0 && arr[stack[l-1]] < arr[i]) {
    ans[stack.pop() as number] = arr[i];
    l -= 1;
  }
  stack.push(i)
  l += 1;
}

console.log(ans.reduce((a, c)=> a + `${c} `, ''))