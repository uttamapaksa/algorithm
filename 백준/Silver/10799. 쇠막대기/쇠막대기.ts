const str: string[] = require('fs').readFileSync(0).toString().trim().split('');
const stack: any[] = [];

let ans = 0;
for (const v of str) {
  if (v === '(') {
    stack.push(v);
  } else {
    if (stack[stack.length-1] === '(') {
      stack.pop()
      if (stack.length > 1 && typeof(stack[stack.length-1]) === 'number') {
        stack[stack.length-1]++;
      } else {
        stack.push(1);
      }
    } else {
      const val = stack.pop() as number;
      ans += val + 1;
      stack.pop();
      if (stack.length > 1 && typeof(stack[stack.length-1]) === 'number') {
        stack[stack.length-1] += val;
      } else {
        stack.push(val);
      }
    }
  }
}

console.log(ans);