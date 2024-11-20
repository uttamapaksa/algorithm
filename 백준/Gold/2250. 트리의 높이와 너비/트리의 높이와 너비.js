function inorder(n, l) {
    if (!n) return;
    inorder(left[n], l+1);
    idx++;
    if (level[l]) {
        level[l][1] = idx;
    } else {
        level[l] = [idx, idx];
    }
    inorder(right[n], l+1);
}

const [[N], ...ipt] = require('fs').readFileSync(0).toString().trim().split('\n').map(x=>x.split(' ').map(Number));
const par = Array.from({ length: N+1 }, (_, i) => i);
const left = Array(N+1).fill(0);
const right = Array(N+1).fill(0);

for (const [n, l, r] of ipt) {
  if (l !== -1) {
      left[n] = l;
      par[l] = n;
  }
  if (r !== -1) {
      right[n] = r;
      par[r] = n;
  }
}

let idx = 0;
const level = {};
for (let i=1; i<=N; i++) {
  if (i === par[i]) {
      inorder(i, 1);
      break;
  }
}

let ansLevel = 10001;
let ansWidth = 0;
for (const k of Object.keys(level).map(Number).sort((a,b)=>a-b)) {
    const width = level[k][1] - level[k][0] + 1;
    if (ansWidth < width) {
        ansLevel = k;
        ansWidth = width;
    }
}

console.log(ansLevel, ansWidth);
