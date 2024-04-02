
function turn(num, dir) {
  const delta = new Array(4).fill(0);
  delta[num] -= dir;
  
  // right part
  let nDir = dir;
  for (let i = num; i < 3; i++) {
    if (gear[i][(idx[i] + 2) % 8] !== gear[i+1][(idx[i+1] + 6) % 8]) {
      delta[i+1] += nDir;
      nDir = -nDir;
    } else {
      break;
    }
  }
  
  // left part
  nDir = dir;
  for (let i = num; i > 0; i--) {
    if (gear[i][(idx[i] + 6) % 8] !== gear[i-1][(idx[i-1] + 2) % 8]) {
      delta[i-1] += nDir;
      nDir = -nDir;
    } else {
      break;
    }
  }
  
  // turn
  for (let i = 0; i < 4; i++) {
    idx[i] = (idx[i] + delta[i] + 8) % 8;
  }
}


const input = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n');
const gear = input.slice(0, 4).map(x=>x.split('').map(Number));
const idx = Array(4).fill(0);

for (let i=5; i<input.length; i++) {
  const [num, dir] = input[i].split(' ').map(Number);
  turn(num - 1, dir);
}

let ans = 0;
for (let i=0; i<4; i++) {
  ans += gear[i][idx[i]] * 2 ** i;
}
console.log(ans);