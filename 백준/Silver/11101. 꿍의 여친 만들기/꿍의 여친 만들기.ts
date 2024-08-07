const input: string[] = require('fs').readFileSync(0).toString().trim().split('\n');
const N = parseInt(input[0]);

let i = 0;
while (i < 2*N) {
  const cnt: Record<string, number> = {};
  
  i++;
  for (const kv of input[i].split(',')) {
    const [k, v] = kv.split(':');
    cnt[k] = parseInt(v);
  }

  i++;
  let ans = 1000;
  for (const vv of input[i].trim().split('|')) {
    const curr = Math.max(...vv.split('&').map(k=>cnt[k]));
    ans = Math.min(ans, curr)
  }
  
  console.log(ans);
}