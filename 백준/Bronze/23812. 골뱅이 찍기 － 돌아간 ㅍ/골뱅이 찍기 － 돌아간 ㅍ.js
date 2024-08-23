const N = +require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim()
const A = '@'.repeat(N);
const B = ' '.repeat(3*N);
const C = A+B+A;
const D = A.repeat(5);
for (let i=0; i<N; i++) {
  console.log(C);
}
for (let i=0; i<N; i++) {
  console.log(D);
}
for (let i=0; i<N; i++) {
  console.log(C);
}
for (let i=0; i<N; i++) {
  console.log(D);
}
for (let i=0; i<N; i++) {
  console.log(C);
}