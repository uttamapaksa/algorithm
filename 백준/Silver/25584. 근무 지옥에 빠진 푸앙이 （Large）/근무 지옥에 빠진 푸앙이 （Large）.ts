const input: string[] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n');
const N = parseInt(input[0]);

const workTimeObj: Record<string, number> = {};
let i = 1;
for (let j=0; j<N; j++) {
  for (const time of [4, 6, 4, 10]) {
    for (const name of input[i++].trim().split(' ')) {
      if (name === '-') continue;
      if (!workTimeObj[name]) workTimeObj[name] = time;
      else workTimeObj[name] += time;
    }
  }
}

const workTimeArr = Array.from(Object.values(workTimeObj)).sort((a,b) => a-b);
if (!workTimeArr.length|| workTimeArr[workTimeArr.length-1]-workTimeArr[0] <= 12) {
  console.log('Yes');
} else {
  console.log('No');
}