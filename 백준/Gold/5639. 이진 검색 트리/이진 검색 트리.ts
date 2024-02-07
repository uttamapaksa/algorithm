const arr: number[] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map(Number);
const L: Record<number, number> = {};
const R: Record<number, number> = {};
const root: number = arr[0];
const stack: number[] = [root];
let curr: number, next: number;

for (let i=1; i<arr.length; i++) {
  curr = stack[stack.length-1];
  next = arr[i];
  
  if (curr > next) {
    L[curr] = next;
  } else {
    while (stack.length && stack[stack.length-1] < next) {
      curr = stack.pop() as number;
    }
    R[curr] = next;
  }
  stack.push(next);
}

function postOrder(x: number) {
  if (!x) return;
  postOrder(L[x])
  postOrder(R[x])
  console.log(x)
}

postOrder(root);