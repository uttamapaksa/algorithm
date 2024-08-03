const P = Array(10001).fill(1);
for (let i=2; i<101; i++) {
  for (let j=i*i; j<10001; j+=i) {
    if (P[j]) P[j] = 0;
  }
}

const [_, ...A]: number[] = require('fs').readFileSync(0).toString().split('\n').map(x => +x);
A.forEach(v => {
  for (let i=v/2; i>1; i--) {
    if (P[i] && P[v-i]) {
      console.log(`${i} ${v-i}`);
      break;
    }
  }
})