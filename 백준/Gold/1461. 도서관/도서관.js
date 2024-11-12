const [[N, M], [...arr]] = require('fs').readFileSync(0).toString().trim().split('\n').map((x) => x.split(' ').map(Number));
const left = [0];
const right = [0];
arr.forEach((x) => {
  if (x > 0) right.push(x);
  else left.push(x);
});
left.sort((a, b) => b - a);
right.sort((a, b) => a - b);

let l = left.length;
let r = right.length;
let ans = 0;

if (-left[l - 1] >= right[r - 1]) {
  ans -= left[l - 1];
  l -= M;
} else {
  ans += right[r - 1];
  r -= M;
}
while (l > 1) {
  ans -= 2 * left[l - 1];
  l -= M;
}
while (r > 1) {
  ans += 2 * right[r - 1];
  r -= M;
}

console.log(ans);
