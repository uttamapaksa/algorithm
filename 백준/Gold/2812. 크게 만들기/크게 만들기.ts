const input = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n');
const [N, K]: number[] = input[0].split(' ').map(Number);
const nums: number[] = input[1].split('').map(Number);
const stack: number[] = [];
let minusCount = K;

for (let i = 0; i < N; i++) {
  while (minusCount && stack.length && (stack[stack.length-1] < nums[i])) {
    stack.pop();
    minusCount--;
  }
  stack.push(nums[i]);
}

while (minusCount--) {
  stack.pop();
}

console.log(stack.join(''));