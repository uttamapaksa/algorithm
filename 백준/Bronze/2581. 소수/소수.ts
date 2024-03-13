const [M, N] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map(Number);
const primes: number[] = [];

for (let i=Math.max(2, M); i<N+1; i++) {
  let isPrime = 1
  for (let j=2; j<Math.trunc(i**1/2 + 1); j++) {
    if (!(i%j)) { isPrime = 0; break } 
  }
  if (isPrime) { primes.push(i) }
}

console.log(primes.length ? `${primes.reduce((a,c)=>a+c)}\n${primes[0]}` : -1)