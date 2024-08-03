const [[N, K], ...rows]: number[][] = require('fs').readFileSync(0).toString().split('\n').map(x=>x.trim().split(' ').map(x=>+x));
const len = N*K;
const next = Array.from({length: len}, (_,i) => i+1); next[len-1] = 0;
const cards: number[][] = [];
let id = 0;
for (let row of rows) {
  for (let val of row) {
    cards.push([id++, val])
  }
}

id = len-1;
for (let i=1; i<len; i++) {
  const val = cards[next[id]][1];
  next[id] = next[next[id]]
  for (let j=0; j<val-1; j++) {
    id = next[id];
  }
}

const [a, b]: number[] = cards[next[id]];
console.log(`${Math.floor(a/K)+1} ${b}`);