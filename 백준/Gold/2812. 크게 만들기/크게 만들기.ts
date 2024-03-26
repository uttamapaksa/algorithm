const input = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n');
let [N, K]: number[] = input[0].split(' ').map(Number);
const nums: string[] = input[1].split('');
const stack: string[] = [];

for (const num of nums) {
  while (K && stack.length && (stack[stack.length-1] < num)) {
    stack.pop();
    K--;
  }
  stack.push(num);
}

while (K--) {
  stack.pop();
}

console.log(stack.join(''));