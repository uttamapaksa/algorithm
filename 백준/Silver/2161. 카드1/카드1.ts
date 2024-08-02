const N: number = +require("fs").readFileSync(process.platform==="linux"?0:'input.txt').toString().trim();
const A: number[] = Array.from({length: N}, (_, i) => i+1);
const R: number[] = [];

for (let i=0; i<A.length; i++) {
  R.push(A[i]);
  A.push(A[++i]);
}

console.log(R.join(' '));