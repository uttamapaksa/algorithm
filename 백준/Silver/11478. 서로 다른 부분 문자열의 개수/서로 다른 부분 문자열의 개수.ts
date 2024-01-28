const input: string = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim();
const N: number = input.length;
const subset: Set<string> = new Set();
let tmp: string;

for (let i=0; i<N; i++) {
  tmp = input[i];
  subset.add(tmp);
  for (let j=i+1; j<N; j++) {
    tmp += input[j];
    subset.add(tmp);
  }
}

console.log(subset.size);