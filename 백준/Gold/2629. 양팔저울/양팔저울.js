const [N, weights, M, beads] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map(x=>x.trim().split(/\s/).map(x=>parseInt(x)));
const comb = new Set([0]);
const tmp = new Set();

// brute force to find all combiantions
for (const x of weights) {
  tmp.clear();

  for (const c of comb) {
    tmp.add(x+c); // sum
    tmp.add(x>c ? x-c : c-x); // difference
  }

  for (const t of tmp) {
    comb.add(t);
  }
}

let ans = "";
for (const b of beads) {
  if (comb.has(b)) {
    ans += "Y ";
  } else {
    ans += "N ";
  }
}

console.log(ans);