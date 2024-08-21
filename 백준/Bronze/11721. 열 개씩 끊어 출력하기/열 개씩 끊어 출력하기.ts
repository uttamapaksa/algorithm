const word: string = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim();
const N = word.length;
const M = Math.ceil(N/10);

for (let i=0; i<M; i++) {
  console.log(word.slice(i*10, (i+1)*10));
}