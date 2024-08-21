const [_, A, B] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map(x=>new Set(x.trim().split(' ').map(Number)));
const C = [...A].filter(x => !B.has(x)).sort((a,b) => a-b)
console.log(C.length);
console.log(C.join(' '));