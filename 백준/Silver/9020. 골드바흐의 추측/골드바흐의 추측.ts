const prime = new Set(Array.from({length:10000}, (_,i) => i));
for (let i=2; i<101; i++) {
  for (let j=i*i; j<10001; j+=i) {
    if (prime.has(j)) {
      prime.delete(j);
    }
  }
}

const [N, ...arr]: number[] = require('fs').readFileSync(0).toString().split('\n').map((x:string)=>+x);
for (const num of arr) {
  for (let i=num/2; i>1; i--) {
    if (prime.has(i) && prime.has(num-i)) {
      console.log(`${i} ${num-i}`);
      break;
    }
  }
}