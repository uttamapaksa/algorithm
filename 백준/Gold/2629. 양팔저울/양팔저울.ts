const [N, weights, M, beads]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x: string)=>x.trim().split(/\s/).map((x:string)=>parseInt(x)));
const comb: Set<number> = new Set();
comb.add(0);
const tmp: Set<number> = new Set();

for (const x of weights) {
  tmp.clear()

  for (const c of Array.from(comb)) {
    tmp.add(x + c)
    tmp.add(Math.abs(x - c))
  }

  tmp.forEach((t) => comb.add(t))
}

let ans: string = "";
for (const b of beads) {
  if (comb.has(b)) {
    ans += "Y ";
  } else {
    ans += "N ";
  }
}

console.log(ans);