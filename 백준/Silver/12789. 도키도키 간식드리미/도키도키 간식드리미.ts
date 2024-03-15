const [_, ...arr]: number[] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split(/\s+/).map(Number);
const stack: number[] = [];
let curr = 1;
let ans = 'Nice';

for (const x of arr) {
  if (x === curr) {
      curr++;
      while (stack.length && stack[stack.length - 1] === curr) {
          stack.pop();
          curr++;
      }
  } else if (!stack.length || stack[stack.length - 1] > x) {
      stack.push(x);
  } else {
      ans = 'Sad';
      break;
  }
}

console.log(ans);