const numbers = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('').map(x=>+x);
if (numbers.reduce((a,c)=>a+c,0) % 3 || !numbers.includes(0)) {
  console.log(-1);
} else {
  console.log(numbers.sort((a,b)=>b-a).join(''));
}